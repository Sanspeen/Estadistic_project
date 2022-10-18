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
    return round(sum/len(randomVariableArray), 4)

def medium(randomVariableArray):
    mediumIndex = math.ceil(len(randomVariableArray)/2)
    mediumValue = randomVariableArray[mediumIndex-1]
    return mediumValue, mediumIndex
def standardDevitation(randomVariableArray):
    calculatedHalf = half(randomVariableArray)
    sumOfDistance = 0
    for i in randomVariableArray:
        sumOfDistance += (i - calculatedHalf)**2
    return round(math.sqrt(sumOfDistance/len(randomVariableArray)), 4)

#arrayOfVariable = randomVariableExtractor(database, "lastSemesterAvg")
arrayOfVariable = [1, 2.45, 4.5, 5]
print(arrayOfVariable)

print(f"\nLa media de la variable es: {half(arrayOfVariable)}")

print(f'\nLa mediana se encuentra en el indice: {medium(arrayOfVariable)[1]} y su valor es: {medium(arrayOfVariable)[0]}')

print(f'\nDesviacion estandar: {standardDevitation(arrayOfVariable)}')