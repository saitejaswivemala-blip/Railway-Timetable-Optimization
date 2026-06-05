import pandas as pd


def comparison_table():

    data = {

        "Algorithm":[
        "Proposed GA+FW",
        "Genetic Algorithm",
        "PSO",
        "Simulated Annealing"
        ],

        "Profit":[
        1917917,
        1650000,
        1600000,
        1580000
        ],

        "Passenger Cost":[
        0.46,
        0.52,
        0.55,
        0.57
        ]
    }

    table=pd.DataFrame(data)

    print(table)

    return table