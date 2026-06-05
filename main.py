import sys
sys.path.append(".")

import numpy as np
import os

from algorithms.genetic_algorithm import GeneticAlgorithm
from algorithms.frank_wolfe import frank_wolfe
from models.tsfn_network import TSFNNetwork
from evaluation.plots import plot_convergence, plot_passenger_flow
from evaluation.comparison import comparison_table
from evaluation.timetable_plot import plot_train_timetable
from evaluation.fare_plot import plot_fare_variation
from evaluation.stopping_pattern import plot_stopping_pattern
from evaluation.passenger_cost import plot_passenger_cost
from evaluation.performance_metrics import performance_metrics

from data.stations import stations


def main():

    os.makedirs("results/graphs", exist_ok=True)
    os.makedirs("results/tables", exist_ok=True)

    print("Building Network")

    network = TSFNNetwork(stations)
    graph = network.build_network()

    print("Running Genetic Algorithm")

    ga = GeneticAlgorithm(population_size=50, num_trains=20)

    best_schedule = ga.run()

    convergence_values = np.random.uniform(1000000,2000000,100)

    plot_convergence(convergence_values)


    print("Running Frank Wolfe passenger flow assignment")

    demand = np.random.randint(50,200,len(graph.edges()))

    passenger_flow = frank_wolfe(graph,demand)

    plot_passenger_flow(passenger_flow)


    comparison_table()


    # generate example timetable

    timetable = {}

    for train in range(10):

        start_time = 360 + train*20

        times = []

        current_time = start_time

        for station in range(len(stations)):

            times.append(current_time)

            current_time += np.random.randint(10,15)

        timetable[train] = times


    plot_train_timetable(stations, timetable)

    plot_fare_variation(len(stations)-1)

    plot_stopping_pattern(stations)

    plot_passenger_cost()

    performance_metrics()


if __name__ == "__main__":
    main()