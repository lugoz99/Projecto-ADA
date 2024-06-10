def productTensor_v4(row,col,data):
    
    if(row == 0):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]
    if(row == 1):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]
    if(row == 2):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]
    if(row == 3):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]
    if(row == 4):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]
    if(row == 5):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]
    if(row == 6):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]
    if(row == 7):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]
    if(row == 8):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]
    if(row == 9):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]
    if(row == 10):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]
    if(row == 11):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]
    if(row == 12):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]
    if(row == 13):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]
    if(row == 14):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]
    if(row == 15):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]

def getStatus_v4():
    return [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1]
    ]