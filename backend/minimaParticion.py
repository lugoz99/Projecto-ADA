from networkx import tensor_product
import numpy as np
from scipy.stats import wasserstein_distance

from backend.auxiliares import (
    ordenar_matriz_product,
    repr_current_to_array,
    repr_next_to_array,
)
from backend.marginalizacion import obtener_tabla_probabilidades


def min_particion(ns, cs, cs_value, probabilities, states):
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

    print("|===========================================================|")
    print("| Original System: ", original_system, "    |")
    print("|===========================================================|\n")

    
    memory = {}
    combinaciones_evaluadas = set()
    min_emd = float("inf")
    mejor_particion = None
    emd_distance = float("inf")

    # Función recursiva para descomponer el sistema en particiones
    def descomponer_recusivo(ns, cs, memory, states):
        if (cs, tuple(ns)) in memory:
            return memory[(cs, tuple(ns))]
        # Si solo hay un estado siguiente, calcular su tabla de probabilidades
        if len(ns) == 1:
            value = obtener_tabla_probabilidades(
                repr_current_to_array(cs, cs_value),
                repr_next_to_array(ns),
                probabilities,
                states,
            )
            value = np.array(value)
            memory[(cs, tuple(ns))] = value
            return value
        value = None
        for i in range(len(ns)):
            # Descomponer recursivamente en partes más pequeñas
            sub_value = descomponer_recusivo([ns[i]], cs, memory, states)
            if value is None:
                value = sub_value
            else:
                # Realizar el producto tensor para  las particiones
                tensor = np.kron(value, sub_value)
                value = ordenar_matriz_product(tensor)
            memory[(cs, tuple(ns[: i + 1]))] = value
        # Asegurarse de que el valor final no sea None
        if value is None:
            value = np.array([])
        memory[(cs, tuple(ns))] = value
        return value

    for lenNs in range(1, len(ns) + 1):
        for i in range(len(ns) - lenNs + 1):
            j = i + lenNs - 1
            ns1, ns2 = ns[i : j + 1], ns[:i] + ns[j + 1 :]
            for lenCs in range(len(cs) + 1):
                for x in range(len(cs) - lenCs + 1):
                    z = x + lenCs - 1
                    # Dividir la lista de estados actuales en dos partes: cs1 y cs2
                    cs1, cs2 = cs[x : z + 1], cs[:x] + cs[z + 1 :]
                    # Definir la combinación actual de ns1, cs1, ns2 y cs2,
                    # fusionando ns1 con cs1 y ns2 con cs2
                    # para obtener la partición actual
                    combinacion_actual = (
                        (tuple(ns1), tuple(cs1)),
                        (tuple(ns2), tuple(cs2)),
                    )
                    # Definir la combinación inversa de ns1, cs1, ns2 y cs2, fusionando ns1 con ns2 y cs1 con cs2
                    # para obtener la partición inversa
                    combinacion_inversa = (
                        (tuple(ns2), tuple(cs2)),
                        (tuple(ns1), tuple(cs1)),
                    )

                    if (
                        combinacion_actual not in combinaciones_evaluadas
                        and combinacion_inversa not in combinaciones_evaluadas
                    ):
                        print(
                            "|===========================================================|"
                        )
                        print(
                            f"                   ({ns2} | {cs2})", f" * ({ns1} | {cs1})"
                        )
                        print(
                            "|===========================================================|\n\n"
                        )
                        # Descomponer el sistema en particiones
                        particiones_arr1 = descomponer_recusivo(
                            ns2, cs2, memory, states
                        )
                        particiones_arr2 = descomponer_recusivo(
                            ns1, cs1, memory, states
                        )

                        # Asegurarse de que arr1 y arr2 no sean None
                        if particiones_arr1 is None:
                            particiones_arr1 = np.array([])
                        if particiones_arr2 is None:
                            particiones_arr1 = np.array([])
                        partitioned_system = []
                        if particiones_arr1.size > 0 and particiones_arr2.size > 0:
                            tensor = np.kron(particiones_arr1, particiones_arr2)
                            partitioned_system = ordenar_matriz_product(tensor)
                        elif particiones_arr1.size > 0:
                            partitioned_system = particiones_arr1
                        elif particiones_arr2.size > 0:
                            partitioned_system = particiones_arr2

                        if len(partitioned_system) > 0:
                            # Convertir partitioned_system a array de NumPy si no lo es
                            partitioned_system = np.array(partitioned_system)

                            # Calcular la Distancia de Wasserstein (EMD)
                            emd_distance = wasserstein_distance(
                                original_system,
                                partitioned_system,
                            )
                            if emd_distance <= min_emd:
                                min_emd = emd_distance
                                mejor_particion = combinacion_actual

                        combinaciones_evaluadas.add(combinacion_actual)
                        combinaciones_evaluadas.add(combinacion_inversa)

    #print(combinaciones_evaluadas)
    return mejor_particion, round(min_emd, 5)


