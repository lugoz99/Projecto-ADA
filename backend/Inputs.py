import time

start_time = time.time()

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from backend.auxiliares import repr_current_to_array, repr_next_to_array
from backend.marginalizacion import obtener_tabla_probabilidades
from backend.minimaParticion import decomposition

from backend.casospruebas import (
    probabilidades,
    estado_actual_v3,
    estado_futuro_v3,
    estado_presente_v3,
    estados,
)


# * Mirar cual es el valor de la distribucion de probabilidad original
original_system = obtener_tabla_probabilidades(
    repr_current_to_array(estado_presente_v3, estado_actual_v3),
    repr_next_to_array(estado_futuro_v3),
    probabilidades,
    estados,
)
print(f"Original System: {original_system}")
# Descomposition
print(
    decomposition(
        estado_futuro_v3, estado_presente_v3, estado_actual_v3, probabilidades, estados
    )
)
