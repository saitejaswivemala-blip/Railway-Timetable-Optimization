import numpy as np

TRAIN_CAPACITY = 600

alpha = 2
beta = 0.4
gamma = 0.2


def departure_cost(flow, preference):

    return alpha/preference + beta*(flow/TRAIN_CAPACITY)


def travel_cost(flow, distance, fare):

    congestion = beta*(flow/TRAIN_CAPACITY)

    ticket = fare*distance

    return ticket + congestion


def dwell_cost(flow, dwell_time):

    return gamma*dwell_time + beta*(flow/TRAIN_CAPACITY)


def generalized_cost(flow, preference, distance, fare, dwell):

    dc = departure_cost(flow, preference)

    tc = travel_cost(flow, distance, fare)

    wc = dwell_cost(flow, dwell)

    return dc + tc + wc