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
# <div>
# <iframe src="https://www.google.com/maps/embed?pb=!1m166!1m12!1m3!1d12721591.723851744!2d-100.83682709597703!3d38.88150532125363!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m151!3e6!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff!2sMontgomery%2C%20Alabama!3m2!1d32.3792233!2d-86.3077368!4m5!1s0x86243867325f74cb%3A0x2123f1db91579a1d!2sBaton%20Rouge%2C%20Louisiana!3m2!1d30.4514677!2d-91.18714659999999!4m5!1s0x4cb200fdafacc49d%3A0x79a3488d64220b2d!2sAugusta%2C%20Maine%2004330!3m2!1d44.3106241!2d-69.7794897!4m5!1s0x89c7633375685ead%3A0xa9e2e447fb006cf0!2sDover%2C%20Delaware!3m2!1d39.158167999999996!2d-75.5243682!4m5!1s0x89b7f66570672fd5%3A0x43f854fdd3a8274b!2sAnnapolis%2C%20Maryland!3m2!1d38.9784453!2d-76.4921829!4m5!1s0x89e65311f21151a5%3A0xcc8e4aa8e97d5999!2sHartford%2C%20Connecticut!3m2!1d41.7658043!2d-72.6733723!4m5!1s0x89e3652d0d3d311b%3A0x787cbf240162e8a0!2sBoston%2C%20Massachusetts!3m2!1d42.3600825!2d-71.0588801!4m5!1s0x8822c01c7f318c37%3A0x4378b62389029d9e!2sLansing%2C%20Michigan!3m2!1d42.732535!2d-84.5555347!4m5!1s0x8875391d24dbd177%3A0xe72c82eecca86d22!2sSpringfield%2C%20Illinois!3m2!1d39.7817213!2d-89.6501481!4m5!1s0x886b50ffa7796a03%3A0xd68e9df640b9ea7c!2sIndianapolis%2C%20Indiana!3m2!1d39.768403!2d-86.158068!4m5!1s0x87ee99a4c1611ee7%3A0x710028512691e4b2!2sDes%20Moines%2C%20Iowa!3m2!1d41.5868353!2d-93.6249593!4m5!1s0x87db5dab4e3b0af1%3A0xb2e7c94bbca8d9ad!2sJefferson%20City%2C%20Missouri!3m2!1d38.5767017!2d-92.1735164!4m5!1s0x87bf02e4daec7a29%3A0xbe2be7d06ae3a7f0!2sTopeka%2C%20Kansas!3m2!1d39.0473451!2d-95.67515759999999!4m5!1s0x809ac672b28397f9%3A0x921f6aaa74197fdb!2sSacramento%2C%20California!3m2!1d38.5815719!2d-121.4943996!4m5!1s0x5343510fedc7db4d%3A0x214c1d71e3fdf714!2sHelena%2C%20Montana!3m2!1d46.5891452!2d-112.0391057!4m5!1s0x54aef172e947b49d%3A0x9a5b989b36679d9b!2sBoise%2C%20Idaho!3m2!1d43.6150186!2d-116.20231369999999!4m5!1s0x52b2d4cee4e9379f%3A0xc87291d23fda2e29!2sSt%20Paul%2C%20Minnesota!3m2!1d44.953702899999996!2d-93.0899578!4m5!1s0x8842734c8b1953c9%3A0x536418a08867425c!2sFrankfort%2C%20Kentucky%2040601!3m2!1d38.2009055!2d-84.8732835!4m5!1s0x86282b7f90741b21%3A0x713cde441f038a0!2sJackson%2C%20Mississippi!3m2!1d32.2987573!2d-90.1848103!4m5!1s0x876b80aa231f17cf%3A0x118ef4f8278a36d6!2sDenver%2C%20Colorado!3m2!1d39.739235799999996!2d-104.990251!4m5!1s0x872b12ed50a179cb%3A0x8c69c7f8354a1bac!2sPhoenix%2C%20Arizona!3m2!1d33.4483771!2d-112.0740373!4m5!1s0x87d2a134a11f569b%3A0x3405f5100df35b17!2sLittle%20Rock%2C%20Arkansas!3m2!1d34.7464809!2d-92.28959479999999!4m5!1s0x88ec8a5187124b53%3A0xebee077ad4fdb1f8!2sTallahassee%2C%20Florida!3m2!1d30.438255899999998!2d-84.28073289999999!4m5!1s0x88f5045d6993098d%3A0x66fede2f990b630b!2sAtlanta%2C%20Georgia!3m2!1d33.7489954!2d-84.3879824!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff!2sMontgomery%2C%20Alabama!3m2!1d32.3792233!2d-86.3077368!5e0!3m2!1sen!2sus!4v1632479255379!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
# </div>

BODY = """
<body>
    <div>
    {1}
    </div>
 {0}
</body>
"""

LINK = """
    <p><a href= {0}>Map {1} Distance {2}</a></p>
"""

# url1 = 'https://www.google.com/maps/embed?pb=!1m82!1m12!1m3!1d13801327.904657999!2d-106.26294180727534!3d31
# .095728998803047!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m67!3e6!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff


