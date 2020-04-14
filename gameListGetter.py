import sys
# import library to parse HTML from page
from bs4 import BeautifulSoup
# import library to query webpage of interest
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

gameSystem = sys.argv[1].lower()
# specifying page of interest
if gameSystem == "snes":
    gameWiki = "https://en.wikipedia.org/wiki/List_of_Super_Nintendo_Entertainment_System_games"  # noqa: E501
    totalColumns = 7
    tableNumber = 0
elif gameSystem == "gba":
    gameWiki = "https://en.wikipedia.org/wiki/List_of_Game_Boy_Advance_games"
    totalColumns = 6
    tableNumber = 2
elif gameSystem == "nes":
    gameWiki = "https://en.wikipedia.org/wiki/List_of_Nintendo_Entertainment_System_games"  # noqa: E501
    totalColumns = 5
    tableNumber = 0
elif gameSystem == "gamecube":
    gameWiki = "https://en.wikipedia.org/wiki/List_of_GameCube_games"
    totalColumns = 7
    tableNumber = 0
elif gameSystem == "n64":
    gameWiki = "https://en.wikipedia.org/wiki/List_of_Nintendo_64_games"
    totalColumns = 6
    tableNumber = 1
elif gameSystem == "ds":
    gameWiki = "https://en.wikipedia.org/wiki/List_of_Nintendo_DS_games"
    totalColumns = 8
    tableNumber = 0
elif gameSystem == "3ds":
    gameWiki = "https://en.wikipedia.org/wiki/List_of_Nintendo_3DS_games"
    totalColumns = 8
    tableNumber = 0
    gameSystem = "threeDs"
elif gameSystem == "ps2":
    gameWiki = "https://en.wikipedia.org/wiki/List_of_PlayStation_2_games"
    totalColumns = 7
    tableNumber = 0

# save the HTML of the site within the page variable
page = urllib2.urlopen(gameWiki)

# parse data from "page" and save to new variable "soup"
soup = BeautifulSoup(page)
# print(soup.prettify())
# pinpointing the location of the table and its contents
page_tables = soup.find_all("table", class_="wikitable")
game_table = page_tables[tableNumber]
# print(game_table.prettify())
# creating lists for each of the columns I know to be in my table.
A = []
# utilizing HTML tags for rows <tr> and elements <td> to iterate through each row of data and append data elements to their appropriate lists:  # noqa: E501
for row in game_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells) == totalColumns:  # Only extract table body not heading
        A.append(cells[0].find(text=True))
# convert all values from unicode to string
A = [x.encode('UTF8') for x in A]
gameListFile = open("GameLists\\" + gameSystem + "GameList.txt", "w")
for game in A:
    game = str(game)
    game = game[2:]
    game = game[:-1]
    gameListFile.write(str(game) + "\n")
gameListFile.close()
