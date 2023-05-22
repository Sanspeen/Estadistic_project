from Functions import *
import os
import matplotlib.pyplot as plt
import statistics
from scipy.stats import normaltest, shapiro
from scipy import stats


def point_a(data_base):
    stratum_1 = filter_by_punctual_value(data_base, 'stratum', 1)
    enrollment_value_stratum_1 = random_variable_extractor(stratum_1, 'enrollmentValue')
    half_of_stratum_1 = half(enrollment_value_stratum_1)[0]
    standard_deviation_of_stratum_1 = standard_deviation(enrollment_value_stratum_1)[0]

    stratum_2 = filter_by_punctual_value(data_base, 'stratum', 2)
    enrollment_value_stratum_2 = random_variable_extractor(stratum_2, 'enrollmentValue')
    half_of_stratum_2 = half(enrollment_value_stratum_2)[0]
    standard_deviation_of_stratum_2 = standard_deviation(enrollment_value_stratum_2)[0]

    stratum_3 = filter_by_punctual_value(data_base, 'stratum', 3)
    enrollment_value_stratum_3 = random_variable_extractor(stratum_3, 'enrollmentValue')
    half_of_stratum_3 = half(enrollment_value_stratum_3)[0]
    standard_deviation_of_stratum_3 = standard_deviation(enrollment_value_stratum_3)[0]

    stratum_4 = filter_by_punctual_value(data_base, 'stratum', 4)
    enrollment_value_stratum_4 = random_variable_extractor(stratum_4, 'enrollmentValue')
    half_of_stratum_4 = half(enrollment_value_stratum_4)[0]
    standard_deviation_of_stratum_4 = standard_deviation(enrollment_value_stratum_4)[0]

    stratum_5 = filter_by_punctual_value(data_base, 'stratum', 5)
    enrollment_value_stratum_5 = random_variable_extractor(stratum_5, 'enrollmentValue')
    half_of_stratum_5 = half(enrollment_value_stratum_5)[0]
    standard_deviation_of_stratum_5 = standard_deviation(enrollment_value_stratum_5)[0]

    stratum_6 = filter_by_punctual_value(data_base, 'stratum', 6)
    enrollment_value_stratum_6 = random_variable_extractor(stratum_6, 'enrollmentValue')
    half_of_stratum_6 = half(enrollment_value_stratum_6)[0]
    standard_deviation_of_stratum_6 = standard_deviation(enrollment_value_stratum_6)[0]

    return  f'Promedio del valor de la matricula para estrato 1: {half_of_stratum_1}\n' +\
            f'Desviacion estandar del valor de matricula para estrato 1: {standard_deviation_of_stratum_1}\n\n' +\
            f'Promedio del valor de la matricula para estrato 2: {half_of_stratum_2}\n' +\
            f'Desviacion estandar del valor de matricula para estrato 2: {standard_deviation_of_stratum_2}\n\n' +\
            f'Promedio del valor de la matricula para estrato 3: {half_of_stratum_3}\n' +\
            f'Desviacion estandar del valor de matricula para estrato 3: {standard_deviation_of_stratum_3}\n\n' +\
            f'Promedio del valor de la matricula para estrato 4: {half_of_stratum_4}\n' +\
            f'Desviacion estandar del valor de matricula para estrato 4: {standard_deviation_of_stratum_4}\n\n' +\
            f'Promedio del valor de la matricula para estrato 5: {half_of_stratum_5}\n' +\
            f'Desviacion estandar del valor de matricula para estrato 5: {standard_deviation_of_stratum_5}\n\n' +\
            f'Promedio del valor de la matricula para estrato 6: {half_of_stratum_6}\n' +\
            f'Desviacion estandar del valor de matricula para estrato 6: {standard_deviation_of_stratum_6}\n\n' +\
            "Conclusion: A mayore estrato socieconomico podemos evidenciar un alza en el \nprecio esperado de\n" +\
            " el valor de la matricula y diferencias sustanciales entre un precio y otro \n" +\
            "dentro de los mismos estratos."



