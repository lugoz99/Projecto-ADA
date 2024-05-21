import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from backend.minimaParticion import min_particion

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

"""" 
se presenta la matriz que representa  las probabilidades de pasar de un estado actual a uno próximo:

"""

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


estado_futuro = "ABC"
estado_presente = "AC"
estado_actual = [1, 0]

# estado_futuro = "AC"
# estado_presente = "ABC"
# estado_actual = [1, 0, 0]
# obtener_sistema_original(
#     estado_futuro, estado_presente, estado_actual, probabilidades, estados
# )


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


print(
    format_partition_output(
        min_particion(
            estado_futuro, estado_presente, estado_actual, probabilidades, estados
        )
    )
)
