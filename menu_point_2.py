from Functions import *
import os
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import seed, randn
from scipy.stats import normaltest, shapiro
from statsmodels.graphics.gofplots import qqplot


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
          f'tama??o {len(data_base)} para los hombres tendran una "mu" comprendida entre este intervalo:'
          f' {male_intervals}\n')

    print(f'Con base en los resultados anteriores podemos concluir que el 99% de las muestras de \n'
          f'tama??o {len(data_base)} para las mujeres tendran una "mu" comprendida entre este intervalo:'
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


def point_d(data_base):
    organized_array = random_variable_extractor(data_base, 'lastSemesterAvg')
    twenty_five_percentage_of_array = math.ceil(len(organized_array) * 0.25)
    sum = 0
    for i in range(0, twenty_five_percentage_of_array):
        sum += organized_array[i]
    result = round(sum / twenty_five_percentage_of_array, 4)

    print(f'Para ser del 25% de los peores estudiantes, basandonos en nuestros promedios encontramos que\n'
          f'se tendria que tener a lo sumo una nota de {organized_array[twenty_five_percentage_of_array - 1]}'
          f' ya que el 25% de\n'
          f'los estudiantes tienen un promedio dado de: {result}\n')
    print(f'Las notas son: {organized_array}')


def point_e(data_base):
    is_working_array = filter_by_variable_bool(data_base, 'isWorking')[0]
    is_not_working_array = filter_by_variable_bool(data_base, 'isWorking')[1]

    study_of_workers = random_variable_extractor(is_working_array, 'studyHours')
    study_not_workers = random_variable_extractor(is_not_working_array, 'studyHours')

    is_working_half = half(study_of_workers)[0]
    is_not_working_half = half(study_not_workers)[0]

    input('Primero que nada planteamos la hipotesis nula que vendria a ser: Si el promedio de horas de estudio para\n'
          'los que no trabajan es mayor... Con base en esta premisa analizaremos la base de datos y comprobaremos\n'
          'al 100% si esta hipotesis es verdadera o falsa. Presione <<Enter>> para continuar.')
    os.system('cls')

    print(f'Horas de estudio personas que trabajan: {study_of_workers}')
    print(f'Promedio trabajan:{is_working_half}\n')
    print(f'Horas de estudio personas que NO trabajan: {study_not_workers}')
    print(f'Promedio no trabajan:{is_not_working_half}\n')

    if is_working_half > is_not_working_half:
        print(f'Conclusion: Se rechaza la hipotesis nula puesto a que {is_working_half} >= {is_not_working_half}.')

    else:
        print(f'Conclusion: NO se rechaza la hipotesis nula puesto a que {is_working_half} < {is_not_working_half}.')


def point_f(data_base):
    academic_avg_array = random_variable_extractor(data_base, 'lastSemesterAvg')
    study_hours_array = random_variable_extractor(data_base, 'studyHours')
    print(linear_correlation(academic_avg_array, study_hours_array,'promedio academico anterior semestre',
                             'Horas estudiadas fuera de clase'))

    print('\nSe implemento la correlacion de Spearman debido a que esta a diferencia de la re Pearson nos sirve\n'
          'para evaluar la correlacion entre dos variables continuas.')


def point_g(data_base):
    average_array = random_variable_extractor(data_base, 'lastSemesterAvg')
    plt.hist(average_array)
    plt.title('Histograma de una variable promedio del ultimo semestre')
    plt.xlabel('Valor de la variable')
    plt.ylabel('Conteo')
    plt.show()

    stat, p = shapiro(average_array)
    print('shapiro')
    print('Estadisticos=%.3f, p=%.3f' % (stat, p))
    alpha = 0.05
    if p > alpha:
        print('La muestra parece Gaussiana o Normal (no se rechaza la hip??tesis nula H0).')
    else:
        print('La muestra no parece Gaussiana o Normal(se rechaza la hip??tesis nula H0).')

    print('')








