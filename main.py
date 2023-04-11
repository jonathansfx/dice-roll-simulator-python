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
        randnum1 = random.randint(1, 6)
        randnum2 = random.randint(1, 6)
        sum = randnum1 + randnum2
        print(f"{randnum1},{randnum2} (sum: {sum})")
    elif selection == "2":
        print("\nRoll Dice 5 Times")
        i = 0
        while i < 5:
            randnum1 = random.randint(1, 6)
            randnum2 = random.randint(1, 6)
            sum = randnum1 + randnum2
            print(f"{randnum1},{randnum2} (sum: {sum})")
            i += 1
    elif selection == "3":
        print("\nRoll Dice 'n' Times")
        n = input("\nenter the amount of rolls you want: ")
        i = 0
        while i < int(n):
            randnum1 = random.randint(1, 6)
            randnum2 = random.randint(1, 6)
            sum = randnum1 + randnum2
            print(f"{randnum1},{randnum2} (sum: {sum})")
            i += 1
    elif selection == "4":
        print("\nRoll Dice until Snake Eyes")
        i = 0
        while i < 9999:
            randnum1 = random.randint(1, 6)
            randnum2 = random.randint(1, 6)
            sum = randnum1 + randnum2
            print(f"{randnum1},{randnum2} (sum: {sum})")
            i += 1
            if sum == 2:
                print(f"SNAKE EYES! It took {i} rolls to get snake eyes.")
                break

        # use break statement
    elif selection == "5":
        print("\nExit")
        loop = False
