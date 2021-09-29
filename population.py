import sys
import copy
import logging
import random
from types import GeneratorType
from locations import Locations
from distances import Distances
import reporting
import mutations

from solution import Solution
from itertools import permutations
import math
import numpy as np

import time


POPULATION_SIZE = 10000
MAX_GENERATIONS = 5000
NUMBER_OUTPUT_LINKS = 10
ELITISM_PERCENT = 2
MUTATION_PERCENT = 20

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
    fittest_solution_per_generation = []

    with open("results/generation_results.csv", "w") as results:
        results.write(
            "Generation\tAverage Distance\tStandard Deviation\tLongest\tShortest\tRoute\n"
        )

    population = create_population(POPULATION_SIZE, locations)
    logging.info(f" Population size: {len(population)}")

    try:
        for generation_number in range(MAX_GENERATIONS):
            calculate_population_fitness(distance_matix, population)
            current_fittest = min(population, key=lambda c: c.fitness_score)
            fittest_solution_per_generation.append(current_fittest)

            population = create_next_generation(population)

            output_generation_results(generation_number, population, current_fittest)
    except KeyboardInterrupt:
        pass

    add_optimum_solution(fittest_solution_per_generation, distance_matix)

    output_final_results(fittest_solution_per_generation)


def add_optimum_solution(solutions, distance_matrix):
    # For testing. This is the optimum route for 14 locations
    # [0, 7, 8, 6, 5, 11, 10, 12, 13, 4, 9, 3, 1, 2, 0]
    # Elapsed time: 328069 seconds (3.8 days)
    #
    # Current best for 48 locations
    # 13130
    # [0, 21, 15, 40, 33, 13, 24, 47, 4, 28, 1, 25, 3, 34, 44, 9, 41, 23, 31, 38, 12, 20, 46, 10, 22, 2, 39, 14, 45, 32, 11, 19, 29, 42, 16, 26, 18, 36, 5, 27, 35, 6, 17, 43, 30, 37, 8, 7, 0]
    #
    # 13207 milwa
    # [0, 39, 14, 11, 10, 22, 12, 24, 13, 33, 2, 21, 15, 40, 28, 1, 25, 3, 34, 44, 23, 9, 41, 47, 4, 38, 31, 20, 46, 19, 32, 45, 35, 27, 5, 36, 18, 26, 16, 42, 29, 6, 17, 43, 30, 37, 8, 7, 0]

    # Add to solutions to display it for convenience
    optimum_solution = Solution([0, 7, 8, 6, 5, 11, 10, 12, 4, 9, 3, 1, 2, 0])
    optimum_solution.route = [
        0,
        21,
        15,
        40,
        33,
        13,
        24,
        47,
        4,
        28,
        1,
        25,
        3,
        34,
        44,
        9,
        41,
        23,
        31,
        38,
        12,
        20,
        46,
        10,
        22,
        2,
        39,
        14,
        45,
        32,
        11,
        19,
        29,
        42,
        16,
        26,
        18,
        36,
        5,
        27,
        35,
        6,
        17,
        43,
        30,
        37,
        8,
        7,
        0,
    ]
    optimum_solution.fitness_score = calc_fitness_score(
        distance_matrix, optimum_solution.route
    )
    solutions.insert(0, optimum_solution)


def calculate_population_fitness(distance_matix, population):
    #  Calculate the fitness of each solution
    for solution in population:
        solution.fitness_score = calc_fitness_score(distance_matix, solution.route)
        logging.debug(f" Solution: {solution.fitness_score}")


def create_next_generation(population):
    next_generation = get_elites(population)

    remaining_number = POPULATION_SIZE - len(next_generation)
    for _ in range(remaining_number // 2):
        parent1, parent2 = select_parents(population)
        child1, child2 = breed(parent1, parent2)
        child1 = mutations.mutate(child1, MUTATION_PERCENT)
        child2 = mutations.mutate(child2, MUTATION_PERCENT)
        next_generation.append(child1)
        next_generation.append(child2)
    return next_generation


def get_elites(population):
    # Keep this as an even number, makes pairing up for breeding easier
    number = (int(ELITISM_PERCENT / 100 * POPULATION_SIZE) // 2) * 2
    population.sort(key=lambda x: x.fitness_score)
    next_generation = population[:number]
    return next_generation


def output_generation_results(generation_number, population, current_fittest):
    fitness_scores = (x.fitness_score for x in population)
    fitness_array = np.array(list(fitness_scores))
    mean_score = np.mean(fitness_array)
    std_score = np.std(fitness_array)
    longest = fitness_array.max()
    shortest = fitness_array.min()

    print(
        f"Generation: {generation_number}, mean distance: {mean_score}, best distance: {shortest}"
    )
    with open("results/generation_results.csv", "a") as results:
        results.write(
            f"{generation_number}\t{mean_score}\t{std_score}\t{longest}\t{shortest}\t{current_fittest.route}\n"
        )


def output_final_results(solutions):
    routes = []
    counter = 0
    for sol in solutions[::OUTPUT_GENERATION_STEP]:
        print(
            f"Shortest path found {counter}: {sol.route} : {sol.fitness_score} : {sol}"
        )
        routes.append(sol.route)
        counter += 1

    print(f">>>> generating report")

    reporting.generate_report(solutions[::OUTPUT_GENERATION_STEP])


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
            print(f"New best route: {best_route}")

    print(f"Minimum distance: {min_distance} - best route: {best_route}")


if __name__ == "__main__":
    print(f"sys: {sys.argv}")
    print(f"{len(sys.argv)}")

    if len(sys.argv) < 2:
        print(f"Usage is: python population.py <num_locations>")
        exit()

    number_locations = int(sys.argv[1])

    # main(sys.argv[1:])

    # Kick off the GA...
    start_time = time.time()

    distances = Distances.load_matrix(number_locations)
    locations = list(Locations.locations)[:number_locations]

    ga(distances, locations)
    # brute_force(distances, locations)

    end_time = time.time()
    print(f"Elapsed time: {end_time-start_time}")
