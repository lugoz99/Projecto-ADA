import json

import numpy as np
import pandas as pd
from io import StringIO
import streamlit as st

st.title("Descomponer Tabla de Probabilidad")

# Función para obtener el estado de las variables
def get_states(index):
    binary_rep = format(index, '04b')
    return [int(bit) for bit in binary_rep]

# Crear una tabla de estados presente y futuro
def create_state_tables(prob_table):
    state_present = []
    state_future = []
    
    for i in range(len(prob_table)):
        for j in range(len(prob_table[i])):
            if prob_table[i][j] == 1:
                present_state = get_states(i)
                future_state = get_states(j)
                state_present.append(present_state)
                state_future.append(future_state)
    
    return np.array(state_present), np.array(state_future)


data = st.file_uploader("Elige un Archivo para descomponer")

if data is not None:

    st.header('Contenido del Documento')
    st.write(pd.read_json(data))

    # To convert to a string based IO:
    dataJson = json.loads(StringIO(data.getvalue().decode("utf-8")).read())

    # Tabla de probabilidad dada (valores modificados para que sean interpretados como flotantes)
    prob_table = np.array(dataJson["tableProbabilities"])

    # Convertir las probabilidades distintas de cero a 1
    prob_table[prob_table != 0] = 1

    st.header('Tabla de Probabilidad convertida a binario')
    st.write(prob_table)    

    state_present, state_future = create_state_tables(prob_table)

    # Crear la tabla de estados
    states_table = np.array([get_states(i) for i in range(len(prob_table[0]))])

    # Imprimir la tabla de estados
    st.subheader("Tabla de estados:")
    st.table(states_table)

    # Imprimir las tablas de estados presente y futuro
    st.write("Estado Presente:")
    st.write(state_present)

    st.write("Estado Futuro:")
    st.write(state_future)
