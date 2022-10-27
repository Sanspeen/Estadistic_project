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

    print(f'\nDesviacion estandar: {standard_deviation(var1_array)[0]}')
    print(standard_deviation(var1_array)[1])

    input(f'\nPara ver el resultado de la variable: "{var2}" presione <<ENTER>>.')

    os.system('cls')
    print(f'Datos utilizados:{var2_array}\n')
    print(f"\nLa media de la variable es: {half(var2_array)[0]}.")
    print(f'Interpretacion: {half(var2_array)[1]}')

    print(f'\nLa mediana se encuentra en el indice: {medium(var2_array)[1]} y su valor es: {medium(var2_array)[0]}.')
    print(medium(var2_array)[2])

    print(f'\nDesviacion estandar: {standard_deviation(var2_array)[0]}')
    print(standard_deviation(var2_array)[1])


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

    print(f'\nDesviacion estandar de los que trabajan: {standard_deviation(is_working_time)[0]}')
    print(f'Desviacion estandar de los que NO trabajan: {standard_deviation(not_working_time)[0]}')

    print('\nConclusiones:')
    print(f'De nuestra media podremos concluir que las personas que no trabajan se tardan menos en regresar a su casa '
          f'en comparacion con los que si trabajan.')
    print(f'De nuestra mediana podremos obtener que de nuestra muestra que tiene {len(data_base)} datos tenemos'
          f' que son mas las personas de nuestra muestra que trabajan que las que NO trabajan.')
    print(f'Por ultimo podemos evidenciar una mayor dispersión de datos de cuenta de nuestros usuarios que trabajan'
          f' que los que no trabajan.')


def point_c(data_base):
    print('Tabla de frecuencias para Estrato:')
    print(f'{generate_frequency_table(data_base, "stratum")[0]}\n'
          f'n: {generate_frequency_table(data_base, "stratum")[1]}\n')
    print('Intervalos:')
    for i in range(0, len(generate_frequency_table(data_base, "stratum")[2][0])):
        print(f'{i+1} = ({generate_frequency_table(data_base, "stratum")[2][1][i]}) '
              f'- ({generate_frequency_table(data_base, "stratum")[2][0][i]})')
    print('Al realizar los intervalos nos damos cuenta que a partir de MU +- 2Sigma los datos pertenecen al\n'
          'teorema empirico.')
    print('')
    print('Tabla de frecuencias para TRAB:')
    print(f'{generate_frequency_table(data_base, "isWorking")[0]}\n'
          f'n: {generate_frequency_table(data_base, "isWorking")[1]}\n')
    print('Intervalos:')
    for i in range(0, len(generate_frequency_table(data_base, "isWorking")[2][0])):
        print(f'{i+1} = ({generate_frequency_table(data_base, "isWorking")[2][1][i]}) '
              f'- ({generate_frequency_table(data_base, "isWorking")[2][0][i]})')

    print('Primero que nada para este caso podremos concluir que la libreria por debajo transforma los valores de\n'
          'Verdadero y Falso a 1 y 0 respectivamente de manera que nos entrega unos limites algo peculiares\n'
          'Arrojando margenes de error bastante altos, llegando margenes de error casi del 300%.')


def point_d():
    print(f'La cantidad de personas que trabajan dentro'
          f' de nuestra base de datos es: {len(filter_by_variable_bool(database, "isWorking"))}')
    print(f'La cantidad de datos totales de nuestra base es n = {len(database)}\n')
    print(f'Entonces tenemos que la probabilidad de que tomando una persona al azar esta trabaje'
          f' es del: %{probability_of_one(len(filter_by_variable_bool(database, "isWorking")), len(database))*100}')


def point_e():
    print(f'La cantidad de personas que pertenecen al estrato 4'
          f' de nuestra base de datos es: {len(filter_by_punctual_value(database, "stratum", 4))}')
    print(f'La cantidad de datos totales de nuestra base es n = {len(database)}\n')
    print(f'Entonces tenemos que la probabilidad de que tomando una persona al azar esta pertenezca al estrato 4.'
          f' es del: %{probability_of_one(len(filter_by_punctual_value(database, "stratum", 4)), len(database)) * 100}')


def point_f():
    filtered_by_is_not_working = filter_by_variable_bool(database, "isWorking")[1]
    filtered_by_stratum = []
    for i in filtered_by_is_not_working:
        if i.get('stratum') == 5:
            filtered_by_stratum.append(i)

    print(len(filtered_by_is_not_working))
    if len(filtered_by_stratum) == 0:
        print('No existe ningúna persona de estrato 5 en la base de datos.')
    else:
        print(f'La cantidad de personas que no trabajan y que pertenecen al estrato 5'
              f' de nuestra base de datos son: {len(filtered_by_stratum)}')
        print(f'La cantidad de datos totales de nuestra base es n = {len(database)}\n')
        print(f'Entonces tenemos que la probabilidad de que tomando una persona al azar esta no trabaje'
              f' y que pertenezca al estrato 5.'
              f' es del: %{round(probability_of_one(len(filtered_by_stratum), len(database)) * 100, 2)}')


def point_g():
    filtered_by_is_not_working = filter_by_variable_bool(database, "isWorking")[1]
    filtered_by_stratum = []
    for i in filtered_by_is_not_working:
        if i.get('stratum') == 5:
            filtered_by_stratum.append(i)

    print(f'La cantidad de personas que si no trabajan, pertenezcan al estrato 5'
          f' de nuestra base de datos son: {len(filtered_by_stratum)}')
    print(f'La cantidad de datos totales de nuestra base es n = {len(filtered_by_is_not_working)}\n')
    print(f'Entonces tenemos que la probabilidad de que si una persona no trabaja, esta pertenezca al estrato 5'
          f' es del: %{round(probability_of_one(len(filtered_by_stratum), len(filtered_by_is_not_working)) * 100, 2)}')


def point_h():
    print(f'Para la solución de este punto tengo dos posibles respuestas:\n'
          f"\033[;36m"+'Respuesta 1:'+"\033[0;m"+'Teniendo en cuenta que nuestra base de datos fue poblada con datos completamente aleatorios\n'
          f'con unos limites definidos podriamos recalcar que nuestras variables son completamente independientes\n'
          f' puesto a que ninguna de las dos cambia la manera en la que se comporta la otra\n')
    print("\033[;36m"+'Respuesta 2:'+"\033[0;m"+'Teniendo en cuenta que el planteamiento incial se concentra en un contexto dentro de nuestra\n'
          'universidad yo podria determinar que estas variables no son dependientes la una de las otras porque no hay\n'
          'ningun determinante para que tu estrato socieconomico determine tu edad o viceversa.')