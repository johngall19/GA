import random

child = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Swap Mutation
# In swap mutation, we select two positions on the chromosome at random, and interchange the values.
def mutation_swap(child):
    cell1 = random.randint(0, len(child) - 1)
    cell2 = random.randint(0, len(child) - 1)
    if cell1 == cell2:
        mutation_swap(child)
    child[cell1], child[cell2] = child[cell2], child[cell1]
    return child


# Scramble Mutation
# A subset of genes is chosen and their values are scrambled or shuffled randomly.
def mutation_scramble(child):
    subset = []
    subsetSize = int(len(child) / 2)
    for _ in range(subsetSize):
        subset.append(child[_])
    random.shuffle(subset)
    for _ in range(subsetSize):
        child[_] = subset[_]
    return child


# Inversion Mutation
# Select a subset of genes like in scramble mutation, but instead of shuffling the subset, we invert the entire string in the subset.
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

    # switch(num):
    #     case 0: mutation_swap(child)
    #     break
    #     case 1: mutation_scramble(child)
    #     break
    #     case 2: mutated_invert(child)
    #     break
    # switch statement to pick random mutation


print(f"Original... \n{child}")
print(f"Swapped...\n{mutation_swap(child)}")
print(f"Scrambled...\n{mutation_scramble(child)}")
print(f"Inverted...\n{mutated_invert(child)}")
