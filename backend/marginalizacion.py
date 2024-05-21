# - Utilizar la matriz de probabilidades para calcular la distribución de probabilidades
#     sistema en el estado inicial.
# - Aplicar marginalización en el futuro y en el tiempo actual para obtener el cálculo
# de la Distribución Original.

import numpy as np


def getIndicesMarginalizar(states, state):
    """
    The function `getIndicesMarginalizar` takes a list of states and a specific state, and returns a
    dictionary of indices based on the available values in the state along with a computed value.

    :param states: A list of lists representing different states. Each inner list contains values for
    different variables in the state
    :param state: The `state` parameter in the `getIndicesMarginalizar` function is a list representing
    the state of a system. Each element in the list corresponds to a variable in the system. If the
    value of a variable is known, it is represented by that value (e.g., 0 or
    :return: The function `getIndicesMarginalizar` returns a tuple containing two values:
    1. `indices`: a dictionary where keys are tuples of values from the specified indices in the states
    list, and values are lists of indices corresponding to those keys.
    2. `csValue`: an integer value obtained by converting the binary representation of the non-None
    elements in the state list to an integer.
    """
    availableIndices = []
    indices = {}
    csValue = ""
    for i in range(len(state)):
        if state[i] != None:
            availableIndices.append(i)
            csValue = str(state[i]) + csValue

    for i in range(len(states)):
        key = tuple(states[i][j] for j in availableIndices)

        indices[key] = indices.get(key) + [i] if indices.get(key) else [i]

    if csValue == "":
        return indices, 0

    return indices, int(csValue, 2)


def margenaliceNextState(nsIndices, probabilites):
    """
    The function `margenaliceNextState` calculates the transition probabilities for each state in a
    Markov chain based on given indices and probabilities.

    """
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
                csValue = csTransitionTable[csValueIndex]

                if len(result) > 0:
                    result = np.kron(result, csValue)
                else:
                    result = csValue
    else:
        nsIndices, _ = getIndicesMarginalizar(states, nextState)
        nsTransitionTable = margenaliceNextState(nsIndices, probabilities)

        csTransitionTable = margenaliceCurrentState(csIndices, nsTransitionTable)
        result = csTransitionTable[csValueIndex]

    return result
