import time

import os
import sys
import json

import streamlit as st
import pandas as pd
from io import StringIO


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from backend.generator.probabilities import generatorProbabilities
from backend.minimaParticion import decomposition


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

    print("\n\n|===========================================================|")
    print("|--- %s Segundos ---" % (time.time() - start_time),"|")
    print("|===========================================================|")

    return formatted_output


st.title('Próyecto Final')
st.subheader('Análisis Y Diseño De Algoritmo')

st.divider()

data = st.file_uploader("Elige un Archivo")

if data is not None:

    st.header('Contenido del Documento')
    st.write(pd.read_json(data))

    # To convert to a string based IO:
    dataJson = json.loads(StringIO(data.getvalue().decode("utf-8")).read())

    searchStatus, result_matrix, states = generatorProbabilities(dataJson)

    st.header('Tabla de Probabilidad')
    st.table(result_matrix)

    st.text('Estado Buscado')
    st.text(dataJson["stateSought"])

    st.text('Valor Encontrado')
    st.text(searchStatus)

    st.divider()
    st.title("Procesar Datos")

    st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec dignissim nulla. Proin porta nulla eros, ac posuere nisi molestie et. Nulla dapibus pellentesque enim, at elementum nulla mollis ut. Nunc convallis ultricies augue faucibus sagittis. Mauris hendrerit lorem a nunc porta dignissim. Sed vehicula.")

    
    st.write("Complete todos los campos")
        
    currentStatus = st.text_input("Estado Presente", "ABC")
    nextStatus = st.text_input("Estado Futuro", "ABC")
        
    # Every form must have a submit button.
    submitted = st.button("Submit")

    st.divider()
    st.title("Resultado Procesamiento de Datos")

    if submitted:

        start_time = time.time()
        st.text(
            format_partition_output(
                decomposition(
                    nextStatus, currentStatus, dataJson["stateSought"], result_matrix, states, st
                )
            )
        )

        with st.spinner('Procesando Datos...'):
            time.sleep(30)
        st.success('Done!')
