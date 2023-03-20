# dice roll simulator

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
    selection = input("\nEnter a number 1-5: ")

    if selection == "1":
        print("Roll Dice Once")
    elif selection == "2":
        print("Roll Dice 5 Times")
    elif selection == "3":
        print("Roll Dice 'n' Times")
    elif selection == "4":
        print("Roll Dice until Snake Eyes")
    elif selection == "5":
        print("Exit")
        loop = False
