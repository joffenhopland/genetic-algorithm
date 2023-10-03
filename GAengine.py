import random
from Utils import Chromosome, Food


class GAEngine:
    def __init__(self):
        self.population = []
        self.food = []
        self.generations = 0

    def make_initial_population(self, population_size):
        for i in range(population_size):
            self.population.append(
                Chromosome(random.randint(0, 790), random.randint(0, 590))
            )

    def add_food(self, no_of_food):
        for i in range(no_of_food):
            self.food.append(Food(random.randint(0, 790), random.randint(0, 590)))

    # selection code goes here...
    def select_parent(self):
        # Select an individual from the population to be a parent for the next generation, based on its fitness.
        # we are here using the roulette wheel selection method.
        # The more fit an individual is, the higher its chance of being selected.
        total_fitness = sum(individual.fitness for individual in self.population)
        selection_point = random.uniform(0, total_fitness)
        for individual in self.population:
            selection_point -= individual.fitness
            if selection_point <= 0:
                return individual

    def do_crossover(self, no_of_offspring):
        # Produce a new generation of Chromosomes
        #  selects two parents and produces a child using the crossover method.
        # The child is then mutated. This process is repeated no_of_offspring times to produce the number of children for the next generation
        new_population = []
        for _ in range(no_of_offspring):
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            while parent1 == parent2:  # making syre that the two parents are different
                parent2 = self.select_parent()
            child = parent1.crossover(parent2)
            child.mutate()
            new_population.append(child)
        self.population = (
            new_population  # replace old population with the new generation
        )

    # fitness calculation goes here...
    def assign_fitness(self):
        for individual in self.population:
            # The closer the individual is to the food, the lower the distance will be.
            # to ensure that individuals closer to the food have a higher fitness, we'll take the inverse of the distance.
            individual.fitness = 1 / individual.get_distance_to(self.food[0])

    def get_population(self):
        return self.population

    def get_foods(self):
        return self.food
