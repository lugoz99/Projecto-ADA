def productTensor_v6(row,col,data):
    
    if(row == 0):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 1):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 2):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 3):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 4):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 5):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 6):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 7):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 8):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 9):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 10):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 11):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 12):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 13):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 14):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 15):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]
    if(row == 16):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 17):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 18):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 19):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 20):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 21):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 22):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 23):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 24):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 25):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 26):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 27):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 28):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 29):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 30):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]
    if(row == 31):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]
    
    if(row == 32):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 33):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 34):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 35):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 36):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 37):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 38):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 39):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 40):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 41):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 42):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 43):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 44):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 45):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 46):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 47):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]
    if(row == 48):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 49):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 50):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 51):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 52):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 53):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 54):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 55):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 56):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 57):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 58):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 59):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 60):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 61):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 62):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]
    if(row == 63):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]

def getStatus_v6():
    return [
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [1, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [0, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]