# !2sMontgomery%2C%20Alabama!3m2!1d32.3792233!2d-86.3077368!4m5!1s0x872b12ed50a179cb%3A0x8c69c7f8354a1bac
# !2sPhoenix%2C%20Arizona!3m2!1d33.4483771!2d-112.0740373!4m5!1s0x809ac672b28397f9%3A0x921f6aaa74197fdb
# !2sSacramento%2C%20California!3m2!1d38.5815719!2d-121.4943996!4m5!1s0x54aef172e947b49d%3A0x9a5b989b36679d9b
# !2sBoise%2C%20Idaho!3m2
# !1d43.6150186!2d-116.20231369999999!4m5!1s0x876b80aa231f17cf%3A0x118ef4f8278a36d6!2sDenver%2C%20Colorado!3m2!1d39
# .739235799999996!2d-104.990251!4m5!1s0x87d2a134a11f569b%3A0x3405f5100df35b17!2sLittle%20Rock%2C%20Arkansas!3m2!1d34
# .7464809!2d-92.28959479999999!4m5!1s0x89e65311f21151a5%3A0xcc8e4aa8e97d5999!2sHartford%2C%20Connecticut!3m2!1d41
# .7658043!2d-72.6733723!4m5!1s0x89c7633375685ead%3A0xa9e2e447fb006cf0!2sDover%2C%20Delaware!3m2!1d39.158167999999996
# !2d-75.5243682!4m5!1s0x88f5045d6993098d%3A0x66fede2f990b630b!2sAtlanta%2C%20Georgia!3m2!1d33.7489954!2d-84.3879824
# !4m5!1s0x88ec8a5187124b53%3A0xebee077ad4fdb1f8!2sTallahassee%2C%20Florida!3m2!1d30.438255899999998!2d-84
# .28073289999999!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff!2sMontgomery%2C%20Alabama


# !3m2!1d32.3792233!2d-86.3077368!5e0!3m2!1sen!2sus!4v1632401398491!5m2!1sen!2sus'
# print(urlparse(url1))


# <iframe src="https://www.google.com/maps/embed?
# pb=!1m28!1m12!1m3!1d13711620.18693651!2d-108.18842199449227!3d32.96253140759906!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff!2s
# Montgomery%2C%20Alabama!3m2!1d32.3792233!2d-86.3077368!4m5!1s0x872b12ed50a179cb%3A0x8c69c7f8354a1bac!2s
# Phoenix%2C%20Arizona!3m2!1d33.4483771!2d-112.0740373!5e0!3m2!1sen!2sus!4v1632490868483!5m2!1sen!2sus"
#  width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>


# <iframe src="https://www.google.com/maps/embed?pb=!1m166!1m12!1m3!1d55065120.44059436!2d-131.95598368825355!3d32.60862901281424!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m151!3e6!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff!2s
# Montgomery%2C%20Alabama!3m2!1d32.3792233!2d-86.3077368!4m5!1s0x89c7633375685ead%3A0xa9e2e447fb006cf0!2s
# Dover%2C%20Delaware!3m2!1d39.158167999999996!2d-75.5243682!4m5!1s0x872b12ed50a179cb%3A0x8c69c7f8354a1bac!2s
# Phoenix%2C%20Arizona!3m2!1d33.4483771!2d-112.0740373!4m5!1s0x809ac672b28397f9%3A0x921f6aaa74197fdb!2s
# Sacramento%2C%20California!3m2!1d38.5815719!2d-121.4943996!4m5!1s0x54aef172e947b49d%3A0x9a5b989b36679d9b!2s
# Boise%2C%20Idaho!3m2!1d43.6150186!2d-116.20231369999999!4m5!1s0x5343510fedc7db4d%3A0x214c1d71e3fdf714!2s
# Helena%2C%20Montana!3m2!1d46.5891452!2d-112.0391057!4m5!1s0x876b80aa231f17cf%3A0x118ef4f8278a36d6!2s
# Denver%2C%20Colorado!3m2!1d39.739235799999996!2d-104.990251!4m5!1s0x87db5dab4e3b0af1%3A0xb2e7c94bbca8d9ad!2s
# Jefferson%20City%2C%20Missouri!3m2!1d38.5767017!2d-92.1735164!4m5!1s0x886b50ffa7796a03%3A0xd68e9df640b9ea7c!2s
# Indianapolis%2C%20Indiana!3m2!1d39.768403!2d-86.158068!4m5!1s0x87d2a134a11f569b%3A0x3405f5100df35b17!2sLittle%20Rock%2C%20Arkansas!3m2!1d34.7464809!2d-92.28959479999999!4m5!1s0x87bf02e4daec7a29%3A0xbe2be7d06ae3a7f0!2sTopeka%2C%20Kansas!3m2!1d39.0473451!2d-95.67515759999999!4m5!1s0x52b2d4cee4e9379f%3A0xc87291d23fda2e29!2sSt%20Paul%2C%20Minnesota!3m2!1d44.953702899999996!2d-93.0899578!4m5!1s0x87ee99a4c1611ee7%3A0x710028512691e4b2!2sDes%20Moines%2C%20Iowa!3m2!1d41.5868353!2d-93.6249593!4m5!1s0x89e3652d0d3d311b%3A0x787cbf240162e8a0!2sBoston%2C%20Massachusetts!3m2!1d42.3600825!2d-71.0588801!4m5!1s0x89e65311f21151a5%3A0xcc8e4aa8e97d5999!2sHartford%2C%20Connecticut!3m2!1d41.7658043!2d-72.6733723!4m5!1s0x4cb200fdafacc49d%3A0x79a3488d64220b2d!2sAugusta%2C%20Maine%2004330!3m2!1d44.3106241!2d-69.7794897!4m5!1s0x89b7f66570672fd5%3A0x43f854fdd3a8274b!2sAnnapolis%2C%20Maryland!3m2!1d38.9784453!2d-76.4921829!4m5!1s0x8842734c8b1953c9%3A0x536418a08867425c!2sFrankfort%2C%20Kentucky%2040601!3m2!1d38.2009055!2d-84.8732835!4m5!1s0x8875391d24dbd177%3A0xe72c82eecca86d22!2sSpringfield%2C%20Illinois!3m2!1d39.7817213!2d-89.6501481!4m5!1s0x8822c01c7f318c37%3A0x4378b62389029d9e!2sLansing%2C%20Michigan!3m2!1d42.732535!2d-84.5555347!4m5!1s0x86282b7f90741b21%3A0x713cde441f038a0!2sJackson%2C%20Mississippi!3m2!1d32.2987573!2d-90.1848103!4m5!1s0x86243867325f74cb%3A0x2123f1db91579a1d!2sBaton%20Rouge%2C%20Louisiana!3m2!1d30.4514677!2d-91.18714659999999!4m5!1s0x88ec8a5187124b53%3A0xebee077ad4fdb1f8!2sTallahassee%2C%20Florida!3m2!1d30.438255899999998!2d-84.28073289999999!4m5!1s0x88f5045d6993098d%3A0x66fede2f990b630b!2sAtlanta%2C%20Georgia!3m2!1d33.7489954!2d-84.3879824!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff!2sMontgomery%2C%20Alabama!3m2!1d32.3792233!2d-86.3077368!5e0!3m2!1sen!2sus!4v1632491652516!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>

