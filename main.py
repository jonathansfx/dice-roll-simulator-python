# dice roll simulator
import random

loop = True
while loop:
    # print menu
    print("\nMAIN MENU")
    print("1: Roll Dice Once")
    print("2: Roll Dice 5 Times")
    print("3: Roll Dice 'n' Times")
    print("4: Roll Dice until Snake Eyes")
    print("5: Exit")

    # menu selection
    selection = input("Enter a number 1-5: ")

    if selection == "1":
        print("\nRoll Dice Once")
        randnum1 = random.randrange(1, 6)
        randnum2 = random.randrange(1, 6)
        sum = randnum1 + randnum2
        print("sum: "str(sum))
    elif selection == "2":
        print("\nRoll Dice 5 Times")
    elif selection == "3":
        print("\nRoll Dice 'n' Times")
    elif selection == "4":
        print("\nRoll Dice until Snake Eyes")

        # use break statement
    elif selection == "5":
        print("\nExit")
        loop = False
