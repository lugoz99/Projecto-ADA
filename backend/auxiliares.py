"""Extiende la matriz de probabilidades
original para que todas las filas tengan la misma longitud que el número de estados posibles"""


def build_probabilities(probabilities, len_cs):

    extended_probabilities = [None] * len(probabilities)
    for i in range(len(probabilities)):
        extended_probabilities[i] = probabilities[i] + [0] * (
            len_cs - len(probabilities[i])
        )

    return extended_probabilities


def repr_next_to_array(letras):
    ns_arr = [0] * len(letras)
    return ns_arr


def repr_current_to_array(cs, cs_value):
    # Crear un diccionario que mapee las letras en cs a sus correspondientes valores en cs_value
    cs_dict = {
        cs[i]: cs_value[i] if i < len(cs_value) else None for i in range(len(cs))
    }
    # Crear un nuevo arreglo con None en las posiciones que no están especificadas por cs
    # TODO : Generalizar esto afecta
    cs_arr = [cs_dict.get(c) for c in "ABCDE"]
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
