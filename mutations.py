import random


def mutation_swap(child):
    cell1 = random.randint(0, len(child) - 1)
    cell2 = random.randint(0, len(child) - 1)
    if cell1 == cell2:
        mutation_swap(child)
    child[cell1], child[cell2] = child[cell2], child[cell1]
    return child


def mutation_scramble(child):
    subset = []
    subsetSize = int(len(child) / 2)
    for _ in range(subsetSize):
        subset.append(child[_])
    random.shuffle(subset)
    for _ in range(subsetSize):
        child[_] = subset[_]
    return child


def mutated_invert(child):
    subsetSize = random.randint(int(len(child) / 3), int(len(child)))
    subset = []
    for _ in range(subsetSize):
        subset.append(child[_])
    subset.reverse()
    for _ in range(subsetSize):
        child[_] = subset[_]
    return child


def mutate(child):
    num = random.randint(0, 25)

    if num == 0:
        mutation_swap(child.route)
    elif num == 1:
        mutated_invert(child.route)
    elif num == 2:
        mutation_scramble(child.route)
