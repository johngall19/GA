import random

child = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]


def mutation_swap(child):
    cell1 = random.randint(1, len(child) - 2)
    cell2 = random.randint(1, len(child) - 2)
    if cell1 == cell2:
        mutation_swap(child)
    child[cell1], child[cell2] = child[cell2], child[cell1]
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
    start_scramble = random.randint(1, len(child) - 1)
    end_scramble = random.randint(start_scramble, len(child) - 1)
    scrambled_part = child[start_scramble:end_scramble]

    random.shuffle(scrambled_part)

    child = child[0:start_scramble] + scrambled_part + child[end_scramble:]

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
            child = mutation_swap(child.route)
        elif variant == 1:
            child = mutation_invert(child.route)
        elif variant <= 20:
            child = mutation_scramble2(child.route)


print(child)
child = mutation_scramble2(child)
print(child)
