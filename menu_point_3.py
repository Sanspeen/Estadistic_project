from Functions import *
from scipy.stats import norm
import matplotlib.pyplot as plt
BEARS_TO_ORDER = [15000, 18000, 24000, 28000]  # Units of bears
SELL_PRICE = 24  # Dollars
BASE_PRICE = 16  # Dollars
SALE_SELL_PRICE = 5  # Dollars
EXPECTED_DEMANDS = [10000, 20000, 30000]  # Units of bears
CONFIDENCE_LEVEL = 0.95  # Percentage
DEMAND_IC = [10000, 30000]


def point_a():
    z_95 = 1.96
    alpha_half = round((1 - CONFIDENCE_LEVEL)/2, 4)
    addition = 0
    for number in EXPECTED_DEMANDS:
        addition += number

    miu = addition / len(EXPECTED_DEMANDS)

    sigma = (30000 - 20000)/z_95

    return miu, sigma


def point_b():
    miu = point_a()[0]
    sigma = point_a()[1]
    prob_results = []

    for units in BEARS_TO_ORDER:
        prob_results.append(round((units - miu) / sigma, 4))

    return BEARS_TO_ORDER, prob_results



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




