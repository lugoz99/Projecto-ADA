import random
import numpy as np
from itertools import combinations
from scipy.stats import wasserstein_distance


def repr_next_to_array(letras):
    ns_arr = [0] * len(letras)
    return ns_arr


def repr_current_to_array(cs, cs_value):
    cs_dict = {cs[i]: cs_value[i] for i in range(len(cs))}
    cs_arr = [cs_dict.get(c) for c in cs]
    return cs_arr


def ordenar_matriz_product(tensor):
    len_cross = len(tensor)
    if len_cross == 4:
        new_order = [0, 2, 1, 3]
        return tensor[new_order]
    elif len_cross == 8:
        new_order = [0, 1, 2, 3, 4, 6, 5, 7]
        return tensor[new_order]
    return tensor


def getIndicesMarginalizar(states, state):
    availableIndices = []
    indices = {}
    csValue = ""
    for i in range(len(state)):
        if state[i] is not None:
            availableIndices.append(i)
            csValue = str(state[i]) + csValue

    for i in range(len(states)):
        if all(
            j < len(states[i]) for j in availableIndices
        ):  # Verificar que todos los índices están en rango
            key = tuple(states[i][j] for j in availableIndices)
            indices[key] = indices.get(key, []) + [i]

    if csValue == "":
        return indices, 0
    return indices, int(csValue, 2)


def margenaliceNextState(nsIndices, probabilites):
    nsTransitionTable = [[None] * len(nsIndices) for i in range(len(probabilites))]
    currentColumn = 0
    for indices in nsIndices.values():
        for i in range(len(nsTransitionTable)):
            probability = 0
            for j in range(len(indices)):
                probability += probabilites[i][indices[j]]
            nsTransitionTable[i][currentColumn] = probability
        currentColumn += 1
    return nsTransitionTable


def margenaliceCurrentState(csIndices, nsTransitionTable):
    csTransitionTable = [
        [None] * len(nsTransitionTable[0]) for i in range(len(csIndices))
    ]
    currentRow = 0
    for indices in csIndices.values():
        for i in range(len(csTransitionTable[0])):
            probability = 0
            for j in range(len(indices)):
                probability += nsTransitionTable[indices[j]][i]
            csTransitionTable[currentRow][i] = probability / len(indices)
        currentRow += 1
    return csTransitionTable


def obtener_tabla_probabilidades(currentState, nextState, probabilities, states):
    result = []
    csTransitionTable = []
    csIndices, csValueIndex = getIndicesMarginalizar(states, currentState)
    missingCs = any(state is None for state in currentState)
    if missingCs:
        for i, state in enumerate(nextState):
            if state is not None:
                newNs = [None] * len(nextState)
                newNs[i] = nextState[i]
                nsIndices, _ = getIndicesMarginalizar(states, newNs)
                nsTransitionTable = margenaliceNextState(nsIndices, probabilities)
                csTransitionTable = margenaliceCurrentState(
                    csIndices, nsTransitionTable
                )
                if csValueIndex < len(csTransitionTable):  # Verificación de rango
                    csValue = csTransitionTable[csValueIndex]
                else:
                    raise IndexError(
                        f"csValueIndex {csValueIndex} fuera de rango para csTransitionTable de longitud {len(csTransitionTable)}"
                    )
                if len(result) > 0:
                    result = np.kron(result, csValue)
                else:
                    result = csValue
    else:
        nsIndices, _ = getIndicesMarginalizar(states, nextState)
        nsTransitionTable = margenaliceNextState(nsIndices, probabilities)
        csTransitionTable = margenaliceCurrentState(csIndices, nsTransitionTable)
        if csValueIndex < len(csTransitionTable):  # Verificación de rango
            result = csTransitionTable[csValueIndex]
        else:
            raise IndexError(
                f"csValueIndex {csValueIndex} fuera de rango para csTransitionTable de longitud {len(csTransitionTable)}"
            )
    return result


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
            if memory.get(cs) is None:
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
    # Iteramos sobre la longitud de list1 y list2
    for i in range(len(list1) + 1):
        for j in range(len(list2) + 1):
            # Generamos las combinaciones de tamaño i de list1 y tamaño j de list2
            for subset1 in combinations(list1, i):
                for subset2 in combinations(list2, j):
                    # Convertimos los subsets a tuplas
                    subset1 = tuple(subset1)
                    subset2 = tuple(subset2)

                    # Añadimos la combinación y su complemento a la lista de resultados
                    complement_list1 = tuple(x for x in list1 if x not in subset1)
                    complement_list2 = tuple(x for x in list2 if x not in subset2)
                    result.append(
                        ((subset1, subset2), (complement_list1, complement_list2))
                    )

    return result


