import math
import statistics as sta
import pandas as pd
from numpy import mean
import numpy as np
from Data import database


def random_variable_extractor(data_base, name_of_variable):
    extracted_variable_array = []
    for i in range(0, len(data_base)):
        extracted_variable_array.append(data_base[i].get(name_of_variable))
    extracted_variable_array.sort()
    return extracted_variable_array


def half(random_variable_array):
    half_result = round(mean(random_variable_array))
    return half_result, f'La conclusión para la media aritmetica que obtuvimos es que el promedio\n' \
                                                   f'de nuestra variable tomada fue: {half_result}'


def medium(random_variable_array):
    medium_index = math.ceil(len(random_variable_array) / 2)
    medium_value = random_variable_array[medium_index - 1]
    return medium_value, medium_index, f'Nuestro punto medio de datos se encuentra en el indice: {medium_index} y toma el valor de: {medium_value}.'


def standard_deviation(random_variable_array):
    return round(sta.pstdev(random_variable_array), 4), 'La desviacion estandar es la que nos muestra la dispercion entre nuestros datos, a mayor el numero presentado, mayor dispercion entre los datos tendremos...\n' \
         f'por lo tanto nuestra desviacion estandar presenta un valor de: {round(sta.pstdev(random_variable_array), 4)}, Sí fuese 0 indicaria que no hay\n' \
         f'ninguna disperción.'


def topic_deviation(random_variable_array):
    return round(math.sqrt(standard_deviation(random_variable_array)))


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
    absolute_frequency = pd.Series(random_variable_array)

    data = {'f': absolute_frequency.value_counts(),
            'F': accumulated_absolute_frequently(random_variable_array),
            'fr': absolute_frequency.value_counts()/len(absolute_frequency),
            '%': convert_to_percentage(absolute_frequency.value_counts()/len(absolute_frequency))}

    n = len(random_variable_array)
    data = pd.DataFrame(data, pd.unique(absolute_frequency))
    return data, n


print(generate_frequency_table(database, 'isWorking')[0])
print(f'Total: {generate_frequency_table(database, "isWorking")[1]}')

print(generate_frequency_table(database, 'stratum')[0])
print(f'Total: {generate_frequency_table(database, "stratum")[1]}')
