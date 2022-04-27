

# from tabulate import tabulate
from tabulate import tabulate
import random
play = input(
    "Welcome to Holy Grail Golf Course! To play you will choose a club - Driver (180 - 325 yds), Wood (125 - 250) Iron (75 - 200 yds), or Putter (1 - 25 yds). Are you ready to tee off? ").lower()

table1 = [["Hole", 1, 2, 3, 4, 5, 6, 7, 8, 9, "Total"],
          ["Par", 4, 3, 3, 3, 4, 4, 3, 3, 4, 28], ["Swings"]]
print(tabulate(table1))

total = 0
while True:

    # Hole 1
    print("You have made your way to Hole 1: 279 Yds, Par 4")
    yards = 279

    def drive(yards):

        swing_count = 0
        club_choice = input(
            "Choose your club: Driver, Wood, Iron, or Exit ").lower()
        if club_choice == "driver":
            swing = random.randint(200, 325)
            yards = abs(yards - swing)
            swing_count = swing_count + 1
            print("You hit the ball", swing, "yards.")
            print(yards, "yards left")
        elif club_choice == "wood":
            swing = random.randint(175, 225)
            yards = abs(yards - swing)
            swing_count = swing_count + 1
            print("You hit the ball", swing, "yards.")
            print(yards, "yards left")
        elif club_choice == "iron":
            swing = random.randint(75, 201)
            yards = abs(yards - swing)
            swing_count = swing_count + 1
            print("You hit the ball", swing, "yards.")
            print(yards, "yards left")
        elif club_choice == "exit":
            exit()

        else:
            try_again = print("Invalid choice. ")
        while yards > 45:
            club_choice = input(
                "Choose your club: Wedge, Iron, or Exit. ").lower()
            if club_choice == "wedge":
                swing = random.randint(45, yards)
                yards = abs(yards - swing)
                swing_count = swing_count + 1
                print("You hit the ball", swing, "yards.")
                print(yards, "yards left")
            elif club_choice == "iron":
                swing = random.randint(45, yards)
                yards = abs(yards - swing)
                swing_count = swing_count + 1
                print("You hit the ball", swing, "yards.")
                print(yards, "yards left")
            elif club_choice == "exit":
                exit()
        while yards > 0:
            club_choice = input(
                "Choose your club: Iron, Putter, or Exit. ").lower()
            if club_choice == "iron":
                swing = random.randint(1, yards)
                yards = abs(yards - swing)

                swing_count = swing_count + 1
                print("You hit the ball", swing, "yards.")
                print(yards, "yards left")

            elif club_choice == "putter":
                swing = random.randint(1, yards)
                yards = abs(yards - swing)

                swing_count = swing_count + 1
                print("You hit the ball", swing, "yards.")
                print(yards, "yards left")
            elif club_choice == "exit":
                print("Thanks for playing")
                break

        while yards >= 15:
            if club_choice == "putter":
                swing = random.randint(1, yards)
                yards = abs(yards - swing)

                swing_count = swing_count + 1
                print("You hit the ball", swing, "yards.")
                print(yards, "yards left")
            elif club_choice == "exit":
                print("Thanks for playing")
                break

            else:
                print("Invalid choice.")
        global table1
        final_swing_count = swing_count
        print(final_swing_count, "swings")

        table1[2].append(final_swing_count)

        print(tabulate(table1))

    drive(279)

    # Hole 2
    print("Hole 2: 188 yds, Par 3")
    drive(188)

    # Hole 3
    print("Hole 3: 111 yds, Par 3")
    drive(111)

    # Hole 4
    print("Hole 4: 162 yds, Par 3")
    drive(162)

    # Hole 5
    print("Hole 5: 275 yds, Par 4")
    drive(275)

    # Hole 6
    print("Hole 6: 308 yds, Par 4")
    drive(308)

    # Hole 7
    print("Hole 7: 108 yds, Par 3")
    drive(108)

    # Hole 8
    print("Hole 8: 171 yds, Par 3")
    drive(171)

    # Hole 9
    print("Hole 9: 183 yds, Par 4")
    drive(183)

    total = total + int(table1[2][1]) + int(table1[2][2]) + int(table1[2][3]) + int(table1[2][4]) + int(
        table1[2][5]) + int(table1[2][6]) + int(table1[2][7]) + int(table1[2][8]) + int(table1[2][9])
    print("Your final score: ")
    table1[2].append(total)
    print(tabulate(table1))

    play_again = input("Play again? ").lower()
    if play_again == "yes":
        True
        table1 = [["Hole", 1, 2, 3, 4, 5, 6, 7, 8, 9, "Total"],
                  ["Par", 4, 3, 3, 3, 4, 4, 3, 3, 4, 28], ["Swings"]]
        print(tabulate(table1))

        total = 0
    else:
        break
