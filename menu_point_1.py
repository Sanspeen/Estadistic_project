import os
from Functions import *
from Data import data_base


def point_a(var1, var2, var1_users, var2_users):
    os.system('cls')
    print(f'Resultado de la variable "{var1_users}":')
    var1_array = random_variable_extractor(data_base, var1)
    var2_array = random_variable_extractor(data_base, var2)

    print(f'Datos utilizados:{var1_array}\n')
    print(f"\nLa media de la variable es: {half(var1_array)[0]}.")
    print(f'Interpretacion: {half(var1_array)[1]}')

    print(f'\nLa mediana se encuentra en el indice: {medium(var1_array)[1]} y su valor es: {medium(var1_array)[0]}.')
    print(medium(var1_array)[2])

    print(f'\nDesviacion estandar: {standard_deviation(var1_array)[0]}')
    print(standard_deviation(var1_array)[1])

    input(f'\nPara ver el resultado de la variable: "{var2_users}" presione <<ENTER>>.')

    os.system('cls')
    print(f'Datos utilizados:{var2_array}\n')
    print(f"\nLa media de la variable es: {half(var2_array)[0]}.")
    print(f'Interpretacion: {half(var2_array)[1]}')

    print(f'\nLa mediana se encuentra en el indice: {medium(var2_array)[1]} y su valor es: {medium(var2_array)[0]}.')
    print(medium(var2_array)[2])

    print(f'\nDesviacion estandar: {standard_deviation(var2_array)[0]}')
    print(standard_deviation(var2_array)[1])


def point_b(data_base):
    enrollment_value = random_variable_extractor(data_base, "enrollmentValue")
    stratum = random_variable_extractor(data_base, "stratum")

    covariance = round(np.cov(enrollment_value, stratum)[0][1], 2)

    return covariance,\
           "Hallando el la covarianza entre el valor de la matricula y el estrato de los estudiantes\n" \
           "podemos saber que hay una fuerte relacion lineal directa ya que es un valor positivo\n" \
           "muy grande. Lo cual indica que cuando el valor de una de nuestras variables aumenta.\n" \
           "la otra también lo hará.",


def point_c(data_base):

    print('Tabla de frecuencias para Genero:')
    print('Tomando en cuenta True => Mujer y False => Hombre por facilidad en el manejo de datos binarios.')
    print(f'{generate_frequency_table(data_base, "gender")[0]}\n'
          f'n: {generate_frequency_table(data_base, "gender")[1]}\n')
    print('Intervalos:')
    for i in range(0, len(generate_frequency_table(data_base, "gender")[2][0])):
        print(f'{i+1} = ({generate_frequency_table(data_base, "gender")[2][1][i]}) '
              f'- ({generate_frequency_table(data_base, "gender")[2][0][i]})')
    print('Al realizar los intervalos nos damos cuenta que a partir de MU +- 2Sigma los datos pertenecen al\n'
          'teorema empirico.')
    print('')
    # ------------------------------------------------------------------------------------------------------------------
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


def point_d(data_base):
    return f'La cantidad de personas que trabajan dentro'\
        f' de nuestra base de datos es: {len(filter_by_variable_bool(data_base, "isWorking")[0])}',\
        f'La cantidad de datos totales de nuestra base es n = {len(data_base)}\n',\
        f'Entonces tenemos que la probabilidad de que tomando una persona al azar esta trabaje'\
        f' es del: '\
        f'%{round(probability_of_one(len(filter_by_variable_bool(data_base, "isWorking")[0]), len(data_base)) * 100, 4)}'


def point_e(data_base):
    gender_var = random_variable_extractor(data_base, "gender")
    woman_counter = 0
    for gender in gender_var:
        if gender:
            woman_counter += 1

    return f"La probabilidad de que seleccionada al azar una persona, esta sea una mujer" \
        f" es de: {round(probability_of_one(woman_counter, len(data_base)) * 100, 4)}%"


def point_f(data_base):
    filtered_by_is_not_working = filter_by_variable_bool(data_base, "isWorking")[1]
    prob_is_working = len(filtered_by_is_not_working)/len(data_base)
    gender_list = random_variable_extractor(data_base, "gender")
    success_case_is_man = 0

    for gender in gender_list:
        if not gender:
            success_case_is_man += 1

    prob_is_man = success_case_is_man / len(data_base)

    prob_result = (prob_is_man * prob_is_working) * 100

    return f"La probabilidad de que tomando un individuo al azar este no trabaje y sea hombre\n" \
           f"es del: {round(prob_result, 4)}%"


def point_g():
    filtered_by_is_not_working = filter_by_variable_bool(data_base, "isWorking")[1]
    prob_is_working_a = len(filtered_by_is_not_working) / len(data_base)
    gender_list = random_variable_extractor(data_base, "gender")
    success_case_is_man = 0

    for gender in gender_list:
        if not gender:
            success_case_is_man += 1

    prob_is_man_b = success_case_is_man / len(data_base)
    prob_result_a_and_b = prob_is_man_b * prob_is_working_a

    prob_b_given_a = (prob_result_a_and_b / prob_is_working_a) * 100

    return f"La probabilidad de elegir una persona al azar y que esta sea hombre dado que no trabaja\n" \
           f"es del: {prob_b_given_a}%"
