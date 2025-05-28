"""Number guessing game with self-determined bounds and a random attempt limit"""

from random import randint

def get_user_bounds():
    while True:
        try:
            lower_bound = int(input("Enter a lower integer bound: "))
            upper_bound = int(input("Enter an upper integer bound: "))

            if lower_bound < upper_bound:
                return lower_bound, upper_bound
            elif lower_bound == upper_bound:
                print("Bounds must not be equal. Please try again.")
            else:
                print("Lower bound must be less than the upper bound. Please try again.")
        except ValueError:
            print("Invalid input. Please enter only integers.")

def get_user_guess(lower_bound, upper_bound) -> int:
    while True:
        try:
            guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Please enter a valid guess within the given range. No attempt used.")
        except ValueError:
            print("Invalid guess. Please enter an integer.")

def eveluate_guess(guess: int, number: int) -> str:
    if guess > number:
        return "high"
    elif guess < number:
        return "low"
    else:
        return "correct"
    
def play_game(lower_bound, upper_bound):
    attempt_limit: int = randint(1, 10)
    attempt_count: int = 0
    number: int = randint(lower_bound, upper_bound)

    while attempt_limit > 0:
        print(f"You have {attempt_limit} attempt(s) left.")
        
        guess = get_user_guess(lower_bound, upper_bound)
        result = eveluate_guess(guess, number)
        attempt_count += 1

        if result == "low":
            print("Too low!")
        elif result == "high":
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number, {number}, in {attempt_count} attempt(s).")
            return
        
        attempt_limit -= 1
    
    print(f"You have run out of attempts. The correct number was {number}.")

def main():
    print("🎯 Welcome to the Number Guessing Game!")
    lower, upper = get_user_bounds()
    play_game(lower, upper)

main()

