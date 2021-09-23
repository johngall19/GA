import requests
import numpy as np
from locations import Locations

# Display entire array rathern than truncated.
# import sys
# np.set_printoptions(threshold=sys.maxsize)


class Distances:
    KEY = "gJ32Me8WsAMAFwyEs5jmHFDSF7jcyYbg"

    def generate_matrix(self, locations=Locations.locations, key=KEY):
        self.locations = locations
        size = len(locations)
        matrix = [[0.0 for x in range(size)] for y in range(size)]
        matrix = np.array(matrix, dtype="i")
        for i in locations:
            for y in locations:
                start = locations[i]
                end = locations[y]
                myResponse = requests.get(
                    f"http://open.mapquestapi.com/directions/v2/route?key={key}&from={start}&to={end}"
                )
                myResponseJson = myResponse.json()
                distance = myResponseJson["route"]["distance"]
                matrix[i][y] = distance
        return matrix

    def save_matrix(self, matrix, matrixName):
        with open(matrixName + ".npy", "wb") as f:
            np.save(f, matrix)

    def load_matrix(self, size=48):
        # Sample distances array, until npy file available
        distances = np.array(
            [
                [0, 1712, 463, 2424, 1420, 1171, 893, 209, 160, 2241],
                [1796, 0, 1343, 754, 821, 2585, 2414, 1885, 1853, 1043],
                [462, 1345, 0, 1971, 966, 1353, 1106, 669, 518, 1788],
                [2423, 755, 1970, 0, 1182, 2924, 2812, 2630, 2521, 714],
                [1419, 821, 966, 1179, 0, 1880, 1749, 1626, 1402, 831],
                [1168, 2585, 1351, 2920, 1880, 0, 283, 1217, 1001, 2572],
                [891, 2415, 1104, 2810, 1751, 280, 0, 965, 732, 2462],
                [207, 1886, 670, 2631, 1627, 1210, 967, 0, 268, 2449],
                [160, 1854, 519, 2522, 1405, 1004, 734, 268, 0, 2174],
                [2240, 1044, 1788, 713, 830, 2572, 2460, 2448, 2169, 0],
            ]
        )

        # distances = np.load("np-distances.npy")
        return distances[:size, :size]


# # # Testing # # #
# dm = DistanceMatrix()
# # #  x = dm.generate_matrix()
# print(x)
# myMatrix = dm.load_matrix()
# print(dm.load_matrix(3))
# dm.save_matrix(myMatrix, "newesttt")
# print(Locations.locations)
