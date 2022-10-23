from Functions import *
from Data import database
def point_A(var1, var2):
    input(f'Resultado de la variable "{var1}":')
    var1_array = randomVariableExtractor(database, var1)
    var2_array = randomVariableExtractor(database, var2)

    print(f"\nLa media de la variable es: {half(var1_array)[0]}.")
    print(f'Interpretacion: {half(var1_array)[1]}')

    input(f'Para ver el resultado de la variable: "{var2}" preiosne <<ENTER>>.')
    print(f"\nLa media de la variable es: {half(var2_array)[0]}.")
    print(f'Interpretacion: {half(var2_array)[1]}')