"""
Esta implementación combina un enfoque de inicialización voraz y recocido simulado para encontrar la mejor partición 
de los estados que minimiza la distancia de Wasserstein (EMD) entre el sistema original y el sistema particionado. 
El algoritmo funciona de la siguiente manera:

1. **Inicialización Voraz**:
   - Se genera una solución inicial evaluando todas las posibles combinaciones de particiones de los estados `ns` y `cs`.
   - Para cada combinación, se calcula la distancia EMD entre el sistema original y el sistema particionado.
   - La combinación que da la menor distancia EMD se elige como la solución inicial.

2. **Recocido Simulado**:
   - A partir de la solución inicial obtenida del enfoque voraz, se exploran soluciones vecinas mediante modificaciones menores.
   - La probabilidad de aceptar una solución peor disminuye a medida que la temperatura baja con el tiempo.
   - Este enfoque ayuda a escapar de mínimos locales y encontrar una mejor solución global.

3. **Enfriamiento**:
   - La temperatura se reduce en cada iteración, lo que disminuye la probabilidad de aceptar soluciones peores y ayuda al algoritmo a converger.

El objetivo final es encontrar una partición de los estados `ns` y `cs` que minimice la distancia EMD entre el sistema original y el sistema particionado.
"""


# Función para obtener la mejor solución inicial mediante un enfoque voraz
def greedy_initial_solution(ns, cs, cs_value, probabilities, states):
    memory = {}  # Memoria para almacenar cálculos previos y evitar redundancias
    best_solution = None  # Variable para almacenar la mejor solución encontrada
    best_distance = float("inf")  # Inicializar la mejor distancia como infinito

    # Genera todas las combinaciones posibles de particiones de ns y cs
    for (ns1, cs1), (ns2, cs2) in all_combinations(ns, cs):
        # Calcula el sistema particionado para la combinación actual
        partitioned_system = np.array(
            compute_partitioned_system(
                (ns1, ns2), (cs1, cs2), cs_value, probabilities, states, memory
            )
        )
        # Calcula el sistema original completo
        original_system = np.array(
            compute_original_system(cs, cs_value, ns, probabilities, states)
        )

        # Si ambos sistemas tienen tamaño válido, calcula la distancia EMD
        if partitioned_system.size > 0 and original_system.size > 0:
            emd_distance = wasserstein_distance(original_system, partitioned_system)
            # Actualiza la mejor solución si se encuentra una con menor EMD
            if emd_distance < best_distance:
                best_distance = emd_distance
                best_solution = ((ns1, cs1), (ns2, cs2))

    return best_solution, best_distance


