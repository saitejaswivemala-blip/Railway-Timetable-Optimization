import os
import numpy as np


def ensure_directory(path):
    """
    Ensure a directory exists.
    """
    os.makedirs(path, exist_ok=True)


def normalize(values):
    """
    Normalize values between 0 and 1.
    """
    values = np.array(values)
    min_val = np.min(values)
    max_val = np.max(values)

    if max_val - min_val == 0:
        return values

    return (values - min_val) / (max_val - min_val)


def minutes_to_time(minutes):
    """
    Convert minutes to HH:MM format.
    """
    hours = int(minutes // 60)
    mins = int(minutes % 60)

    return f"{hours:02d}:{mins:02d}"


def generate_random_demand(num_stations, low=50, high=200):
    """
    Generate synthetic OD passenger demand matrix.
    """
    demand = np.random.randint(low, high, (num_stations, num_stations))

    for i in range(num_stations):
        demand[i][i] = 0

    return demand


def safe_divide(a, b):
    """
    Avoid division by zero.
    """
    if b == 0:
        return 0
    return a / b
