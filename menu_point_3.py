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

    sigma = round((30000 - 20000)/z_95, 4)

    return miu, sigma


def point_b():
    miu = point_a()[0]
    sigma = point_a()[1]
    prob_results = []

    for units in BEARS_TO_ORDER:
        prob_results.append(round((units - miu) / sigma, 4))

    prob_true = [0.8365, 0.6517, 0.2177, 0.0582]

    return BEARS_TO_ORDER, prob_results, prob_true


def point_c():
    utility = 8
    loses = 11
    scenarios = EXPECTED_DEMANDS

    order_scenarios = []

    for order in BEARS_TO_ORDER:
        order_calculated = []
        for scenario in scenarios:
            if scenario == 10000:
                order_calculated.append((utility * scenario) - (loses * (order - scenario)))

            elif scenario == 20000 and order < scenario:
                order_calculated.append(utility * order)

            elif scenario == 20000 and order > scenario:
                order_calculated.append((utility * scenario) - (loses * abs((order - scenario))))

            elif scenario == 30000 and order < scenario:
                order_calculated.append(utility * order)

        # Matrix where all of our scenarios and order demand get their loses or wins
        order_scenarios.append(order_calculated)
    order_scenarios = np.array(order_scenarios)  # conversion de una lista de listas a Matriz
    return order_scenarios


def point_d():
    miu = point_a()[0]
    sigma = point_a()[1]
    z_70 = 0.5244
    P = 0.6985
    order = z_70 * sigma + miu
    results = []
    for i in range(0, len(EXPECTED_DEMANDS)-1):
        results.append(round((EXPECTED_DEMANDS[i] * 8) - (11 * (order - EXPECTED_DEMANDS[i])), 0))
    results.append(round(order * 8, 0))
    return results

