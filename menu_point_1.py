import os

from Functions import *
from Data import database
def point_A(var1, var2):
    os.system('cls')
    print(f'Resultado de la variable "{var1}":')
    var1_array = randomVariableExtractor(database, var1)
    var2_array = randomVariableExtractor(database, var2)

    print(f'Datos utilizados:{var2_array}\n')
    print(f"\nLa media de la variable es: {half(var1_array)[0]}.")
    print(f'Interpretacion: {half(var1_array)[1]}')

    print(f'\nLa mediana se encuentra en el indice: {medium(var1_array)[1]} y su valor es: {medium(var1_array)[0]}.')
    print(medium(var1_array)[2])

    print(f'\nDesviacion estandar: {standardDevitation(var1_array)[0]}')
    print(standardDevitation(var1_array)[1])

    input(f'\nPara ver el resultado de la variable: "{var2}" presione <<ENTER>>.')

    os.system('cls')
    print(f'Datos utilizados:{var2_array}\n')
    print(f"\nLa media de la variable es: {half(var2_array)[0]}.")
    print(f'Interpretacion: {half(var2_array)[1]}')

    print(f'\nLa mediana se encuentra en el indice: {medium(var2_array)[1]} y su valor es: {medium(var2_array)[0]}.')
    print(medium(var2_array)[2])

    print(f'\nDesviacion estandar: {standardDevitation(var2_array)[0]}')
    print(standardDevitation(var2_array)[1])