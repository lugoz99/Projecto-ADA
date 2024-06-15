import json

from generator.calculateProbabilities_v3 import productTensor_v3, getStatus_v3
from generator.calculateProbabilities_v4 import productTensor_v4, getStatus_v4
from generator.calculateProbabilities_v5 import productTensor_v5, getStatus_v5
from generator.calculateProbabilities_v6 import productTensor_v6, getStatus_v6


def generatorProbabilities(data):

    def createTableGeneral(data):

        num_cols = len(data["primogenitalTables"]["A"][0])
        status = []

        # Inicializar una matriz para almacenar los resultados de la multiplicación
        result_matrix = [[-1] * num_cols for _ in range(num_cols)]

        for col in range(num_cols):
            for row in range(num_cols):

                if(len(data["primogenitalTables"].keys()) == 3):
                    result_matrix[col][row] = productTensor_v3(row,col,data["primogenitalTables"]);
                if(len(data["primogenitalTables"].keys()) == 4):
                    result_matrix[col][row] = productTensor_v4(row,col,data["primogenitalTables"]);
                if(len(data["primogenitalTables"].keys()) == 5):
                    result_matrix[col][row] = productTensor_v5(row,col,data["primogenitalTables"]);
                if(len(data["primogenitalTables"].keys()) == 6):
                    result_matrix[col][row] = productTensor_v6(row,col,data["primogenitalTables"]);
                

        # Imprimir la matriz resultante
        # print("Matriz resultante:")
        #for row in result_matrix:
            #print(row)

        #Buscar el estado especifico
        valueStatus = searchStatus(data,result_matrix)

        if(len(data["primogenitalTables"].keys()) == 3):
            status = getStatus_v3()
        if(len(data["primogenitalTables"].keys()) == 4):
            status = getStatus_v4()
        if(len(data["primogenitalTables"].keys()) == 5):
            status = getStatus_v5()
        if(len(data["primogenitalTables"].keys()) == 6):
            status = getStatus_v6()

        return valueStatus, result_matrix, status
        
    def searchStatus(data, result_matrix):

        statusPosition = int(str(data["stateSought"])[::-1],2);
        return result_matrix[statusPosition]


    return createTableGeneral(data)