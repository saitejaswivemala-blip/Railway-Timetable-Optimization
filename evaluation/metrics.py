import numpy as np


def railway_profit(revenue,cost):

    return revenue-cost


def passenger_cost(costs):

    return np.mean(costs)


def train_utilization(passengers,capacity):

    return passengers/capacity