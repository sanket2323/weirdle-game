# DO NOT modify or add any import statements
from typing import Any

from support import *

ALL_WORDS = load_words("words.txt")


# Name: Sanket Mane
# Student Number: 50040467
# Favorite Word: 
# -----------------------------------------------------------------------------

# Define your functions here
# task 1
def num_hours() -> float:
    return 3.14

# task 2
def has_won(guess: str, target: str) -> bool:
    if guess == target:
        return True
    return False

# task 3
def get_max_guesses() -> int:
    while True:
        number_of_guesses = input(
            "\nPlease enter the number of guesses you require to guess the secret word. Your input must be a number between 5 and 9: ")
        if number_of_guesses.isdigit():
            number_of_guesses = int(number_of_guesses)
            if number_of_guesses <= 9 and number_of_guesses >= 5:
                break
    return number_of_guesses

#task 4
def create_board(max_guesses: int) -> list[tuple[str,str]]:

    #create empty row value
    empty_row_value = EMPTY * 6

    #convert row into tuple
    row_tuple = []
    for j in range(2):
        row_tuple.append(empty_row_value)
    row_tuple = tuple(row_tuple)

    #create a board list by appending tuple rows
    game_board= []
    for i in range(max_guesses):
        game_board.append(row_tuple)
    return game_board

def main() -> None:
    pass


if __name__ == "__main__":
    main()
