import matplotlib.pyplot as plt
import numpy as np


def plot_fare_variation(num_sections):

    fares = np.random.uniform(0.27, 0.36, num_sections)

    plt.figure()

    plt.plot(range(num_sections), fares, marker='o')

    plt.xlabel("Railway Section")

    plt.ylabel("Fare")

    plt.title("Dynamic Fare Variation")

    plt.savefig("results/graphs/fare_variation.png")

    plt.show()