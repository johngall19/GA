from locations import Locations
import random


class Solution(object):
    def __init__(self):
        self.fitness_score = 0
        num_locations = len(Locations.locations)

        locations = list(range(1, num_locations))
        random.shuffle(locations)

        # Always start and finish at location 0
        self.route = [0] + locations + [0]
        print(f"Route: {self.route}")
