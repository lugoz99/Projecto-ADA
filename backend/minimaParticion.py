from itertools import combinations
import numpy as np
from scipy.stats import wasserstein_distance

from backend.auxiliares import (
    ordenar_matriz_product,
    repr_current_to_array,
    repr_next_to_array,
)
from backend.marginalizacion import obtener_tabla_probabilidades
from pyemd import emd
from scipy.spatial.distance import pdist, squareform


def calcular_emd(matriz_original, matriz_resultante):
    # Convertir los nombres de las columnas a números binarios.
    estados = [
        np.array(list(map(int, list(columna)))) for columna in matriz_original.columns
    ]
    num_bins = max(len(matriz_original.values[0]), len(matriz_resultante.values[0]))
    distancias = np.zeros((num_bins, num_bins))

    # Calcular la matriz de distancias (distancias de Hamming entre los estados).
    distancias = pdist(estados, metric="hamming") * len(estados[0])
    distancias = squareform(distancias).astype(np.float64)

    # Calcular el EMD.
    histograma1 = matriz_original.values[0][: len(distancias)]
    histograma2 = matriz_resultante.values[0][: len(distancias)]
    # emd_value = emd(matriz_original.values[0], matriz_resultante.values[0], distancias)
    emd_value = emd(histograma1, histograma2, distancias)

    return round(emd_value, 2)


def decomposition(ns, cs, cs_value, probabilities, states):
    memory = {}
    print("|===========================================================|")
    print("|                      Sistema original                     |")
    print("|===========================================================|")
    print("                     " f"{ns}ᵗ⁺¹ | {cs}ᵗ                    ")
    print("|===========================================================|")
    print("\n")
    
    original_system = obtener_tabla_probabilidades(
        repr_current_to_array(cs, cs_value),
        repr_next_to_array(ns),
        probabilities,
        states,
    )
    print(original_system)
    memory = {}
    impresos = set()
    min_emd = float("inf")
    mejor_particion = None
    emd_distance = float("inf")

    def descomponer(ns, cs, memory, states):
        print("CS: ", cs)
        print("NS: ", ns)
        if memory.get(cs) is not None and memory.get(cs).get(ns) is not None:
            if any(memory.get(cs).get(ns)):
                return memory.get(cs).get(ns)

        if len(ns) == 1:
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
                cross_product = np.kron(value, descomponer(ns[i], cs, memory, states))
                value = ordenar_matriz_product(cross_product)
            else:
                value = np.array(descomponer(ns[i], cs, memory, states))

                if memory.get(cs) == None:
                    memory[cs] = {}

                memory[cs][ns[i]] = value

        return value

    for lenNs in range(len(ns) + 1):
        for i in range(len(ns) - lenNs + 1):
            j = i + lenNs - 1
            ns1, ns2 = ns[i : j + 1], ns[:i] + ns[j + 1 :]
            for lenCs in range(len(cs) + 1):
                for x in range(len(cs) - lenCs + 1):
                    z = x + lenCs - 1
                    cs1, cs2 = cs[x : z + 1], cs[:x] + cs[z + 1 :]
                    combinacion_actual = ((ns1, cs1), (ns2, cs2))
                    combinacion_inversa = ((ns2, cs2), (ns1, cs1))
                    if (
                        combinacion_actual not in impresos
                        and combinacion_inversa not in impresos
                    ) or (ns1 == ns and ns2 == "" and cs1 == "" and cs2 == ""):
                        arr1 = np.array(descomponer(ns2, cs2, memory, states))
                        arr2 = np.array(descomponer(ns1, cs1, memory, states))
                        partitioned_system = []
                        if len(arr1) > 0 and len(arr2) > 0:
                            cross_product = np.kron(arr1, arr2)
                            partitioned_system = ordenar_matriz_product(cross_product)
                        elif len(arr1) > 0:
                            partitioned_system = arr1
                        elif len(arr2) > 0:
                            partitioned_system = arr2
                        if len(partitioned_system) > 0:
                            partitioned_system = np.array(partitioned_system)
                            emd_distance = wasserstein_distance(
                                original_system,
                                partitioned_system,
                            )
                            if emd_distance < min_emd:
                                min_emd = emd_distance
                                mejor_particion = (
                                    f"({ns2} | {cs2})",
                                    f" * ({ns1} | {cs1})",
                                )

                        impresos.add(combinacion_actual)
                        impresos.add(combinacion_inversa)
                        print(emd_distance, combinacion_actual)
    return mejor_particion, min_emd
