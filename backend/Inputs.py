import time

start_time = time.time()

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from backend.minimaParticion import decomposition
from backend.constantes import probabilities, states


def format_partition_output(partition_result):
    # Extraer las particiones de 'ns' y 'cs' junto con la distancia de EMD
    particiones_ns, particiones_cs = partition_result[0]
    distancia_emd = partition_result[1]

    # Formatear las particiones de 'ns' y 'cs' para imprimir
    particiones_ns_formateadas = " | ".join(
        ["".join(subparticion) for subparticion in particiones_ns]
    )
    particiones_cs_formateadas = " | ".join(
        ["".join(subparticion) for subparticion in particiones_cs]
    )

    # Construir y devolver el resultado formateado
    formatted_output = {
        "Particione de ns": particiones_ns_formateadas,
        "Particione de cs": particiones_cs_formateadas,
        "Distancia de EMD": distancia_emd,
    }
    return formatted_output


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

print(
    format_partition_output(
        decomposition(
            estado_futuro_1, estado_presente_1, cs_value, probabilities, states
        )
    )
)


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
print("|--- %s Segundos ---" % (time.time() - start_time),"|")
print("|===========================================================|")