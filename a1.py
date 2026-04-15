# DO NOT modify or add any import statements
from support import *

ALL_WORDS = load_words("words.txt")


# Name: Sanket Tukaram Mane
# Student Number: 50040467
# Favorite Word: pencil
# -----------------------------------------------------------------------------

# Define your functions here
# task 1
def num_hours() -> float:
    """
    Returns the number of hours spent on the assignment
    Returns:
    (float) : Number of hours worked
    """
    return 4.14


# task 2
def has_won(guess: str, target: str) -> bool:
    """
    checks if the guess matches the target word
    Parameter:
        guess: the guess word
        target: the target word
    Returns:
    (boolean) : True if the guess matches the target word, otherwise False
    """
    if guess == target:
        return True
    return False


# task 3
def get_max_guesses() -> int:
    """
    Gets the maximum number of guesses allowed between 5 and 9
    Returns:
    (int) : A valid number of guesses between 5 and 9 entered by user.
    """
    while True:
        number_of_guesses = input(GET_NUM_GUESSES_MESSAGE)
        if number_of_guesses.isdigit():
            number_of_guesses = int(number_of_guesses)
            if number_of_guesses <= 9 and number_of_guesses >= 5:
                break
    return number_of_guesses


# task 4
def create_board(max_guesses: int) -> list[tuple[str, str]]:
    """
    Create an empty game board
    Parameter:
        max_guesses: Number of guesses allowed

    Returns:
    A list of tuples representing the game board
    """
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
    """
    Display the game board
    Parameter:
        board: The game board

    Returns:
    None
    """
    print(SEP)
    for i in range(len(board)):
        print(f"Guess {i + 1}:  {board[i][0]}")
        print(f"Feedback: {board[i][1]}")
        print(SEP)


# task 6
def generate_secret_word() -> str:
    """
    Select a random word from the list of words
    Returns:
    A random word chosen from list of words
    """
    index = randint(0, len(ALL_WORDS) - 1)
    return ALL_WORDS[index]


# task 7
def validate_input(command: str) -> bool:
    """
    checks if the command entered is valid
    Parameter:
        command: The user input

    Returns:
    True if command is valid, otherwise False
    """
    # valid single-letter special commands

    if command in HELP_COMMAND or command in QUIT_COMMAND or command in KEYBOARD_COMMAND:
        return True

    # guess must be exactly 6 alphabetic characters
    if len(command) != 6 or not command.isalpha():
        print(INVALID_FORMAT_MESSAGE)
        return False

    # guess must be lowercase and all letters unique
    if not command.islower() or len(set(command)) != 6:
        print(INVALID_CHARACTERS_MESSAGE)
        return False

    # check if command belong to list of words provided
    if command not in ALL_WORDS:
        print(INVALID_GUESS_MESSAGE)
        return False
    return True


# task 8
def get_command() -> str:
    """
    Get a command from the user
    Returns:
    A valid command
    """
    while True:
        command = input(ENTER_COMMAND_MESSAGE)
        if validate_input(command):
            break
    return command


# task 9
def get_feedback(guess: str, target: str) -> str:
    """
    Generate feedback for a guess
    Parameters:
        guess: The guessed word
        target: The secret word

    Returns:
    A string representing feedback.
    """
    feedback = ""
    for i in range(6):
        if guess[i] == target[i]:
            feedback += GREEN
        elif guess[i] in target:
            feedback += YELLOW
        else:
            feedback += BLACK
    return feedback


# task 10
def update_board(board: list[tuple], guess_num: int, guess: str, target: str) -> None:
    """
    Update the board with a new guess and feedback
    Parameters:
        board: the game board
        guess_num: current guess number
        guess: the guessed word
        target: the secret word

    Returns:
    None
    """
    get_feedback_from_fun = get_feedback(guess, target)
    board[guess_num - 1] = (guess, get_feedback_from_fun)
    return None


# task 11
def display_keyboard(keyboard: dict[str, str]) -> None:
    """
    Display the keyboard
    Parameter:
        keyboard:Dictionary storing letter statuses

    Returns:
    None
    """
    print("Keyboard:")
    print(SEP)
    items = list(keyboard.items())
    for i in range(0, len(items), 3):
        chunks = items[i:i + 3]
        for key, value in chunks:
            print(f"{key}: {value}", end="    ")
        print()
    print(SEP)


# task 12
def update_keyboard(board: list[tuple], keyboard: dict[str, str], guess_num: int) -> None:
    """
    Update the keyboard based on feedback
    Parameters:
        board:the game board
        keyboard: the keyboard dictionary
        guess_num: current guess number

    Returns:
    None
    """
    guess_word = board[guess_num - 1][0]
    feedback_word = board[guess_num - 1][1]

    for i in range(len(guess_word)):
        letter = guess_word[i]
        status = feedback_word[i]

        if keyboard[letter] == "G":
            continue

        elif status == "G":
            if keyboard[letter] != "G":
                keyboard[letter] = "G"

        elif status == "Y":
            if keyboard[letter] != "G":
                keyboard[letter] = "Y"

        else:
            if keyboard[letter] != "G":
                keyboard[letter] = "B"

    return None


# task 13
def play_game() -> None:
    """
    Runs one full game Weirdle.
    Returns:
    None
    """
    print(WELCOME_MESSAGE)
    sec_word = generate_secret_word()
    max_guesses = get_max_guesses()

    # print(f"{max_guesses}")
    board = create_board(max_guesses)
    display_board(board)
    keyboard = create_keyboard()

    current_guess_number = 1

    while current_guess_number <= max_guesses:
        command = get_command()

        if command in HELP_COMMAND:
            print(HELP_MESSAGE)

        elif command == "a" or command == "A":
            display_keyboard(keyboard)

        elif command == "q" or command == "Q":
            break

        else:
            update_board(board, current_guess_number, command, sec_word)
            update_keyboard(board, keyboard, current_guess_number)
            display_board(board)

            if has_won(command, sec_word):
                print(WIN_MESSAGE)
                break
            current_guess_number += 1
        # print(current_guess_number)

    if current_guess_number > max_guesses:
        print(LOST_MESSAGE + f" The word was: {sec_word}")


# task 14
def main() -> None:
    """
    Runs the game repeatedly until users quits.
    Returns:
    None
    """
    while True:
        play_game()
        retry_game_or_not = input(RETRY_MESSAGE)
        if retry_game_or_not.lower() != "y":
            break
    return None


if __name__ == "__main__":
    main()
