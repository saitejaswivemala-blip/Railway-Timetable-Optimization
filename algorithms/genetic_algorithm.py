import random
import numpy as np


class GeneticAlgorithm:

    def __init__(self, population_size, num_trains):

        self.population_size = population_size

        self.num_trains = num_trains

        self.population = []


    def initialize_population(self):

        for _ in range(self.population_size):

            chromosome = []

            for train in range(self.num_trains):

                departure = random.randint(360,1200)

                dwell_times = [random.randint(1,3) for _ in range(8)]

                chromosome.append([departure] + dwell_times)

            self.population.append(chromosome)


    def fitness(self, chromosome):

        total_revenue = 0
        operating_cost = 0

        ticket_price = 0.3
        passengers = 500

        for train in chromosome:
            dwell_times = train[1:]

            revenue = passengers * ticket_price
            
            cost = sum(dwell_times) * 50

            total_revenue += revenue
            operating_cost += cost

        return total_revenue - operating_cost

    def calculate_revenue(self, chromosome):

        return random.uniform(1e6,2e6)


    def calculate_cost(self, chromosome):

        return random.uniform(1e5,5e5)


    def selection(self):

        scored = [(self.fitness(c),c) for c in self.population]

        scored.sort(reverse=True)

        selected = [c for _,c in scored[:self.population_size//2]]

        return selected


    def crossover(self,parent1,parent2):

        child=[]

        for i in range(len(parent1)):

            if random.random()<0.5:

                child.append(parent1[i])

            else:

                child.append(parent2[i])

        return child


    def mutate(self,chromosome):

        for train in chromosome:

            if random.random()<0.1:

                train[0]+=random.randint(-10,10)

        return chromosome


    def run(self,generations=100):

        self.initialize_population()

        for g in range(generations):

            parents=self.selection()

            new_population=[]

            while len(new_population)<self.population_size:

                p1=random.choice(parents)

                p2=random.choice(parents)

                child=self.crossover(p1,p2)

                child=self.mutate(child)

                new_population.append(child)

            self.population=new_population

        best=max(self.population,key=self.fitness)

        return best