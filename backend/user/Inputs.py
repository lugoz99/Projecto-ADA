import numpy as np
import pandas as pd
from math import log2, ceil


def logbase2(num):
    return ceil(log2(num))


def formatoFila(filas):
    num_bits = logbase2(filas)
    estados = ["{0:0{1}b}".format(i, num_bits) for i in range(2**num_bits)]
    estados = [
        estado[::-1] for estado in estados
    ]  # Invertir los estados para que coincidan con el patrón binario
    return estados


def formatoColumna(columnas):
    num_bits = logbase2(columnas)
    estados = ["{0:0{1}b}".format(i, num_bits) for i in range(2**num_bits)]
    estados = [
        estado[::-1] for estado in estados
    ]  # Invertir los estados para que coincidan con el patrón binario
    return estados


def ingresar_filas(matriz):

    canales = [chr(65 + i) for i in range(logbase2(matriz.shape[0]))]
    filas = []
    global flag
    if logbase2(matriz.shape[0]) == 0:
        flag = True
        for i in range(3):
            canales = [chr(65 + i) for i in range(3)]
            fila = str(
                input(
                    f"Ingrese un valor binario para la fila {canales[i]} (0 o 1) enter para no ingresar nada: "
                )
            )
            filas.append(fila)
    else:
        for i in range(logbase2(matriz.shape[0])):
            fila = str(
                input(
                    f"Ingrese un valor binario para la fila {canales[i]} (0 o 1) si no ingresa nada esta fila se marginalizara: "
                )
            )
            filas.append(fila)

    return filas


# Se ingresa los valores binarios de las columnas(estado futuro)
def ingresar_columnas(matriz):
    canales2 = [chr(65 + i) for i in range(logbase2(matriz.shape[1]))]
    columnas = []
    for i in range(logbase2(matriz.shape[1])):
        columna = str(
            input(
                f"Quiere saber la probabilidad del valor futuro de la columna {canales2[i]}?, ingrese s o n (s=si o n=no) si ingresa 'n' se marginalizara esta columna: "
            )
        )
        columnas.append(columna)
    return columnas


# Se ingresa los valores binarios de la matriz
def ingresar_matriz():
    matriz = []
    print(
        "Ingresa los datos de la matriz, separados por espacios(cuando haya acabado presione 2 veces enter):"
    )
    while True:
        fila = input()
        if fila == "":
            break
        matriz.append(list(map(float, fila.replace("\t", " ").split())))
    matriz = np.array(matriz)
    return matriz


"""
1 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 1 0 0
0 1 0 0 0 0 0 0
0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 1 0 0
0 0 0 1 0 0 0 0
"""
""""
1	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0
0	0	0	0	0	1	0	0
0	1	0	0	0	0	0	0
0	1	0	0	0	0	0	0
0	0	0	0	0	0	0	1
0	0	0	0	0	1	0	0
0	0	0	1	0	0	0	0







"""
