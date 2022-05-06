import random
from tabulate import tabulate


CLUB_LIMITS = {"driver": 200, "wood": 175,
               "iron": 75, "wedge": 45, "putter": 1, "exit": 0}

yards_to_hole = [279, 188, 111, 162, 275, 308, 108, 171, 183]


def choose_club(yards_remaining):
    global CLUB_LIMITS
    print("You have", yards_remaining,
          "yards remaining. Which club do you wish to use?")
    for club in CLUB_LIMITS:
        if yards_remaining >= CLUB_LIMITS[club]:
            print(club)

    club = input("Choose one of the above clubs: ")
    club = club.lower()
    if club not in CLUB_LIMITS:
        raise Exception("Invalid club. Please choose again.")
    if CLUB_LIMITS[club] > yards_remaining:
        raise Exception("This club is not valid for yards remaining.")
    return club


def swing(club, yards_remaining):
    # return yards_remaining
    global CLUB_LIMITS
    limit = CLUB_LIMITS[club]
    if club == "driver":
        return random.randint(limit, min(yards_remaining, 325))
    elif club == "wood":
        return random.randint(limit, min(yards_remaining, 225))

    elif club == "iron":
        return random.randint(limit, min(yards_remaining, 201))
    elif club == "wedge":
        return random.randint(limit, yards_remaining)
    elif club == "putter":
        return random.randint(limit, yards_remaining)
    else:
        #print("Invalid club.")
        raise Exception("Invalid club")


play = input(
    "Welcome to Holy Grail Golf Course! To play you will choose a club - Driver (180 - 325 yds), Wood (125 - 250) Iron (75 - 200 yds), or Putter (1 - 25 yds). Are you ready to tee off? ").lower()

scorecard = [["Hole", 1, 2, 3, 4, 5, 6, 7, 8, 9, "Total"],
             ["Par", 4, 3, 3, 3, 4, 4, 3, 3, 4, 28], ["Swings"]]

for hole in range(9):

    print(tabulate(scorecard))
    swing_count = 0
    yards_remaining = yards_to_hole[hole]
    print("On hole", hole + 1)
    while yards_remaining > 0:
        try:
            club = choose_club(yards_remaining)
            if club == "exit":
                exit()

            yards_shot = swing(club, yards_remaining)
        except Exception as e:
            print(e)
            continue
        swing_count += 1
        yards_remaining = yards_remaining - yards_shot

    scorecard[2].append(swing_count)

total = int(scorecard[2][1]) + int(scorecard[2][2]) + int(scorecard[2][3]) + int(scorecard[2][4]) + int(
    scorecard[2][5]) + int(scorecard[2][6]) + int(scorecard[2][7]) + int(scorecard[2][8]) + int(scorecard[2][9])
print("Your final score: ")
scorecard[2].append(total)
print(tabulate(scorecard))
