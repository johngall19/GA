import numpy as np


class Locations:
    # locations = {
    #     0: "Concord, NH",
    #     1: "Hartford, CT",
    #     2: "Boston, MA",
    #     3: "Providence, RI",
    #     4: "Augusta, ME",
    #     5: "Montpelier, VT",
    # }

    # distances = np.array(
    #     [
    #         [0, 240, 114, 178, 226, 186],
    #         [240, 0, 164, 121, 415, 322],
    #         [114, 164, 0, 81, 259, 290],
    #         [178, 121, 81, 0, 340, 342],
    #         [226, 415, 259, 340, 0, 290],
    #         [186, 322, 290, 342, 290, 0],
    #     ]
    # )
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
    }

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
