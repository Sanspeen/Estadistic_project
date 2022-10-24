import os
from Functions import *
from Data import database


def point_a(var1, var2):
    os.system('cls')
    print(f'Resultado de la variable "{var1}":')
    var1_array = random_variable_extractor(database, var1)
    var2_array = random_variable_extractor(database, var2)

    print(f'Datos utilizados:{var2_array}\n')
    print(f"\nLa media de la variable es: {half(var1_array)[0]}.")
    print(f'Interpretacion: {half(var1_array)[1]}')

    print(f'\nLa mediana se encuentra en el indice: {medium(var1_array)[1]} y su valor es: {medium(var1_array)[0]}.')
    print(medium(var1_array)[2])

    print(f'\nDesviacion estandar: {standard_devitation(var1_array)[0]}')
    print(standard_devitation(var1_array)[1])

    input(f'\nPara ver el resultado de la variable: "{var2}" presione <<ENTER>>.')

    os.system('cls')
    print(f'Datos utilizados:{var2_array}\n')
    print(f"\nLa media de la variable es: {half(var2_array)[0]}.")
    print(f'Interpretacion: {half(var2_array)[1]}')

    print(f'\nLa mediana se encuentra en el indice: {medium(var2_array)[1]} y su valor es: {medium(var2_array)[0]}.')
    print(medium(var2_array)[2])

    print(f'\nDesviacion estandar: {standard_devitation(var2_array)[0]}')
    print(standard_devitation(var2_array)[1])


def point_b(data_base):
    print("Solucion indice b, punto 1.\n")
    is_working_users, not_working_users = is_working_separator(data_base)
    is_working_time = random_variable_extractor(is_working_users, 'timeBackingHouse')
    not_working_time = random_variable_extractor(not_working_users, 'timeBackingHouse')

    print(f"\nLa media del tiempo para los que trabajan es: {half(is_working_time)[0]}.")
    print(f"La media del tiempo para los que NO trabajan es: {half(not_working_time)[0]}.\n")

    print(f'\nLa mediana de los que trabajan se encuentra en el indice: {medium(is_working_time)[1]}'
          f' y su valor es: {medium(is_working_time)[0]}.')
    print(f'La mediana de los que NO trabajan se encuentra en el indice: {medium(not_working_time)[1]}'
          f' y su valor es: {medium(not_working_time)[0]}.')

    print(f'\nDesviacion estandar de los que trabajan: {standard_devitation(is_working_time)[0]}')
    print(f'Desviacion estandar de los que NO trabajan: {standard_devitation(not_working_time)[0]}')

    print('\nConclusiones:')
    print(f'De nuestra media podremos concluir que las personas que no trabajan se tardan menos en regresar a su casa '
          f'en comparacion con los que si trabajan.')
    print(f'De nuestra mediana podremos obtener que de nuestra muestra que tiene {len(data_base)} datos tenemos'
          f' que son mas las personas de nuestra muestra que trabajan que las que NO trabajan.')
    print(f'Por ultimo podemos evidenciar una mayor dispersión de datos de cuenta de nuestros usuarios que trabajan'
          f' que los que no trabajan.')
