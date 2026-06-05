import matplotlib.pyplot as plt
import numpy as np


def plot_stopping_pattern(stations):

    stops = np.random.randint(5,40,len(stations))

    plt.figure()

    plt.bar(stations, stops)

    plt.xticks(rotation=45)

    plt.ylabel("Number of Trains Stopping")

    plt.title("Train Stopping Pattern")

    plt.savefig("results/graphs/stopping_pattern.png")

    plt.show()