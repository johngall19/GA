import random

child = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
]


def mutation_mass_swap(child):
    odds = []
    evens = []
    mutant = []
    for gene in range(len(child)):
        if gene > 0 and gene < len(child) - 1:
            if child[gene] % 2 == 0:
                evens.append(child[gene])
            else:
                odds.append(child[gene])
    mutant.append(0)

    for gene in range(len(odds)):
        try:
            mutant.append(evens[gene])
        except:
            pass
        try:
            mutant.append(odds[gene])
        finally:
            pass
    mutant.append(0)
    return mutant


print(child)
print(mutation_mass_swap(child))


def mutation_swap(child):
    cell1 = random.randint(1, len(child) - 2)
    cell2 = random.randint(1, len(child) - 2)
    if cell1 == cell2:
        mutation_swap(child)
    child[cell1], child[cell2] = child[cell2], child[cell1]
    return child


def mutation_nextdoor_swap(child):
    gene1 = random.randint(1, len(child) - 3)
    gene2 = gene1 + 1
    child[gene1], child[gene2] = child[gene2], child[gene1]
    return child


def mutation_scramble(child):
    subset = []
    subsetSize = int(len(child) / 2)
    for _ in range(subsetSize):
        subset.append(child[_ + 1])
    random.shuffle(subset)
    for _ in range(subsetSize):
        child[_ + 1] = subset[_]

    return child


def mutation_scramble2(child):
    start_scramble = random.randint(1, len(child) - 3)
    end_scramble = random.randint(start_scramble + 1, len(child) - 2)
    scrambled_part = child[start_scramble : end_scramble + 1]

    random.shuffle(scrambled_part)

    child = child[0:start_scramble] + scrambled_part + child[end_scramble + 1 :]
    return child


def mutation_invert(child):
    subsetSize = random.randint(int(len(child) / 3), int(len(child) - 2))
    subset = []
    for _ in range(subsetSize):
        subset.append(child[_ + 1])
    subset.reverse()
    for _ in range(subsetSize):
        child[_ + 1] = subset[_]
    return child


def mutate(child, percentage):
    chance = random.randint(0, 100)
    if chance <= percentage:
        variant = random.randint(0, 20)
        if variant == 0:
            child.route = mutation_swap(child.route)
        elif variant == 1:
            child.route = mutation_invert(child.route)
        elif variant <= 7:
            child.route = mutation_mass_swap(child.route)
        elif variant <= 13:
            child.route = mutation_nextdoor_swap(child.route)
        elif variant <= 20:
            child.route = mutation_scramble2(child.route)

    return child


# print(child)
# child = mutation_scramble2(child)
# # child = mutation_nextdoor_swap(child)
# print(child)
