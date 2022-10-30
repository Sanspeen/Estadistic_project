import pandas as pd


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