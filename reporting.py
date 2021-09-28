import urllib
from locations import Locations
from solution import Solution

MAX_LOCATIONS_PER_MAP = 24

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
        {1}
        </div>
        <div class= "map-table">
            <table class="map-table">
                <tr>
                    <th>Map with Distance</th>
                </tr>
                <tr>
                    <td>{0}</td>
                </tr>
            </table>
        </div>
    </div>
</body>
"""

LINK = """
    <p><a href= {0} target="_blank">Map {1} Distance {2}</a></p>
"""

iframe_url_parts = {
    0: "Montgomery%2C%20Alabama!3m2!1d32.3792233!2d-86.3077368!4m5!1s0x876b80aa231f17cf%3A0x118ef4f8278a36d6!2s",
    1: "Phoenix%2C%20Arizona!3m2!1d33.4483771!2d-112.0740373!4m5!1s0x809ac672b28397f9%3A0x921f6aaa74197fdb!2s",
    2: "Little%20Rock%2C%20Arkansas!3m2!1d34.7464809!2d-92.28959479999999!4m5!1s0x872b12ed50a179cb%3A0x8c69c7f8354a1bac!2s",
    3: "Sacramento%2C%20California!3m2!1d38.5815719!2d-121.4943996!4m5!1s0x54aef172e947b49d%3A0x9a5b989b36679d9b!2s",
    4: "Denver%2C%20Colorado!3m2!1d39.739235799999996!2d-104.990251!4m5!1s0x87ee99a4c1611ee7%3A0x710028512691e4b2!2s",
    5: "Hartford%2C%20Connecticut!3m2!1d41.7658043!2d-72.6733723!4m5!1s0x89c7633375685ead%3A0xa9e2e447fb006cf0!2s",
    6: "Dover%2C%20Delaware!3m2!1d39.158167999999996!2d-75.5243682!4m5!1s0x872b12ed50a179cb%3A0x8c69c7f8354a1bac!2s",
    7: "Tallahassee%2C%20Florida!3m2!1d30.438255899999998!2d-84.28073289999999!4m5!1s0x88f5045d6993098d%3A0x66fede2f990b630b!2s",
    8: "Atlanta%2C%20Georgia!3m2!1d33.7489954!2d-84.3879824!4m5!1s0x89e65311f21151a5%3A0xcc8e4aa8e97d5999!2s",
    9: "Boise%2C%20Idaho!3m2!1d43.6150186!2d-116.20231369999999!4m5!1s0x5343510fedc7db4d%3A0x214c1d71e3fdf714!2s",
    10: "Springfield%2C%20Illinois!3m2!1d39.7817213!2d-89.6501481!4m5!1s0x87db5dab4e3b0af1%3A0xb2e7c94bbca8d9ad!2s",
    11: "Indianapolis%2C%20Indiana!3m2!1d39.768403!2d-86.158068!4m5!1s0x87d2a134a11f569b%3A0x3405f5100df35b17!2s",
    12: "Des%20Moines%2C%20Iowa!3m2!1d41.5868353!2d-93.6249593!4m5!1s0x86243867325f74cb%3A0x2123f1db91579a1d!2s",
    13: "Topeka%2C%20Kansas!3m2!1d39.0473451!2d-95.67515759999999!4m5!1s0x87ee99a4c1611ee7%3A0x710028512691e4b2!2s",
    14: "Frankfort%2C%20Kentucky%2040601!3m2!1d38.2009055!2d-84.8732835!4m5!1s0x89e65311f21151a5%3A0xcc8e4aa8e97d5999!2s",
    15: "Baton%20Rouge%2C%20Louisiana!3m2!1d30.4514677!2d-91.18714659999999!4m5!1s0x54aef172e947b49d%3A0x9a5b989b36679d9b!2s",
    16: "Augusta%2C%20Maine%2004330!3m2!1d44.3106241!2d-69.7794897!4m5!1s0x886b50ffa7796a03%3A0xd68e9df640b9ea7c!2s",
    17: "Annapolis%2C%20Maryland!3m2!1d38.9784453!2d-76.4921829!4m5!1s0x8875391d24dbd177%3A0xe72c82eecca86d22!2s",
    18: "Boston%2C%20Massachusetts!3m2!1d42.3600825!2d-71.0588801!4m5!1s0x88f5045d6993098d%3A0x66fede2f990b630b!2s",
    19: "Lansing%2C%20Michigan!3m2!1d42.732535!2d-84.5555347!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff!2s",
    20: "St%20Paul%2C%20Minnesota!3m2!1d44.953702899999996!2d-93.0899578!4m5!1s0x8842734c8b1953c9%3A0x536418a08867425c!2s",
    21: "Jackson%2C%20Mississippi!3m2!1d32.2987573!2d-90.1848103!4m5!1s0x87bf02e4daec7a29%3A0xbe2be7d06ae3a7f0!2s",
    22: "Jefferson%20City%2C%20Missouri!3m2!1d38.5767017!2d-92.1735164!4m5!1s0x886b50ffa7796a03%3A0xd68e9df640b9ea7c!2s",
    23: "Helena%2C%20Montana!3m2!1d46.5891452!2d-112.0391057!4m5!1s0x876b80aa231f17cf%3A0x118ef4f8278a36d6!2s",
    24: "Lincoln%2C%20Nebraska!3m2!1d40.813615999999996!2d-96.7025955!4m5!1s0x89de0a34cc4ffb4b%3A0xe1a16312a0e728c4!2s",
    25: "Carson%20City%2C%20Nevada!3m2!1d39.1637984!2d-119.76740339999999!4m5!1s0x88f8a5697931d1e3%3A0xf32808f4b379fa96!2s",
    26: "Concord%2C%20New%20Hampshire!3m2!1d43.208136599999996!2d-71.5375718!4m5!1s0x89e444e0437e735d%3A0x69df7c4d48b3b627!2s",
    27: "Trenton%2C%20New%20Jersey!3m2!1d40.2205824!2d-74.759717!4m5!1s0x89e26a96154a8917%3A0x5a871a0a62528f1!2s",
    28: "Santa%20Fe%2C%20New%20Mexico!3m2!1d35.6869752!2d-105.937799!4m5!1s0x89c143482d3dbbb9%3A0xcf16567f895cd7bc!2s",
    29: "Albany%2C%20New%20York!3m2!1d42.6525793!2d-73.7562317!4m5!1s0x87185043e79852a9%3A0x8c902373fd88df40!2s",
    30: "Raleigh%2C%20North%20Carolina!3m2!1d35.779589699999995!2d-78.6381787!4m5!1s0x8644b599a0cc032f%3A0x5d9b464bd469d57a!2s",
    31: "Bismarck%2C%20North%20Dakota!3m2!1d46.808326799999996!2d-100.7837392!4m5!1s0x884f2cce88145d39%3A0x7661a84704c91b0b!2s",
    33: "Oklahoma%20City%2C%20Oklahoma!3m2!1d35.4675602!2d-97.5164276!4m5!1s0x80990aa1f8deb471%3A0xf79c6c82bde23828!2s",
    34: "Salem%2C%20Oregon!3m2!1d44.9428975!2d-123.03509629999999!4m5!1s0x8806536d3a2019ff%3A0x4e0cfcb5ba484198!2s",
    35: "Harrisburg%2C%20Pennsylvania!3m2!1d40.2731911!2d-76.8867008!4m5!1s0x8796be59ca561265%3A0x633a859b1fd5deb9!2s",
    36: "Providence%2C%20Rhode%20Island!3m2!1d41.8239891!2d-71.4128343!4m5!1s0x876f38762e73ef93%3A0xb10a30418f972d2b!2s",
    37: "Columbia%2C%20South%20Carolina!3m2!1d34.000710399999996!2d-81.0348144!4m5!1s0x54bffefcbc4b9c63%3A0xf93429e08f0357c2!2s",
    38: "Pierre%2C%20South%20Dakota%2057501!3m2!1d44.366787599999995!2d-100.3537522!4m5!1s0x8864ec3213eb903d%3A0x7d3fb9d0a1e9daa0!2s",
    39: "Nashville%2C%20Tennessee!3m2!1d36.1626638!2d-86.7816016!4m5!1s0x883889c1b990de71%3A0xe43266f8cfb1b533!2s",
    40: "Austin%2C%20Texas!3m2!1d30.267152999999997!2d-97.7430608!4m5!1s0x87ad8a547ef8d281%3A0x33a21274d14f3a9d!2s",
    41: "Salt%20Lake%20City%2C%20Utah!3m2!1d40.760779299999996!2d-111.89104739999999!4m5!1s0x4cb5a78cc44dea05%3A0x4891e094ceb5836!2s",
    42: "Montpelier%2C%20Vermont%2005602!3m2!1d44.260059299999995!2d-72.5753869!4m5!1s0x89ac5a2f9f51e0f7%3A0x6790b6528a11f0ad!2s",
    43: "Richmond%2C%20Virginia!3m2!1d37.5407246!2d-77.4360481!4m5!1s0x5491c9c1ae285569%3A0x4f146197e2881b83!2s",
    44: "Olympia%2C%20Washington!3m2!1d47.037874099999996!2d-122.9006951!4m5!1s0x87523d9488d131ed%3A0x5b53b7a0484d31ca!2s",
    45: "Charleston%2C%20West%20Virginia!3m2!1d38.349819499999995!2d-81.6326234!4m5!1s0x89c8c116b8079e97%3A0xbb6e42c8128d46d5!2s",
    46: "Madison%2C%20Wisconsin!3m2!1d43.0730517!2d-89.4012302!4m5!1s0x52d7831257d8e963%3A0xccaabd12f9bbca93!2s",
    47: "Cheyenne%2C%20Wyoming!3m2!1d41.139981399999996!2d-104.8202462!4m5!1s0x52d54a64b288f891%3A0x9e9950165931af92!2s",
}

URL_IFRAME = '<iframe src="https://www.google.com/maps/embed?'
URL_PB = "pb=!1m{}!1m12!1m3!1d6611040.563108434!2d-100.14363041075251!3d35.994714528137486!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m{}!3e6!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff!2s"
LAST_LOCATION = '!5e0!3m2!1sen!2sus!4v1632504621988!5m2!1sen!2sus"'
URL_END = ' width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>'


def build_iframe(solution=None):
    END_TOKEN = "!4m"

    # route = [0, 2, 1, 3, 9, 4, 13, 12, 10, 11, 5, 6, 8, 7, 0]
    route = solution.route

    iframe_url = URL_IFRAME + URL_PB.format(16 + len(route) * 6, 1 + len(route) * 6)

    for location in route:
        url = iframe_url_parts[location]
        print(f"Url_part: {url}")
        iframe_url += url

    #  split the last !4m
    truncate_point = iframe_url.rfind(END_TOKEN)
    iframe_url = iframe_url[:truncate_point]

    iframe_url += LAST_LOCATION
    iframe_url += URL_END

    print("My iframe link {}".format(iframe_url))
    return iframe_url


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
        # Google maps has a limit to the number of locations it will display.
        # Chunk the route up in to parts if required.
        chunks = [
            solution.route[x : x + MAX_LOCATIONS_PER_MAP + 1]
            for x in range(0, len(solution.route), MAX_LOCATIONS_PER_MAP)
        ]

        for chunk in chunks:
            links += LINK.format(build_url(chunk), counter, solution.fitness_score)

        counter += 1

    # print(f"Links: {links}")

    report = HEADERS + BODY.format(links, build_iframe(solutions[-1]))

    print(f"Report: {report}")

    f = open("results/result.html", "w")
    f.write(report)
    f.close()
