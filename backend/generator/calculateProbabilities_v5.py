def productTensor_v5(row,col,data):
    
    if(row == 0):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]
    if(row == 1):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]
    if(row == 2):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]
    if(row == 3):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]
    if(row == 4):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]
    if(row == 5):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]
    if(row == 6):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]
    if(row == 7):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]
    if(row == 8):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]
    if(row == 9):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]
    if(row == 10):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]
    if(row == 11):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]
    if(row == 12):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]
    if(row == 13):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]
    if(row == 14):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]
    if(row == 15):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]
    if(row == 16):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]
    if(row == 17):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]
    if(row == 18):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]
    if(row == 19):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]
    if(row == 20):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]
    if(row == 21):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]
    if(row == 22):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]
    if(row == 23):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]
    if(row == 24):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]
    if(row == 25):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]
    if(row == 26):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]
    if(row == 27):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]
    if(row == 28):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]
    if(row == 29):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]
    if(row == 30):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]
    if(row == 31):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]

def getStatus_v5():
    return [
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 1, 1],
        [1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]