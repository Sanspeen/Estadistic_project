from Data import *
from Functions import *
import os


def point_a(data_base):
    stratum_2 = filter_by_punctual_value(data_base, 'stratum', 2)
    enrollment_value_stratum_2 = random_variable_extractor(stratum_2, 'enrollmentValue')
    half_of_stratum_2 = half(enrollment_value_stratum_2)[0]
    print(enrollment_value_stratum_2)
    standard_deviation_of_stratum_2 = standard_deviation(enrollment_value_stratum_2)[0]
    print(f'Promedio del valor de la matricula para estrato 2: {half_of_stratum_2}')
    print(f'Desviacion estandar del valor de matricula para estrato 2: {standard_deviation_of_stratum_2}')
    input('Para ver el resultado para el siguiente estrato presiona <<Enter>>.')
    os.system('cls')

    stratum_3 = filter_by_punctual_value(data_base, 'stratum', 3)
    enrollment_value_stratum_3 = random_variable_extractor(stratum_3, 'enrollmentValue')
    half_of_stratum_3 = half(enrollment_value_stratum_3)[0]
    standard_deviation_of_stratum_3 = standard_deviation(enrollment_value_stratum_3)[0]
    print(f'Promedio del valor de la matricula para estrato 3: {half_of_stratum_3}')
    print(f'Desviacion estandar del valor de matricula para estrato 3: {standard_deviation_of_stratum_3}')
    input('Para ver el resultado para el siguiente estrato presiona <<Enter>>.')
    os.system('cls')

    stratum_4 = filter_by_punctual_value(data_base, 'stratum', 4)
    enrollment_value_stratum_4 = random_variable_extractor(stratum_4, 'enrollmentValue')
    half_of_stratum_4 = half(enrollment_value_stratum_4)[0]
    standard_deviation_of_stratum_4 = standard_deviation(enrollment_value_stratum_4)[0]
    print(f'Promedio del valor de la matricula para estrato 4: {half_of_stratum_4}')
    print(f'Desviacion estandar del valor de matricula para estrato 4: {standard_deviation_of_stratum_4}')
    input('Para ver el resultado para el siguiente estrato presiona <<Enter>>.')
    os.system('cls')

    stratum_5 = filter_by_punctual_value(data_base, 'stratum', 5)
    enrollment_value_stratum_5 = random_variable_extractor(stratum_5, 'enrollmentValue')
    half_of_stratum_5 = half(enrollment_value_stratum_5)[0]
    standard_deviation_of_stratum_5 = standard_deviation(enrollment_value_stratum_5)[0]
    print(f'Promedio del valor de la matricula para estrato 5: {half_of_stratum_5}')
    print(f'Desviacion estandar del valor de matricula para estrato 5: {standard_deviation_of_stratum_5}')









