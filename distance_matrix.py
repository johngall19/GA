import requests
import numpy as np
import pickle

locations = {
    0: "Montgomery, AL",
    1: "Phoenix, AZ",
    2: "Little Rock, AR",
    3: "Sacramento, CA",
    4: "Denver, CO",
    5: "Hartford, CT",
    6: "Dover, DE",
    7: "Tallahassee, FL",
    8: "Atlanta, GA",
    9: "Boise, ID",
    10: "Springfield, IL",
    11: "Indianapolis, IN",
    12: "Des Moines, IA",
    13: "Topeka, KS",
    14: "Frankfort, KY",
    15: "Baton Rouge, LA",
    16: "Augusta, ME",
    17: "Annapolis, MD",
    18: "Boston, MA",
    19: "Lansing, MI",
    20: "St. Paul, MN",
    21: "Jackson, MS",
    22: "Jefferson City, MO",
    23: "Helena, MT",
    24: "Lincoln, NE",
    25: "Carson City, NV",
    26: "Concord, NH",
    27: "Trenton, NJ",
    28: "Santa Fe, NM",
    29: "Albany, NY",
    30: "Raleigh, NC",
    31: "Bismarck, ND",
    32: "Columbus, OH",
    33: "Oklahoma City, OK",
    34: "Salem, OR",
    35: "Harrisburg, PA",
    36: "Providence, RI",
    37: "Columbia, SC",
    38: "Pierre, SD",
    39: "Nashville, TN",
    40: "Austin, TX",
    41: "Salt Lake City, UT",
    42: "Montpelier, VT",
    43: "Richmond, VA",
    44: "Olympia, WA",
    45: "Charleston, WV",
    46: "Madison, WI",
    47: "Cheyenne, WY",
}
KEY = "bGGcGfEZdGoFkAUUEKmAdRAsE4tG94vb"


class DistanceMatrix:
    def generateMatrix(
        self, locations, maxSize=None, key="bGGcGfEZdGoFkAUUEKmAdRAsE4tG94vb"
    ):
        self.maxSize = maxSize
        self.locations = locations
        # initialise empty matrix
        if maxSize == None:
            maxSize = len(locations)
        matrix = [[0.0 for x in range(maxSize)] for y in range(maxSize)]
        # Converting from list to array
        DistancesMatrix = np.array(matrix)
        # Populate the matrix
        for i in locations:
            if i >= maxSize:
                break
            for y in locations:
                if y >= maxSize:
                    break
                else:
                    start = locations[i]
                    end = locations[y]
                    myResponse = requests.get(
                        f"http://open.mapquestapi.com/directions/v2/route?key={key}&from={start}&to={end}"
                    )
                    myResponseJson = myResponse.json()
                    distance = myResponseJson["route"]["distance"]
                    matrix[i][y] = distance
        matrix = np.array(matrix, dtype="i")
        return matrix

    def pickle_matrix(self, matrix, matrixName):
        filename = f"pickled_{matrixName}"
        outfile = open(filename, "wb")
        pickle.dump(matrix, outfile)
        outfile.close