def point_b(data_base):
    average_data = random_variable_extractor(data_base, "lastSemesterAvg")
    n_average = len(average_data)
    average_half = half(average_data)[0]
    alpha_divided_two = 0.025
    standard_devitation_average = standard_deviation(average_data)[0]
    z_aplha_div_2_value = round(stats.norm.ppf(1-alpha_divided_two), 4)

    lowest_limit = average_half - z_aplha_div_2_value * (standard_devitation_average / math.sqrt(n_average))
    highest_limit = average_half + z_aplha_div_2_value * (standard_devitation_average / math.sqrt(n_average))

    return average_half, (round(lowest_limit, 4), round(highest_limit, 4)),\
            f"Conclusion: Podemos afirmar con una confianza del 95%," \
            f"que el\npromedio de nuestra muestra de promedios academicos se encuentra en el " \
            f"intervalo: {(round(lowest_limit, 4), round(highest_limit, 4))}"

def point_c(data_base):
    sum = 0
    organized_array = random_variable_extractor(data_base, 'lastSemesterAvg')
    organized_array = sorted(organized_array, reverse=True)
    five_percentage_of_array = math.ceil(len(organized_array) * 0.05)
    for i in range(0, five_percentage_of_array):
        sum += organized_array[i]

    result = round(sum/five_percentage_of_array, 4)

    return f'Para ser del 5% de los mejores estudiantes, basandonos en nuestros promedios encontramos que\n' +\
          f'se tendria que tener al menos una nota de {organized_array[five_percentage_of_array-1]} ya que el 5% de\n' +\
          f'los estudiantes tienen un promedio dado de: {result}\n'


def point_d(data_base):
    organized_array = random_variable_extractor(data_base, 'lastSemesterAvg')
    five_percentage_of_array = math.ceil(len(organized_array) * 0.05)
    sum = 0
    for i in range(0, five_percentage_of_array):
        sum += organized_array[i]
    result = round(sum / five_percentage_of_array, 4)

    return f'Para ser del 25% de los peores estudiantes, basandonos en nuestros promedios encontramos que\n' +\
          f'se tendria que tener a lo sumo una nota de {organized_array[five_percentage_of_array - 1]}' +\
          f' ya que el 5% de\n' +\
          f'los estudiantes tienen un promedio dado de: {result}\n'


def point_e(data_base):
    is_working_array = filter_by_variable_bool(data_base, 'isWorking')[0]
    is_not_working_array = filter_by_variable_bool(data_base, 'isWorking')[1]

    study_of_workers = random_variable_extractor(is_working_array, 'studyHours')
    study_not_workers = random_variable_extractor(is_not_working_array, 'studyHours')

    is_working_half = half(study_of_workers)[0]
    is_not_working_half = half(study_not_workers)[0]

    answer_1 =  'Primero que nada planteamos la hipotesis nula que vendria a ser: Si el promedio de horas de estudio para\n' +\
                'los que no trabajan es mayor... Con base en esta premisa analizaremos la base de datos y comprobaremos\n' +\
                'al 100% si esta hipotesis es verdadera o falsa.\n' +\
                f'Promedio trabajan:{is_working_half}\n' +\
                f'Promedio no trabajan:{is_not_working_half}\n'

    if is_working_half > is_not_working_half:
        answer_2 = f'Conclusion: Se rechaza la hipotesis nula puesto a que {is_working_half} >= {is_not_working_half}.'
        return answer_1, answer_2
    else:
        answer_2 = f'Conclusion: NO se rechaza la hipotesis nula puesto a que {is_working_half} < {is_not_working_half}.'
        return answer_1, answer_2

def point_f(data_base):
    academic_avg_array = random_variable_extractor(data_base, 'lastSemesterAvg')
    study_hours_array = random_variable_extractor(data_base, 'studyHours')

    covariance = round(np.cov(academic_avg_array, study_hours_array)[0][1], 2)

    return f"Podemos evidenciar que pese a que si existe una relacion lineal debido a que tenemos una " \
           f"\ncovarianza positiva pero esta no es de un valor muy alto por lo cual su relacion no debe de\n" \
           f"ser muy fuerte.\nCovarianza:{covariance}"


def point_g(data_base):


    return f"Con base a la grafica anteriormente presentada podemos evidenciar una distribucion Chi cuadrado"


def show_graphic(data_base):
    enrollment_value_array = random_variable_extractor(data_base, 'enrollmentValue')
    plt.hist(enrollment_value_array)
    plt.title('Histograma de una variable promedio del ultimo semestre')
    plt.xlabel('Valor de la variable')
    plt.ylabel('Conteo')
    plt.show()








