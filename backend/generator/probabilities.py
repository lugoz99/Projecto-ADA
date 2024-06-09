import json

def generatorProbabilities(data):

    def createTableGeneral(dataRaw):

        data = json.loads(dataRaw)

        num_cols = len(data["primogenitalTables"]["A"][0])

        # Inicializar una matriz para almacenar los resultados de la multiplicación
        result_matrix = [[-1] * num_cols for _ in range(num_cols)]

        for col in range(num_cols):
            for row in range(num_cols):
                result_matrix[col][row] = productTensor(row,col,data["primogenitalTables"]);

        # Imprimir la matriz resultante
        # print("Matriz resultante:")
        #for row in result_matrix:
            #print(row)

        #Buscar el estado especifico
        status = searchStatus(data,result_matrix)

        return status, result_matrix


    def productTensor(row,col,data):
        
        if(row == 0):
            return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]
        if(row == 1):
            return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]
        if(row == 2):
            return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]
        if(row == 3):
            return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]
        if(row == 4):
            return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]
        if(row == 5):
            return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]
        if(row == 6):
            return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]
        if(row == 7):
            return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]
        
    def searchStatus(data, result_matrix):

        statusPosition = int(str(data["stateSought"])[::-1],2);
        return result_matrix[statusPosition]


    return createTableGeneral(data)