iframe_url_parts = {
    0: "Montgomery%2C%20Alabama!3m2!1d32.3792233!2d-86.3077368!4m5!1s0x876b80aa231f17cf%3A0x118ef4f8278a36d6!2s",
    1: "Phoenix%2C%20Arizona!3m2!1d33.4483771!2d-112.0740373!4m5!1s0x809ac672b28397f9%3A0x921f6aaa74197fdb!2s",
    3: "Sacramento%2C%20California!3m2!1d38.5815719!2d-121.4943996!4m5!1s0x54aef172e947b49d%3A0x9a5b989b36679d9b!2s",
    4: "Denver%2C%20Colorado!3m2!1d39.739235799999996!2d-104.990251!4m5!1s0x87ee99a4c1611ee7%3A0x710028512691e4b2!2s",
    6: "Dover%2C%20Delaware!3m2!1d39.158167999999996!2d-75.5243682!4m5!1s0x872b12ed50a179cb%3A0x8c69c7f8354a1bac!2s",
    9: "Boise%2C%20Idaho!3m2!1d43.6150186!2d-116.20231369999999!4m5!1s0x5343510fedc7db4d%3A0x214c1d71e3fdf714!2s",
    11: "Indianapolis%2C%20Indiana!3m2!1d39.768403!2d-86.158068!4m5!1s0x87d2a134a11f569b%3A0x3405f5100df35b17!2s",
    22: "Jefferson%20City%2C%20Missouri!3m2!1d38.5767017!2d-92.1735164!4m5!1s0x886b50ffa7796a03%3A0xd68e9df640b9ea7c!2s",
    23: "Helena%2C%20Montana!3m2!1d46.5891452!2d-112.0391057!4m5!1s0x876b80aa231f17cf%3A0x118ef4f8278a36d6!2s",
}

URL_IFRAME = '<iframe src="https://www.google.com/maps/embed?'
URL_PB = "pb=!1m{}!1m12!1m3!1d6611040.563108434!2d-100.14363041075251!3d35.994714528137486!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m{}!3e6!4m5!1s0x888e8194b0d481f9%3A0x8e1b511d354285ff!2s"
LAST_LOCATION = '!5e0!3m2!1sen!2sus!4v1632504621988!5m2!1sen!2sus"'
URL_END = ' width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>'


def build_iframe(solution=None):
    END_TOKEN = "!4m"

    route = [0, 4, 9, 6, 11]
    # route = solution.route

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
    counter = 0
    for solution in solutions:
        links += LINK.format(build_url(solution.route), counter, solution.fitness_score)
        counter += 1

    # print(f"Links: {links}")

    report = HEADERS + BODY.format(links, build_iframe(solutions[-1]))

    print(f"Report: {report}")

    f = open("results/result.html", "w")
    f.write(report)
    f.close()