"""
Estrategia de Recocido Simulado con Inicialización Voraz:
Esta función combina un enfoque de inicialización voraz con recocido simulado
para mejorar la búsqueda de una solución óptima. 
El proceso es el siguiente:

1. **Inicialización Voraz**:
   - Se utiliza la función `greedy_initial_solution` para encontrar 
     una buena solución inicial evaluando todas las combinaciones posibles de particiones
     de los estados `ns` y `cs`.
   - Esta solución inicial se selecciona como la mejor combinación que minimiza 
   la distancia de Wasserstein (EMD) entre el sistema original y el sistema particionado.

2. **Recocido Simulado**:
   - Utiliza la solución inicial del enfoque voraz para iniciar el proceso de recocido simulado.
   - Genera vecinos de la solución actual modificando ligeramente `ns` y `cs`.
   - Calcula la distancia EMD para cada vecino y decide si acepta la nueva solución 
    basada en la probabilidad de aceptación, que depende de la temperatura actual.
   - Este proceso permite escapar de mínimos locales y explorar el espacio de soluciones más efectivamente.

3. **Enfriamiento**:
   - La temperatura inicial se reduce en cada iteración según la tasa de
   enfriamiento (`cooling_rate`).
   - A medida que la temperatura disminuye, la probabilidad de aceptar
   soluciones peores también disminuye, lo que ayuda al algoritmo a converger a una solución óptima.

El objetivo es encontrar la partición de los estados 
`ns` y `cs` que minimice la distancia EMD entre el sistema original y
el sistema particionado, utilizando la inicialización voraz para una mejor
 solución inicial y el recocido simulado para refinar la búsqueda.
"""


def simulated_annealing_with_greedy_initialization(
    ns,
    cs,
    cs_value,
    probabilities,
    states,
    initial_temperature=100,
    cooling_rate=0.95,
    max_iterations=1000,
):
    def neighborhood(solution, ns, cs):
        """
        Genera vecinos de la solución actual modificando ligeramente ns y cs
        """
        neighbors = []

        for i in range(len(ns)):
            for j in range(len(cs)):
                if ns[i] != solution[0] or cs[j] != solution[1]:
                    neighbors.append(((ns[i], cs[j]), solution[1]))
        return neighbors

    def acceptance_probability(old_cost, new_cost, temperature):
        """
        Acepta siempre soluciones con menor costo.
        Acepta soluciones peores con una probabilidad dependiente de la temperatura.
        """
        if new_cost < old_cost:
            return 1.0
        return np.exp((old_cost - new_cost) / temperature)

    memory = {}  # Memoria para almacenar cálculos previos y evitar redundancias
    # Inicializa con la mejor solución voraz
    current_solution, current_distance = greedy_initial_solution(
        ns, cs, cs_value, probabilities, states
    )
    best_solution = (
        current_solution  # Inicializa la mejor solución con la solución actual
    )
    best_distance = (
        current_distance  # Inicializa la mejor distancia con la distancia actual
    )
    temperature = initial_temperature  # Temperatura inicial para el recocido simulado

    # Bucle principal de recocido simulado
    for iteration in range(max_iterations):
        neighbors = neighborhood(
            current_solution, ns, cs
        )  # Genera vecinos de la solución actual
        next_solution = random.choice(
            neighbors
        )  # Selecciona aleatoriamente una solución vecina
        ns_comb, cs_comb = next_solution

        # Calcula el sistema particionado para la nueva solución
        partitioned_system = np.array(
            compute_partitioned_system(
                ns_comb, cs_comb, cs_value, probabilities, states, memory
            )
        )
        # Calcula el sistema original completo
        original_system = np.array(
            compute_original_system(cs, cs_value, ns, probabilities, states)
        )

        # Si ambos sistemas tienen tamaño válido, calcula la distancia EMD
        if partitioned_system.size > 0 and original_system.size > 0:
            emd_distance = wasserstein_distance(original_system, partitioned_system)

            # Decide si aceptar la nueva solución basándose en la probabilidad de aceptación
            if (
                acceptance_probability(current_distance, emd_distance, temperature)
                > random.random()
            ):
                current_solution = next_solution  # Actualiza la solución actual
                current_distance = emd_distance  # Actualiza la distancia actual

                # Actualiza la mejor solución encontrada si la nueva es mejor
                if emd_distance < best_distance:
                    best_solution = next_solution
                    best_distance = emd_distance

        temperature *= cooling_rate  # Enfría la temperatura

    return best_solution, best_distance


# Ejemplo de uso

probabilidades = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
]

estados = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1],
]
ns = ["A", "C"]
cs = ["A"]
cs_value = [1, 1, 1]

best_partition, min_distance = simulated_annealing_with_greedy_initialization(
    ns, cs, cs_value, probabilidades, estados
)
print(f"Mejor partición: {best_partition}, Distancia mínima: {min_distance}")
