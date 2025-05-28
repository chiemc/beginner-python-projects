"""Rock paper scissors game"""

from random import choice

ROCK = "r"
SCISSORS = "s"
PAPER = "p"
emojis: dict[str, str] = {ROCK: "🪨", PAPER: "📄", SCISSORS: "✂️"}
valid_choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid choice! Try again.")
            continue

def display_choices(user_choice, computer_choice):
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_outcome(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == ROCK and computer_choice == SCISSORS)):
        print("You win!")
    else:
        print("You lose!")


def rock_paper_scissor() -> None:
    while True:
        
        user_choice = get_user_choice()

        computer_choice = choice(valid_choices)
        
        display_choices(user_choice, computer_choice)

        determine_outcome(user_choice, computer_choice)

        decision_to_continue = input("Continue? (y/n): ").lower()
        if decision_to_continue == "n":
            print("Thanks for playing!")
            break

rock_paper_scissor()