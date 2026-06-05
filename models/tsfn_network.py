import networkx as nx

class TSFNNetwork:

    def __init__(self, stations):

        self.stations = stations

        self.graph = nx.DiGraph()


    def build_network(self):

        for i in range(len(self.stations)-1):

            self.graph.add_edge(self.stations[i],
                                self.stations[i+1],
                                weight=1)

        return self.graph