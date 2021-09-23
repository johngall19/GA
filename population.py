import copy
import logging
import random
from locations import Locations
from distances import Distances
import reporting

from solution import Solution
from itertools import permutations
import math


POPULATION_SIZE = 10
MAX_GENERATIONS = 10
NUMBER_OUTPUT_LINKS = 15

if NUMBER_OUTPUT_LINKS > MAX_GENERATIONS:
    OUTPUT_GENERATION_STEP = 1
else:
    OUTPUT_GENERATION_STEP = MAX_GENERATIONS // NUMBER_OUTPUT_LINKS


def breed(parent_one, parent_two):
    # print("######### breed")
    # print(f"parent_one: {parent_one.route}")
    # print(f"parent_two: {parent_two.route}")

    child_one = copy.deepcopy(parent_one)
    child_two = copy.deepcopy(parent_two)

    num_genes = len(parent_one.route)

    # Anywhere upto the end -2 to ensure at least one swap
    cross_over_start = random.randint(0, num_genes - 2)
    cross_over_end = random.randint(cross_over_start + 1, num_genes - 1)

    # print(f"num_genes:       {num_genes}")
    # print(f"cross_over_start:      {cross_over_start}")
    # print(f"remaining_genes: {remaining_genes}")
    # print(f"cross_over_end:  {cross_over_end}")

    for i in range(cross_over_start, cross_over_end + 1):
        first_location = child_one.route[i]
        second_location = child_two.route[i]

        # Swap the locations in each of the children
        swap(child_one.route, first_location, second_location)
        swap(child_two.route, first_location, second_location)

    # print(f"child_one: {child1.route}")
    # print(f"child_two: {child2.route}")
    return child_one, child_two


def swap(values, first_value, second_value):
    first_index = values.index(first_value)
    second_index = values.index(second_value)

    temp = values[first_index]
    values[first_index] = values[second_index]
    values[second_index] = temp


def selection(population):
    selected = random.sample(population, 2)
    return min(selected, key=lambda x: x.fitness_score)


def select_parents(population):
    while True:
        candidate1 = selection(population)
        candidate2 = selection(population)
        if candidate1 != candidate2:
            break
    return candidate1, candidate2


def create_population(size, locations):
    population = []
    for x in range(size):
        population.append(Solution(locations))

    return population


def ga(distance_matix, locations):
    logging.basicConfig(level=logging.INFO)
    fittest_all_time = 999999999
    fittest_solution_all_time = None
    fittest_solution_per_generation = []

    population = create_population(POPULATION_SIZE, locations)
    logging.info(f" Population size: {len(population)}")

    # Print initial population
    # for solution in population:
    #     logging.debug(f" Solution: {solution.calc_fitness_score()}")

    for generation_number in range(MAX_GENERATIONS):
        #  Calculate the fitness of each solution
        for solution in population:
            solution.fitness_score = calc_fitness_score(distance_matix, solution.route)
            logging.debug(f" Solution: {solution.fitness_score}")

        current_fittest = min(population, key=lambda c: c.fitness_score)
        fittest_solution_per_generation.append(current_fittest)

        if current_fittest.fitness_score < fittest_all_time:
            fittest_solution_all_time = copy.deepcopy(current_fittest)
            fittest_all_time = current_fittest.fitness_score  # jgg is this neeeded

        next_generation = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = breed(parent1, parent2)
            next_generation.append(child1)
            next_generation.append(child2)

        population = next_generation

        logging.info(
            f" Generation number>>>>>>>>>>>>>>>>>>>>>>>>>: {generation_number}"
        )

    output_results(fittest_solution_all_time, fittest_solution_per_generation)


def output_results(solution, solutions):
    # [0, 7, 8, 6, 5, 4, 9, 3, 1, 2, 0]

    print(f"Overall shortest route found: {solution.route} : {solution.fitness_score}")

    routes = []
    counter = 0
    for sol in solutions[::OUTPUT_GENERATION_STEP]:
        print(
            f"Shortest path found {counter}: {sol.route} : {sol.fitness_score} : {sol}"
        )
        routes.append(sol.route)
        counter += 1

    # For testing. This is the optimum route for 10 locations
    # [0, 7, 8, 6, 5, 4, 9, 3, 1, 2, 0]
    # Add to solutions to display it for convenience
    optimum_solution = Solution([0, 7, 8, 6, 5, 4, 9, 3, 1, 2, 0])
    optimum_solution.route = [0, 7, 8, 6, 5, 4, 9, 3, 1, 2, 0]
    solutions.append(optimum_solution)

    reporting.generate_report(solutions)


def calc_fitness_score(distance_matix, route):
    total_distance = 0

    for i in range(len(route) - 1):
        total_distance += distance_matix[route[i], route[i + 1]]

    return total_distance


def brute_force(distances, locations):
    min_distance = 999999999

    next_perm = permutations(list(locations)[1:])

    print(f"Num permutations: {math.factorial(len(locations) - 1)}")

    for current_route in next_perm:
        full_route = [0] + list(current_route) + [0]

        # print(f"Permutation: {full_route}")

        current_distance = calc_fitness_score(distances, full_route)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = full_route

    print(f"Minimum distance: {min_distance} - best route: {best_route}")


# Kick off the GA...
number_locations = 6
distances = Distances.load_matrix(number_locations)
locations = list(Locations.locations)[:number_locations]
ga(distances, locations)
brute_force(distances, locations)
