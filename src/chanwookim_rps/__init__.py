"""
This module implements a simple rock-paper-scissors command-line game.
Users can play against the computer, view game instructions, and track their score.
"""
import random
import sys

commands = {
    'game': ['game', 'play'],
    'help': ['help', 'rules'],
    'exit': ['exit', 'quit']
}

rps = ['scissors', 'rock', 'paper']
win_cases = {
    'scissors': 'paper',
    'rock': 'scissors',
    'paper': 'rock'
}
score = 0

def get_command_type(user_input):
    """
    Checks which command type the user input corresponds to.

    Args:
        user_input (str): User's input command.

    Returns:
        str: Command type ('game', 'help', 'exit') or None if not recognized.
    """
    user_input = user_input.lower().strip()
    for cmd_type, aliases in commands.items():
        if user_input in aliases:
            return cmd_type
    return None

def main():
    """
    Main function to run the rock-paper-scissors game.
    It presents a menu to the user and handles game flow based on user input.
    """
    while True:
        cmd = input('''
Rock-Paper-Scissors Game
Menu | game | help | exit |
: ''').strip()
        cmd_type = get_command_type(cmd)

        if cmd_type == 'game':
            game()
            break
        elif cmd_type == 'help':
            intro()
        elif cmd_type == 'exit':
            sys.exit()
        else:
            print('Invalid command.')

def get_user_choice():
    """
    Prompts the user to choose rock, paper, or scissors, or to quit the game.
    Continuously asks for input until a valid choice is made.

    Returns:
        str: The user's choice ('scissors', 'rock', 'paper') or 'quit'.
    """
    while True:
        choice = input(f'''
Menu | quit | Current Score: {score}
Choose: scissors, rock, or paper : ''').strip().lower()

        if choice in rps:
            return choice
        elif choice in ['quit', 'exit']:
            return 'quit'
        else:
            print('\nX Invalid input. Please try again.')

def get_computer_choice():
    """
    Generates a random choice for the computer ('scissors', 'rock', 'paper').

    Returns:
        str: The computer's random choice.
    """
    return random.choice(rps)

def get_result(user: str, computer: str):
    """
    Determines the winner of a rock-paper-scissors round and updates the score.

    Args:
        user (str): The user's choice ('scissors', 'rock', 'paper').
        computer (str): The computer's choice ('scissors', 'rock', 'paper').

    Returns:
        str: A string indicating the result ('Draw', 'You win!', 'You lose').
    """
    global score
    if user == computer:
        return 'Draw'
    elif win_cases[user] == computer:
        score += 1
        return 'You win!'
    else:
        return 'You lose'

def return_result(user: str, computer: str, result: str):
    """
    Formats the game round's result into a readable string.

    Args:
        user (str): The user's choice.
        computer (str): The computer's choice.
        result (str): The outcome of the round ('Draw', 'You win!', 'You lose').

    Returns:
        str: A formatted string displaying the choices, result, and current score.
    """
    return (
        "\n"
        "==================== Result ====================\n"
        f"Your choice: {user}\n"
        f"Computer's choice: {computer}\n\n"
        f"Result: {result}\n"
        f"Current score: {score}\n"
        "================================================\n"
    )

def game():
    """
    Handles the main game loop, allowing the user to play multiple rounds.
    Resets the score when the user quits the game.
    """
    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit' or user_choice is None:
            global score
            score = 0
            main()
            break
        computer_choice = get_computer_choice()
        result = get_result(user_choice, computer_choice)
        print(return_result(user_choice, computer_choice, result))

def intro():
    """
    Prints the introduction and rules of the rock-paper-scissors game.
    """
    print('''\n===== Game Rules =====

Rock-Paper-Scissors Game!
Choose one of scissors, rock, or paper!
The opponent will randomly choose one of them.
- Scissors beats paper
- Rock beats scissors
- Paper beats rock
=======================\n''')

if __name__ == '__main__':
    main()