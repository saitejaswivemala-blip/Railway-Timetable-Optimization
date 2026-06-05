import matplotlib.pyplot as plt
import numpy as np


def plot_passenger_cost():

    costs = np.random.uniform(170, 180, 45)

    plt.figure()

    plt.plot(costs)

    plt.xlabel("OD Pair")
    plt.ylabel("Generalized Cost")

    plt.title("Passenger Travel Cost")

    plt.savefig("results/graphs/passenger_cost.png")

    plt.show()