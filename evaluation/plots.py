import matplotlib.pyplot as plt


def plot_convergence(values):

    plt.figure()

    plt.plot(values)

    plt.xlabel("Iteration")

    plt.ylabel("Objective Value")

    plt.title("Algorithm Convergence")

    plt.savefig("results/graphs/convergence.png")

    plt.show()


def plot_passenger_flow(flow):

    plt.figure()

    plt.bar(range(len(flow)),flow)

    plt.xlabel("Section")

    plt.ylabel("Passengers")

    plt.title("Passenger Flow Distribution")

    plt.savefig("results/graphs/passenger_flow.png")

    plt.show()