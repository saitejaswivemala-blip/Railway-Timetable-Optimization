import matplotlib.pyplot as plt


def plot_train_timetable(stations, timetable):

    plt.figure(figsize=(12,6))

    for train_id, times in timetable.items():

        station_index = list(range(len(stations)))

        plt.plot(times, station_index, marker='o', label=f"Train {train_id}")

    plt.yticks(range(len(stations)), stations)

    plt.xlabel("Time (minutes)")
    plt.ylabel("Stations")
    plt.title("Train Timetable Diagram")

    plt.grid(True)

    plt.legend(fontsize=8)

    plt.savefig("results/graphs/train_timetable.png")

    plt.show()