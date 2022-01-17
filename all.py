import random

pop_size = 8
TARGET_CHROMOSOMES = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
NUMB_OF_ELITE_CHROMOSOMES = 1
TOURNAMENT_SELECTION_SIZE = 4
MUTATION_RATE = 0.25


class Chromosome:
    def __init__(self):
        self._fitness = 0

    genes = []

    i = 0

    while i < TARGET_CHROMOSOMES.__len__():
        if random.randint(0, 1) >= 0.5:
            genes.append(1)
        else:
            genes.append(0)

        i += 1

    def get_genes(self):
        return self.genes

    def get_fitness(self):
        self._fitness = 0
        for i in range(len(self.genes)):
            if self.genes[i] == TARGET_CHROMOSOMES[i]:
                self._fitness += 1
        return self._fitness

    def __str__(self):
        return self.genes.__str__()


class Population(Chromosome):

    def __init__(self, size):
        self._chromosomes = []
        i = 0
        while i < size:
            self._chromosomes.append(Chromosome().genes)
            i += 1

    def get_chromosome(self):
        return self._chromosomes


class GeneticAlgotithm(Chromosome, Population):

    def _crossover_population(pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_CHROMOSOMES):
            crossover_pop.get_chromosome().append(pop.get_chromosome()[i])

    def evolve(pop):
        return GeneticAlgotithm._mutate_population(GeneticAlgotithm._crossover_population(pop))

        i = NUMB_OF_ELITE_CHROMOSOMES
        while i < pop_size:
            chromosome1 = GeneticAlgotithm._select_tournament_population(pop).get_chromosome()[0]
            chromosome2 = GeneticAlgotithm._select_tournament_population(pop).get_chromosome()[0]
            crossover_pop.get_chromosome().append(GeneticAlgotithm._crossover_chromomsomes(chrmosome1, chrmosome2))
            i += 1
        return crossover_pop

    def _mutate_population(pop):
        for i in range(NUMB_OF_ELITE_CHROMOSOMES, pop_size):
            GeneticAlgotithm._mutate_chromomsomes(pop.get_chromosome()[i])
        return pop

    def _crossover_chromomsomes(chrmosome1, chrmosome2):
        crossover_chrom = Chromosome()
        for i in range(TARGET_CHROMOSOMES.__len__()):
            if random.random() >= 0.5:
                crossover_chrom.get_genes()[i] = chrmosome1.get_genes()[i]
            else:
                crossover_chrom.get_genes()[i] = chrmosome2.get_genes()[i]
        return crossover_chrom

    def _mutate_chromomsomes(chrmosome):
        for i in range(TARGET_CHROMOSOMES.__len__()):
            if random.random() < MUTATION_RATE:
                if random.random() < 0.5:
                    chrmosome.get_genes()[i] = 1
                else:
                    chrmosome.get_genes()[i] = 0

    def _select_tournament_population(pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_chromosome().append(pop.get_chromosome()[random.randrange(0, pop_size)])
            i += 1
        tournament_pop.get_chromosome().sort(key=lambda x: x.get_fitness, reverse=True)
        return tournament_pop


def _print_population(pop, gen_number):
    print("\n----------------------------------------------------------")
    print("Generation #", gen_number, "| Fittest chromosome fitness:", pop.get_chromosome()[0].get_fitness())
    print("Target Chromosome:", TARGET_CHROMOSOMES)
    print("------------------------------------------------------------")
    i = 0
    for x in pop.get_chromosome():
        print("Chromosome #", i, " :", x, "| Fitness:", x.get_fitness())
        i += 1


population = Population(pop_size)
population.get_chromosome().sort(key=lambda x: x.get_fitness(), reverse=True)
_print_population(population, 0)
generation_number = 1
while population.get_chromosome()[0].get_fitness() < TARGET_CHROMOSOMES.__len__():
    population = GeneticAlgotithm.evolve(population)
    population.get_chromosome().sort(key=lambda x: x.get_fitness(), reverse=True)
    _print_population(population, generation_number)
    generation_number += 1
