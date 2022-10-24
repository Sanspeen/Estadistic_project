import math
import statistics as sta
from numpy import mean
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


def standard_devitation(random_variable_array):
    return round(sta.pstdev(random_variable_array), 4), 'La desviacion estandar es la que nos muestra la dispercion entre nuestros datos, a mayor el numero presentado, mayor dispercion entre los datos tendremos...\n' \
         f'por lo tanto nuestra desviacion estandar presenta un valor de: {round(sta.pstdev(random_variable_array), 4)}, Sí fuese 0 indicaria que no hay\n' \
         f'ninguna disperción.'


def tipic_devitation(random_variable_array):
    return round(math.sqrt(standard_devitation(random_variable_array)))


def is_working_separator(random_variable_array):
    is_working_users = []
    not_working_users = []
    for i in random_variable_array:
        if(i.get('isWorking') == True):
            is_working_users.append(i)
        else:
            not_working_users.append(i)

    return is_working_users, not_working_users
