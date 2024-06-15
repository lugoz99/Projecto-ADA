import time

start_time = time.time()

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from backend.auxiliares import repr_current_to_array, repr_next_to_array
from backend.marginalizacion import obtener_tabla_probabilidades, verificar_vacio

from backend.minimaParticion import decomposition
from backend.constantes import (
    probabilities,
    states,
    probabilidades,
    estados,
    estado_presente_v3,
    estado_futuro_v3,
    estado_actual_v3,
)


estado_futuro_1 = "ABCD"
estado_presente_1 = "ABCD"
estado_futuro_2 = "ABCD"
estado_presente_2 = "ABCDE"
estado_futuro_3 = "ABCDE"
estado_presente_3 = "ABCD"
estado_futuro_4 = "ABC"
estado_presente_4 = "ABCDE"
estado_futuro_5 = "ABCDE"
estado_presente_5 = "AB"
estado_futuro_6 = "ACD"
estado_presente_6 = "ACD"
estado_futuro_7 = "ABC"
estado_presente_7 = "ABC"
estado_futuro_8 = "ABCE"
estado_presente_8 = "ABE"
estado_futuro_9 = "BC"
estado_presente_9 = "ABC"
estado_futuro_10 = "BC"
estado_presente_10 = "C"
estado_futuro_11 = "ABC"
estado_presente_11 = "AC"


# Valor del estado actual del sistema
cs_value = [1, 0, 0, 0, 1]


# original_system = obtener_tabla_probabilidades(
#     repr_current_to_array("C", [0]),
#     repr_next_to_array("BC"),
#     probabilities,
#     states,
# )
print(verificar_vacio("", "BC"))
print(decomposition("C", "", [0], probabilidades, estados))
# print(decomposition("C", "", [1], probabilidades, estados))

# print(
#     decomposition(
#         estado_futuro_v3, estado_presente_v3, estado_actual_v3, probabilidades, estados
#     )
# )

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


print("\n\n|===========================================================|")
print("|--- %s Segundos ---" % (time.time() - start_time), "|")
print("|===========================================================|")
