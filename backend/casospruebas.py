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

estado_futuro_v3 = "ABC"
estado_presente_v3 = "ABC"
estado_actual_v3 = [1, 0, 0]


# *******GENERALES*****************
casos_de_prueba = [
    ("ABCD", "ABCD"),
    ("ABCD", "ABCDE"),
    ("ABCDE", "ABCD"),
    ("ABC", "ABCDE"),
    ("ABCDE", "AB"),
    ("ACD", "ACD"),
    ("ABC", "ABC"),
    ("ABCE", "ABE"),
    ("BC", "ABC"),
    ("BC", "C"),
    ("ABC", "AC"),
]
