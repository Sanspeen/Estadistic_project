import math
import statistics as sta
import pandas as pd
from numpy import mean
import numpy as np
from Data import data_base
import matplotlib.pyplot as plt
import seaborn as sns
import pylab
import scipy.stats as stats


def random_variable_extractor(data_base, name_of_variable):
    extracted_variable_array = []
    for i in range(0, len(data_base)):
        extracted_variable_array.append(data_base[i].get(name_of_variable))
    extracted_variable_array.sort()
    return extracted_variable_array


def half(random_variable_array):
    half_result = round(mean(random_variable_array), 2)
    return half_result, f'La conclusión para la media aritmetica que obtuvimos es que el promedio\n' \
                                                   f'de nuestra variable tomada fue: {half_result}'


def medium(random_variable_array):
    medium_index = math.ceil(len(random_variable_array) / 2)
    medium_value = random_variable_array[medium_index - 1]
    return medium_value, medium_index, f'Nuestro punto medio de datos se encuentra en el indice: {medium_index}' \
                                       f' y toma el valor de: {medium_value}.'


def standard_deviation(random_variable_array):
    return round(sta.pstdev(random_variable_array), 4), 'La desviacion estandar es la que nos muestra la dispercion entre nuestros datos, a mayor el numero presentado, mayor dispercion entre los datos tendremos...\n' \
         f'por lo tanto nuestra desviacion estandar presenta un valor de: {round(sta.pstdev(random_variable_array), 4)}, Sí fuese 0 indicaria que no hay\n' \
         f'ninguna disperción.'


def topic_deviation(random_variable_array):
    return round(math.sqrt(standard_deviation(random_variable_array)[0]), 4)


def is_working_separator(random_variable_array):
    is_working_users = []
    not_working_users = []
    for i in random_variable_array:
        if i.get('isWorking'):
            is_working_users.append(i)
        else:
            not_working_users.append(i)

    return is_working_users, not_working_users


def accumulated_absolute_frequently(absolute_frequency_array):
    data = np.array(absolute_frequency_array)
    (unique, counts) = np.unique(data, True)
    absolute_fr = []
    sum = 0
    for i in unique:
        for j in absolute_frequency_array:

            if(i != j):
                absolute_frequency_array = list(filter((i).__ne__, absolute_frequency_array))
                break
            else:
                sum += 1

        absolute_fr.append(sum)
    return absolute_fr


def convert_to_percentage(array_to_convert):
    converted = []
    for i in array_to_convert:
        converted.append(round(i*100))
    return converted


def generate_frequency_table(data_base, variable_name):
    random_variable_array = random_variable_extractor(data_base, variable_name)
    half_of_variable = half(random_variable_array)[0]
    topic_deviation_of_variable = topic_deviation(random_variable_array)

    absolute_frequency = pd.Series(random_variable_array)
    sum = 0
    for i in absolute_frequency.value_counts():
        sum += i/len(absolute_frequency)

    data = {'f': absolute_frequency.value_counts(),
            'F': accumulated_absolute_frequently(random_variable_array),
            'fr': absolute_frequency.value_counts()/len(absolute_frequency),
            '%': convert_to_percentage(absolute_frequency.value_counts()/len(absolute_frequency))}

    # Separar esto en una funcion mas adelante.
    top_intervals = []
    bottom_intervals = []
    for i in range(0, 3):
        top_interval = round(half_of_variable + (i + 1) * topic_deviation_of_variable, 4)
        top_intervals.append(top_interval)

        bottom_interval = round(half_of_variable - (i + 1) * topic_deviation_of_variable, 4)
        bottom_intervals.append(bottom_interval)
    # Hasta aqui.
    intervals = []
    intervals.append(top_intervals)
    intervals.append(bottom_intervals)

    n = len(random_variable_array)
    data = pd.DataFrame(data, pd.unique(absolute_frequency))

    return data, n, intervals, sum


def filter_by_variable_bool(data_base, name_of_variable):
    filtered_variables_is_working = []
    filtered_variables_is_not_working = []
    for i in range(0, len(data_base)):
        if data_base[i].get(name_of_variable):
            filtered_variables_is_working.append(data_base[i])

    for j in range(0, len(data_base)):
        if not data_base[j].get(name_of_variable):
            filtered_variables_is_not_working.append(data_base[j])

    return filtered_variables_is_working, filtered_variables_is_not_working


def filter_by_punctual_value(data_base, name_of_variable, estimated_value):
    filtered_variables = []
    for i in range(0, len(data_base)):
        if data_base[i].get(name_of_variable) == estimated_value:
            filtered_variables.append(data_base[i])
    return filtered_variables


def probability_of_one(successful_cases, number_of_data):
    return successful_cases/number_of_data


def possible_error(estimated_p, data_base):
    return math.sqrt(estimated_p*(1-estimated_p)/len(data_base))


def ic_generator(estimated_p, estimated_error, z_value):
    bottom_interval = estimated_p - z_value * estimated_error
    top_interval = estimated_p + z_value * estimated_error

    return bottom_interval, top_interval


def linear_correlation(variable_1, variable_2, name_of_variable_1, name_of_variable_2):
    plt.scatter(variable_1, variable_2)
    plt.title('Diagrama de puntos.')
    plt.xlabel(name_of_variable_1)
    plt.ylabel(name_of_variable_2)
    plt.grid(linestyle='dotted')
    plt.show()

    data = {
        'Promedio ultimo semestre': variable_1,
        'Horas estudiadas': variable_2
    }

    matriz = pd.DataFrame(data)
    correlation = matriz.corr(method='spearman')
    return correlation


def dist_intervals(half_of_variable, topic_deviation_of_variable):
    top_intervals = []
    bottom_intervals = []
    intervals = []
    for i in range(0, 3):
        top_interval = round(half_of_variable + (i + 1) * topic_deviation_of_variable, 4)
        top_intervals.append(top_interval)

        bottom_interval = round(half_of_variable - (i + 1) * topic_deviation_of_variable, 4)
        bottom_intervals.append(bottom_interval)
    intervals.append(top_intervals)
    intervals.append(bottom_intervals)
    return intervals











