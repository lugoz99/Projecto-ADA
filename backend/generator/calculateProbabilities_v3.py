def productTensor_v3(row,col,data):
        
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

def getStatus_v3():
    return [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1]
]