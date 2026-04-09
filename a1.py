# DO NOT modify or add any import statements
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
        number_of_guesses = input(GET_NUM_GUESSES_MESSAGE)
        if number_of_guesses.isdigit():
            number_of_guesses = int(number_of_guesses)
            if number_of_guesses <= 9 and number_of_guesses >= 5:
                break
    return number_of_guesses


# task 4
def create_board(max_guesses: int) -> list[tuple[str, str]]:
    # create empty row value
    empty_row_value = EMPTY * 6

    # convert row into tuple
    row_tuple = []
    for j in range(2):
        row_tuple.append(empty_row_value)
    row_tuple = tuple(row_tuple)

    # create a board list by appending tuple rows
    game_board = []
    for i in range(max_guesses):
        game_board.append(row_tuple)
    return game_board


# task 5
def display_board(board: list[tuple[str, str]]) -> None:
    print(SEP)
    for i in range(len(board)):
        print(f"Guess {i + 1}:  {board[i][0]}")
        print(f"Feedback: {board[i][1]}")
        print(SEP)


# task 6
def generate_secret_word() -> str:
    index = randint(0, len(ALL_WORDS) - 1)
    return ALL_WORDS[index]


# task 7
def validate_input(command: str) -> bool:
    length_of_command = len(command)

    if length_of_command == 1:
        if command.isalpha() and command in HELP_COMMAND:
            return True
        else:
            print(INVALID_FORMAT_MESSAGE)
            return False

    if length_of_command != 6 or not command.isalpha():
        print(INVALID_FORMAT_MESSAGE)
        return False

    if not command.islower() or len(set(command)) != length_of_command:
        print(INVALID_CHARACTERS_MESSAGE)
        return False

    if not command in ALL_WORDS:
        print(INVALID_GUESS_MESSAGE)
        return False

    return True


# task 8
def get_command() -> str:
    while True:
        command = input(ENTER_COMMAND_MESSAGE)

        if validate_input(command):
            break

    return command


# #task 9
# def get_feedback(guess: str, target: str) -> str:
#


def main() -> None:
    pass


if __name__ == "__main__":
    main()
