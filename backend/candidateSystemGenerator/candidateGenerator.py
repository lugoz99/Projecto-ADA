import numpy as np

def indexCandidateSystem(probabilities, candidateSystem, st):

    size=9

    """
    Obtiene una submatriz de las primeras `size` filas y columnas de la matriz original.
    
    :param matrix: numpy array, matriz original de tamaño n x n.
    :param size: int, el tamaño de la submatriz deseada (por defecto es 9).
    :return: numpy array, submatriz de tamaño `size` x `size`.
    """

    probabilities_result = np.array(probabilities)

    return probabilities_result[:size, :size]