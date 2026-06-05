import numpy as np
from models.cost_functions import generalized_cost


def frank_wolfe(network, demand):

    num_edges = len(network.edges())

    flow = np.zeros(num_edges)

    for iteration in range(30):

        costs = []

        for i in range(num_edges):

            cost = generalized_cost(
                flow=flow[i],
                preference=0.8,
                distance=50,
                fare=0.3,
                dwell=3
            )

            costs.append(cost)

        costs = np.array(costs)

        best_path = np.argmin(costs)

        new_flow = np.zeros(num_edges)

        new_flow[best_path] = sum(demand)

        step = 1/(iteration+1)

        flow = flow + step*(new_flow-flow)

    return flow