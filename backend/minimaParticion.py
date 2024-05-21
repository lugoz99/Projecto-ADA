import numpy as np
from scipy.stats import wasserstein_distance

from backend.auxiliares import (
    ordenar_matriz_product,
    repr_current_to_array,
    repr_next_to_array,
)
from backend.marginalizacion import obtener_tabla_probabilidades


def min_particion(ns, cs, cs_value, probabilities, states):
    """
    Calculates the minimum partition of a system based on given inputs.

    Args:
        ns (list): List of next states.
        cs (list): List of current states.
        cs_value (float): Value of the current state.
        probabilities (list): List of probabilities.
        states (list): List of states.

    Returns:
        tuple: A tuple containing the best partition and the minimum Earth Mover's Distance (EMD) value.

    """
    memory = {}
    print("Sistema original")
    print(f"{ns}ᵗ⁺¹ | {cs}ᵗ")
    original_system = obtener_tabla_probabilidades(
        repr_current_to_array(cs, cs_value),
        repr_next_to_array(ns),
        probabilities,
        states,
    )
    memory = {}
    combinaciones_evaluadas = set()
    min_emd = float("inf")
    mejor_particion = None

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
                        print(f"({ns2} | {cs2})", f" * ({ns1} | {cs1})")
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
                        """"
                        se presenta la matriz que representa 
                        las probabilidades de pasar de un estado actual a uno próximo:
                        creando un sistema particionado a partir de dos arrays
                        """
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
                            if emd_distance < min_emd:
                                min_emd = emd_distance
                                mejor_particion = combinacion_actual

                        combinaciones_evaluadas.add(combinacion_actual)
                        combinaciones_evaluadas.add(combinacion_inversa)

    return mejor_particion, round(min_emd, 2)
