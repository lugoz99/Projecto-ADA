from itertools import combinations
import numpy as np
from scipy.stats import wasserstein_distance

from backend.auxiliares import (
    ordenar_matriz_product,
    repr_current_to_array,
    repr_next_to_array,
)
from backend.marginalizacion import obtener_tabla_probabilidades


import numpy as np
from scipy.stats import wasserstein_distance


def compute_original_system(cs, cs_value, ns, probabilities, states):
    return obtener_tabla_probabilidades(
        repr_current_to_array(cs, cs_value),
        repr_next_to_array(ns),
        probabilities,
        states,
    )


def descomponer(ns, cs, cs_value, probabilities, states, memory):
    if cs in memory and ns in memory[cs]:
        return memory[cs][ns]

    if len(ns) == 1:
        print(f"ns : {ns} | cs: {cs} cs_value: {cs_value}")
        value = obtener_tabla_probabilidades(
            repr_current_to_array(cs, cs_value),
            repr_next_to_array(ns),
            probabilities,
            states,
        )
        return value

    value = []
    for i in range(0, len(ns)):
        if len(value) > 0:
            cross_product = np.kron(
                value, descomponer(ns[i], cs, cs_value, probabilities, states, memory)
            )
            value = ordenar_matriz_product(cross_product)
        else:
            value = np.array(
                descomponer(ns[i], cs, cs_value, probabilities, states, memory)
            )

            if memory.get(cs) == None:
                memory[cs] = {}

            memory[cs][ns[i]] = value

    return value


def compute_partitioned_system(ns, cs, cs_value, probabilities, states, memory):
    arr1 = np.array(descomponer(ns[1], cs[1], cs_value, probabilities, states, memory))
    arr2 = np.array(descomponer(ns[0], cs[0], cs_value, probabilities, states, memory))

    partitioned_system = []
    if len(arr1) > 0 and len(arr2) > 0:
        cross_product = np.kron(arr1, arr2)
        partitioned_system = ordenar_matriz_product(cross_product)
    elif len(arr1) > 0:
        partitioned_system = arr1
    elif len(arr2) > 0:
        partitioned_system = arr2

    return np.array(partitioned_system)


def all_combinations(list1, list2):
    result = []
    for i in range(len(list1) + 1):
        for j in range(len(list2) + 1):
            for subset1 in combinations(list1, i):
                for subset2 in combinations(list2, j):
                    subset1 = tuple(subset1)
                    subset2 = tuple(subset2)
                    complement_list1 = tuple(x for x in list1 if x not in subset1)
                    complement_list2 = tuple(x for x in list2 if x not in subset2)
                    result.append(
                        ((subset1, subset2), (complement_list1, complement_list2))
                    )
    return result


def decomposition(ns, cs, cs_value, probabilities, states):
    memory = {}
    original_system = compute_original_system(cs, cs_value, ns, probabilities, states)
    print(f"Sistema Original: {original_system}")
    min_emd = float("inf")
    mejor_particion = None
    impresos = set()

    ns_combinations = all_combinations(ns, cs)
    for (ns1, cs1), (ns2, cs2) in ns_combinations:
        combinacion_actual = ((ns1, cs1), (ns2, cs2))
        combinacion_inversa = ((ns2, cs2), (ns1, cs1))
        if combinacion_actual not in impresos and combinacion_inversa not in impresos:
            partitioned_system = compute_partitioned_system(
                (ns1, ns2), (cs1, cs2), cs_value, probabilities, states, memory
            )
            partitioned_system = compute_partitioned_system(
                (ns1, ns2), (cs1, cs2), cs_value, probabilities, states, memory
            )

            if partitioned_system.size:
                emd_distance = wasserstein_distance(original_system, partitioned_system)
                if emd_distance < min_emd:
                    min_emd = emd_distance
                    mejor_particion = mejor_particion = (
                        f"p({ns2}ᵗ⁺¹|{cs2}ᵗ) * p({ns1}ᵗ⁺¹|{cs1}ᵗ)",
                    )

            impresos.add(combinacion_actual)
            impresos.add(combinacion_inversa)

    return mejor_particion, round(min_emd, 5)
