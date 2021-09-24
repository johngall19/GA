import urllib
from locations import Locations
from solution import Solution

us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

HEADERS = """
<!DOCTYPE html>
<html>

<head>
    <title>GA Results</title>
    <style>
    body {
        margin: 0;
        padding: 0;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        color: #060;
    }
    header {
        background-color: #DFB887;
        height: 35px;
        width: 100%;
        opacity: .9;
        margin-bottom: 10px;
    }
    
    header h1.logo {
    margin: 0;
    font-size: 1.7em;
    color: #060;
    text-transform: uppercase;
    float: left;
  }

  header h1.logo:hover {
    color: #fff;
    text-decoration: none;
  }
    
    .container {
        width: 1200px;
        margin: 0 auto;
    }
    .map-table {
        margin: 1em 0;
        min-width: 300px;
    }
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 50%;
    }
    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }
    tr:nth-child(odd) {
        background-color: #dddddd;
    }
    </style>
</head>
"""
BODY = """
<body>
 <header>
      <div class="container">
        <h1 class="logo">Genetic Algorithms</h1>
        </div>
    </header>
    <div class="container">
        <div>
            <iframe src="https://www.google.com/maps/embed?pb=Montgomery%2C%20Alabama%2C%20USA%2C%20Dover%2C%20Delaware%2C%20USAHartford%2C%20Connecticut%2C%20USA%2C%20Denver%2C%20Colorado%2C%20USA%2C%20Boise%2C%20Idaho%2C%20USA%2C%20Sacramento%2C%20California%2C%20USA%2C%20Phoenix%2C%20Arizona%2C%20USA%2C%20Little%20Rock%2C%20Arkansas%2C%20USA%2C%20Atlanta%2C%20Georgia%2C%20USA%2C%20Tallahassee%2C%20Florida%2C%20USA%2C%20Montgomery%2C%20Alabama%2C%20USA" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
        <div class= "map-table">
            <table class="map-table">
                <tr>
                    <th>Map and Distance</th>
                </tr>
                <tr>
                    <td>{0}</td>
                </tr>
            </table>
        </div>
</body>
"""

LINK = """
    <p><a href= {0} target="_blank">Map {1} Distance {2}</a></p>
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
    counter = 1
    for solution in solutions:
        links += LINK.format(build_url(solution.route), counter, solution.fitness_score)
        counter += 1

    # print(f"Links: {links}")

    report = HEADERS + BODY.format(links)

    f = open("results/result.html", "w")
    f.write(report)
    f.close()
