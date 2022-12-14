import pandas as pd
from Functions import *


def point_a(data_base):
    volume_not_sorted = pd.DataFrame(data_base['Volumen (ml)'])
    volume = volume_not_sorted.sort_values(by='Volumen (ml)')
    index_of_variable = 0
    array_of_volumes = []

    for i in volume['Volumen (ml)']:
        array_of_volumes.append(i)

    for i in range(0, len(array_of_volumes)):
        item = array_of_volumes[i]
        if float(item.replace(',', '.')) >= 153.0:
            index_of_variable = i
            break

    less_glass = 0
    for i in range(0, len(array_of_volumes)):
        if array_of_volumes[i] < array_of_volumes[index_of_variable]:
            less_glass += 1

    print(f'El porcentaje de vasos que contendra menos de 150ml es de: {less_glass/len(array_of_volumes)*100}%')


def point_b(data_base):
    volume_not_sorted = pd.DataFrame(data_base['Volumen (ml)'])
    volume = volume_not_sorted.sort_values(by='Volumen (ml)')
    array_of_volumes = []
    index_of_variable_1 = 0
    index_of_variable_2 = 0

    for i in volume['Volumen (ml)']:
        array_of_volumes.append(i)

    for i in range(0, len(array_of_volumes)):
        item = array_of_volumes[i]
        if float(item.replace(',', '.')) >= 152.0:
            index_of_variable_1 = i
            break

    array_lenght = len(array_of_volumes)-1
    while array_lenght > 0:
        item = array_of_volumes[array_lenght]
        if float(item.replace(',', '.')) <= 158.0:
            index_of_variable_2 = array_lenght
            break
        array_lenght -= 1

    print(f'{(index_of_variable_2 - index_of_variable_1)/len(array_of_volumes) * 100}% seria la probabilidad de que\n'
          f'un vaso contenga entre 152 y 158ml.')


def point_c():
    print('Teniendo en cuenta que analizando la cantidad de vasos que cuenten con esta medida (155ml) en nuestra\n'
          'base de datos y dado que no existe ninguno, podemos concluir que la probabilidad de que esto pase es de: 0%')


def point_d(data_base):
    volume_not_sorted = pd.DataFrame(data_base['Volumen (ml)'])
    volume = volume_not_sorted.sort_values(by='Volumen (ml)')
    array_of_volumes = []
    for i in volume['Volumen (ml)']:
        array_of_volumes.append(i)

    five_percentage_of_array = math.ceil(len(array_of_volumes) * 0.05)

    print(f'Todos los valores por debajo de: {array_of_volumes[five_percentage_of_array - 1]}, entrarian en el\n'
          f'5% de los vasos con menos contenido.')




