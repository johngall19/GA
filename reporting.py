import urllib
from locations import Locations
from solution import Solution


HEADERS = """
<!DOCTYPE html>
<html>

<head>
    <title>GA Results</title>
</head>
"""
BODY = """
<body>
 {0}
</body>
"""

LINK = """
    <p><a href= {0}>Map {1} Distance {2}</a></p>
"""


def add_route(route):  # list of numbers
    # Build a url to display the map
    route.append(route)


def build_url(route):
    base_url = "https://www.google.com/maps/dir/"
    path = ""
    for loc in route:
        path += "{}/".format(Locations.locations[loc].replace(" ", "+"))
    final_destination = base_url + path
    return final_destination


def generate_report(solutions):
    # build HTML page with links to all the routes (URL to maps)
    # list of embedded links to route maps.
    links = ""
    counter = 0
    for solution in solutions:
        links += LINK.format(build_url(solution.route), counter, solution.fitness_score)
        counter += 1

    # print(f"Links: {links}")

    report = HEADERS + BODY.format(links)

    f = open("results/result.html", "w")
    f.write(report)
    f.close()
