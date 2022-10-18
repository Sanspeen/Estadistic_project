import math
from Data import database

def randomVariableExtractor(database, nameOfVariable):
    extractedVariableArray = []
    for i in range(0, len(database)):
        extractedVariableArray.append(database[i].get(nameOfVariable))
    extractedVariableArray.sort()
    return extractedVariableArray

def half(randomVariableArray):
    sum = 0
    for i in range(0, len(randomVariableArray)):
        sum += randomVariableArray[i]
    print(f"\nLa media de la variable es: {round(sum/len(randomVariableArray), 4)}")

def medium(randomVariableArray):
    mediumIndex = math.ceil(len(randomVariableArray)/2)
    mediumValue = randomVariableArray[mediumIndex-1]
    print(f'\nLa mediana se encuentra en el indice: {mediumIndex} y su valor es: {mediumValue}')

arrayOfVariable = randomVariableExtractor(database, "lastSemesterAvg")
print(arrayOfVariable)

half(arrayOfVariable)

medium(arrayOfVariable)

