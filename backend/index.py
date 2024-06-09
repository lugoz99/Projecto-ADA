import time

start_time = time.time()

import sys
import os

import streamlit as st
import pandas as pd
from io import StringIO


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from backend.generator.probabilities import generatorProbabilities
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

# Valor del estado actual del sistema
cs_value = [1, 0, 0, 0, 1]

st.title('Próyecto Final')
st.subheader('Análisis Y Diseño De Algoritmo')


st.divider()

data = st.file_uploader("Elige un Archivo")

if data is not None:

    st.write(pd.read_json(data))

    # To convert to a string based IO:
    dataJson = StringIO(data.getvalue().decode("utf-8"))

    searchStatus, result_matrix = generatorProbabilities(dataJson.read())

    #st.table(searchStatus)
    st.table(result_matrix)

#print(
#    format_partition_output(
#        decomposition(
#            estado_futuro_1, estado_presente_1, cs_value, probabilities, states
#        )
#    )
#)

print("\n\n|===========================================================|")
print("|--- %s Segundos ---" % (time.time() - start_time),"|")
print("|===========================================================|")