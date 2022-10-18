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
    halfResult = round(sum/len(randomVariableArray), 4)
    return halfResult, f'La conclusión para la media aritmetica que obtuvimos es que el promedio\n' \
                                                   f'de nuestra variable tomada fue: {halfResult}'

def medium(randomVariableArray):
    mediumIndex = math.ceil(len(randomVariableArray)/2)
    mediumValue = randomVariableArray[mediumIndex-1]
    return mediumValue, mediumIndex, f'Nuestro punto medio de datos se encuentra en el indice: {mediumIndex} y toma el valor de: {mediumValue}.'
def standardDevitation(randomVariableArray):
    calculatedHalf = half(randomVariableArray)
    sumOfDistance = 0
    for i in randomVariableArray:
        sumOfDistance += (i - calculatedHalf[0])**2
    return round(math.sqrt(sumOfDistance/len(randomVariableArray)), 4)\
        ,'La desviacion estandar es la que nos muestra la dispercion entre nuestros datos, a mayor el numero presentado, mayor dispercion entre los datos tendremos...\n' \
         f'por lo tanto nuestra desviacion estandar presenta un valor de: {round(math.sqrt(sumOfDistance/len(randomVariableArray)), 4)}, Sí fuese 0 indicaria que no hay\n' \
         f'ninguna disperción.'

#arrayOfVariable = randomVariableExtractor(database, "lastSemesterAvg")
arrayOfVariable = [1, 2.45, 4.5, 5]
print(arrayOfVariable)

print(f"\nLa media de la variable es: {half(arrayOfVariable)[0]}.")
print(half(arrayOfVariable)[1])

print(f'\nLa mediana se encuentra en el indice: {medium(arrayOfVariable)[1]} y su valor es: {medium(arrayOfVariable)[0]}.')
print(medium(arrayOfVariable)[2])

print(f'\nDesviacion estandar: {standardDevitation(arrayOfVariable)[0]}')
print(standardDevitation(arrayOfVariable)[1])