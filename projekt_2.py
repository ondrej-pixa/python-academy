"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Ondrej Pixa
email: ondrej.pixa@gmail.com
discord: ondra_32
"""

WELCOME_TEXT = """Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game"""

# Board is represented as a list of lists (3x3).
BOARD = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]
# Maximum turns players can take during one game.
MAX_TURNS = 9


def print_board():
    """Prints the board"""
    board_str = ''
    for row in range(3):
        for col in range(3):
            board_str += BOARD[row][col] + " "
        board_str += "\n"

    print(board_str, end="")


def get_row(position: int) -> int:
    """
    Return row number from the user input position.
    {1, 2, 3} -> 0
    {4, 5, 6} -> 1
    {7, 8, 9} -> 2
    """
    return (position - 1) // 3


def get_column(position: int) -> int:
    """
    Return column number from the user input position.
    {1, 4, 7} -> 0
    {2, 5, 8} -> 1
    {3, 6, 9} -> 2
    """
    return (position - 1) % 3


def take_turn(player: str):
    """Function for handling player's turn."""

    print(f"Player {player} | Please enter your move number (from 1 to 9): ", end="")
    user_input = input()

    if not user_input.isdigit():
        raise ValueError("Not a number. Please try again.")

    number = int(user_input)
    if not (1 <= number <= 9):
        raise ValueError("Number must be from 1 to 9. Please try again.")

    # Calculate row and column from the user's number input.
    row = get_row(position=number)
    column = get_column(position=number)

    if BOARD[row][column] != ".":
        raise ValueError(f"Position {number} is already taken. Please try again.")

    # User's input is valid, we can put player's symbol on the selected board position.
    BOARD[row][column] = player


def get_next_player(current_player: str) -> str:
    """Return the next player based on the current player"""
    if current_player == "o":
        return "x"

    return "o"


def is_completed() -> bool:
    """Return True, if board has three same marks in any of its rows, columns or diagonals."""

    # Check whether any row contains the same mark.
    for row in range(3):
        if BOARD[row][0] != "." and BOARD[row][0] == BOARD[row][1] == BOARD[row][2]:
            return True

    # Check whether any column contains the same mark.
    for col in range(3):
        if BOARD[0][col] != "." and BOARD[0][col] == BOARD[1][col] == BOARD[2][col]:
            return True

    # Check whether any diagonal contains the same mark.
    if BOARD[0][0] != "." and BOARD[0][0] == BOARD[1][1] == BOARD[2][2]:
        return True
    if BOARD[0][2] != "." and BOARD[0][2] == BOARD[1][1] == BOARD[2][0]:
        return True

    return False


def main():
    """Main function starts the whole game.
    Players x and o are taking turns until one of them wins or it's a draw.
    """
    print(WELCOME_TEXT)
    print_board()

    # Track count of turns that players played.
    turns_count = 0
    # Track which player is currently on turn. Player o starts always first.
    current_player = "o"

    while turns_count < MAX_TURNS:
        try:
            take_turn(player=current_player)
        except ValueError as err:
            # Failed to take a turn. Print the error and try again.
            print(err)
            continue

        # Player has successfully marked position, increment number of played turns.
        turns_count = turns_count + 1
        print_board()

        if is_completed():
            break

        next_player = get_next_player(current_player=current_player)
        current_player = next_player

    if turns_count == MAX_TURNS:
        print("It's a draw!")
    else:
        print(f"Congratulations, player {current_player} WON!")


main()
