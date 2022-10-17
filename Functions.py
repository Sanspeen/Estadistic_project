from Data import database

def randomVariableExtractor(database, nameOfVariable):
    extractedVariableArray = []
    for i in range(0, len(database)):
        extractedVariableArray.append(database[i].get(nameOfVariable))
    return extractedVariableArray

def half(randomVariableArray):
    sum = 0
    for i in range(0, len(randomVariableArray)):
        sum += randomVariableArray[i]
    print(f"La media de la variable es: {round(sum/len(randomVariableArray), 4)}")

arrayOfVariable = randomVariableExtractor(database, "lastSemesterAvg")
half(arrayOfVariable)