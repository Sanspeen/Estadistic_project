import pandas as pd
from Functions import *
BEARS_TO_ORDER = [15000, 18000, 24000, 28000]  # Units of bears
SELL_PRICE = 24  # Dollars
BASE_PRICE = 16  # Dollars
SALE_SELL_PRICE = 5  # Dollars
EXPECTED_DEMAND = 20000  # Units of bears
CONFIDENCE_LEVEL = 0.95  # Percentage
DEMAND_IC = [10000, 30000]


def point_a():
    standard_devitation = round((DEMAND_IC[1] - DEMAND_IC[0]) / 6, 4)
    # MAKE NORMAL GRAPH.
    return EXPECTED_DEMAND, standard_devitation


def point_b():
    premise = "Definimos X como la demanda.\n" \
              "para tener de esta manera P(X < x).\n" \
              "Tenemos una desviacion estandar de: 3333.3333.\n" \
              f"Y una media de: {EXPECTED_DEMAND}"
    answer_1 = f"Ingresando los datos para {BEARS_TO_ORDER[0]} en el aplicativo," \
               f" tenemos que: P(X < {BEARS_TO_ORDER[0]}) = 0.0668 * 100 => 6.68%" \
               f" de probabilidades de que la demanda sea menor que el stock esperado."
    answer_2 = f"Ingresando los datos para {BEARS_TO_ORDER[1]} en el aplicativo," \
               f" tenemos que: P(X < {BEARS_TO_ORDER[1]}) = 0.2742 * 100 => 27.47%" \
               f" de probabilidades de que la demanda sea menor que el stock esperado."
    answer_3 = f"Ingresando los datos para {BEARS_TO_ORDER[2]} en el aplicativo," \
               f" tenemos que: P(X < {BEARS_TO_ORDER[2]}) = 0.8849 * 100 => 88.49%" \
               f" de probabilidades de que la demanda sea menor que el stock esperado."
    answer_4 = f"Ingresando los datos para {BEARS_TO_ORDER[3]} en el aplicativo," \
               f" tenemos que: P(X < {BEARS_TO_ORDER[3]}) = 0.9918 * 100 => 99.18% de" \
               f" probabilidades de que la demanda sea menor que el stock esperado."

    return premise, answer_1, answer_2, answer_3, answer_4
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




