"""Dice rolling game that utilizes randit"""

from random import randint

def dice_rolling_game() -> None:
    while True:
        answer = input("Roll the dice? (y/n): ").lower()
        if answer == "y":
            print((randint(1,6), randint(1,6)))
        elif answer == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")

dice_rolling_game()
