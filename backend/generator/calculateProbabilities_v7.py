def productTensor_v7(row,col,data):
    
    if(row == 0):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 1):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 2):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 3):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 4):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 5):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 6):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 7):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 8):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 9):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 10):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 11):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 12):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 13):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 14):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 15):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 16):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 17):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 18):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 19):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 20):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 21):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 22):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 23):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 24):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 25):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 26):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 27):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 28):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 29):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 30):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    if(row == 31):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][0][col]
    
    if(row == 32):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 33):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 34):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 35):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 36):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 37):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 38):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 39):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 40):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 41):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 42):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 43):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 44):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 45):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 46):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 47):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 48):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 49):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 50):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 51):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 52):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 53):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 54):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 55):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 56):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 57):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 58):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 59):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 60):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 61):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 62):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    if(row == 63):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][0][col]
    
    if(row == 64):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 65):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 66):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 67):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 68):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 69):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 70):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 71):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 72):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 73):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 74):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 75):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 76):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 77):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 78):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 79):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 80):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 81):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 82):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 83):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 84):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 85):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 86):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 87):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 88):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 89):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 90):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 91):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 92):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 93):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 94):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    if(row == 95):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][0][col]*data["G"][1][col]
    
    if(row == 96):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 97):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 98):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 99):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 100):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 101):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 102):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 103):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 104):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 105):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 106):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 107):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 108):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 109):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 110):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 111):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][0][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 112):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 113):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 114):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 115):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 116):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 117):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 118):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 119):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][0][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 120):
        return data["A"][0][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 121):
        return data["A"][1][col] * data["B"][0][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 122):
        return data["A"][0][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 123):
        return data["A"][1][col] * data["B"][1][col] * data["C"][0][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 124):
        return data["A"][0][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 125):
        return data["A"][1][col] * data["B"][0][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 126):
        return data["A"][0][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]
    if(row == 127):
        return data["A"][1][col] * data["B"][1][col] * data["C"][1][col]*data["D"][1][col]*data["E"][1][col]*data["F"][1][col]*data["G"][1][col]

def getStatus_v7():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [1, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [1, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0]

        [0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]