def decomposition(ns, cs, cs_value, probabilities, states):
    memory = {}
    print("\n")
    print("|===========================================================|")
    print("|                        Probabilities                      |")
    print("|===========================================================|")
    for probabilitie in probabilities:
        print(probabilitie)
    print("|===========================================================|")
    print("\n")

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

    print("|===========================================================|")
    print("| Original System: ", original_system, "    |")
    print("|===========================================================|\n\n")

    # graphProbability(original_system, "orange", f"{ns}ᵗ⁺¹ | {cs}ᵗ = {cs_value}")
    memory = {}
    impresos = set()
    min_emd = float("inf")
    mejor_particion = None
    emd_distance = float("inf")

    def descomponer(ns, cs, memory, states):
        if memory.get(cs) is not None and memory.get(cs).get(ns) is not None:
            if any(memory.get(cs).get(ns)):
                # print("|===========================================================|")
                print("|                      get in memory                        |")
                # print("|===========================================================|\n\n")
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
                value = tensor_product(cross_product)
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

                    # Verificar duplicados
                    combinacion_actual = ((ns1, cs1), (ns2, cs2))
                    combinacion_inversa = ((ns2, cs2), (ns1, cs1))

                    if (
                        combinacion_actual not in impresos
                        and combinacion_inversa not in impresos
                    ) or (ns1 == ns and ns2 == "" and cs1 == "" and cs2 == ""):
                        print(
                            "|===========================================================|"
                        )
                        print(
                            f"                   ({ns2} | {cs2})", f" * ({ns1} | {cs1})"
                        )
                        print(
                            "|===========================================================|\n\n"
                        )
                        arr1 = np.array(descomponer(ns2, cs2, memory, states))
                        arr2 = np.array(descomponer(ns1, cs1, memory, states))

                        partitioned_system = []

                        if len(arr1) > 0 and len(arr2) > 0:
                            cross_product = np.kron(arr1, arr2)
                            partitioned_system = tensor_product(cross_product)

                        elif len(arr1) > 0:
                            partitioned_system = arr1
                        elif len(arr2) > 0:
                            partitioned_system = arr2

                        if len(partitioned_system) > 0:
                            # Convertir partitioned_system a array de NumPy si no lo es
                            partitioned_system = np.array(partitioned_system)

                            # Calcular la Distancia de Wasserstein (EMD)
                            emd_distance = wasserstein_distance(
                                original_system,
                                partitioned_system,
                            )
                            print(emd_distance)
                            if emd_distance <= min_emd:
                                min_emd = emd_distance
                                mejor_particion = combinacion_actual

                        impresos.add(combinacion_actual)
                        impresos.add(combinacion_inversa)

    print("|===========================================================|")
    #print(memory)
    print("|===========================================================|\n\n")

    print("Alejo")

    return mejor_particion, round(min_emd, 5)
