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


def point_b(data_base):
    genders = random_variable_extractor(data_base, 'gender')
    gender_male = []
    gender_female = []
    # filter by gender
    for i in genders:
        if i == 'Male':
            gender_male.append(i)
        else:
            gender_female.append(i)

    female_half = len(gender_female) / len(data_base)
    male_half = len(gender_male)/len(data_base)

    male_error = possible_error(male_half, gender_male)
    female_error = possible_error(female_half, gender_female)

    male_intervals = []
    female_intervals = []

    male_intervals.append(round(ic_generator(male_half, male_error, 2.576)[0], 4))
    male_intervals.append(round(ic_generator(male_half, male_error, 2.576)[1], 4))

    female_intervals.append(round(ic_generator(female_half, female_error, 2.576)[0], 4))
    female_intervals.append(round(ic_generator(female_half, female_error, 2.576)[1], 4))

    print(f'Con base en los resultados anteriores podemos concluir que el 99% de las muestras de \n'
          f'tamaño {len(data_base)} para los hombres tendran una "mu" comprendida entre este intervalo:'
          f' {male_intervals}\n')

    print(f'Con base en los resultados anteriores podemos concluir que el 99% de las muestras de \n'
          f'tamaño {len(data_base)} para las mujeres tendran una "mu" comprendida entre este intervalo:'
          f' {female_intervals}\n')

    print('Por lo tanto se concluye que nuestros intervalos de confianza de hombres difieren de los de las mujeres.')


def point_c(data_base):
    sum = 0
    organized_array = random_variable_extractor(data_base, 'lastSemesterAvg')
    organized_array = sorted(organized_array, reverse=True)
    five_percentage_of_array = math.ceil(len(organized_array) * 0.05)
    for i in range(0, five_percentage_of_array):
        sum += organized_array[i]

    result = round(sum/five_percentage_of_array, 4)

    print(f'Para ser del 5% de los mejores estudiantes, basandonos en nuestros promedios encontramos que\n'
          f'se tendria que tener al menos una nota de {organized_array[five_percentage_of_array-1]} ya que el 5% de\n'
          f'los estudiantes tienen un promedio dado de: {result}\n')
    print(f'Las notas son: {organized_array}')






