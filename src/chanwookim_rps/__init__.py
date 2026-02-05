"""
This module implements a simple rock-paper-scissors command-line game.
Users can play against the computer, view game instructions, and track their score.
"""
import random
import sys

cmd_list = ['게임','설명','닫기']
rps = ['가위', '바위', '보']
win_cases = {
    '가위': '보',
    '바위': '가위',
    '보': '바위'
}
score = 0

def main():
    """
    Main function to run the rock-paper-scissors game.
    It presents a menu to the user and handles game flow based on user input.
    """
    while True:
        cmd = input('''
    가위바위보 게임
메뉴 | 게임 | 설명 | 닫기 |
: ''').strip()
        if cmd == '게임':
            game()
            break
        if cmd == '설명':
            intro()
        if cmd == '닫기':
            sys.exit()
        else:
            print('잘못된 명령어입니다.')

def get_user_choice():
    """
    Prompts the user to choose rock, paper, or scissors, or to quit the game.
    Continuously asks for input until a valid choice is made.

    Returns:
        str: The user's choice ('가위', '바위', '보') or '끝내기'.
    """
    while True:
        choice = input(f'''
메뉴 |끝내기| 현재 점수: {score}
가위, 바위, 보 중 하나를 선택하세요 : ''').strip()
        if choice in rps:
            return choice
        if choice == '끝내기':
            return '끝내기'
        else:
            print('\nX 잘못된 입력입니다. 다시 입력해주세요.')

def get_computer_choice():
    """
    Generates a random choice for the computer ('가위', '바위', '보').

    Returns:
        str: The computer's random choice.
    """
    return random.choice(rps)

def get_result(user: str, computer: str):
    """
    Determines the winner of a rock-paper-scissors round and updates the score.

    Args:
        user (str): The user's choice ('가위', '바위', '보').
        computer (str): The computer's choice ('가위', '바위', '보').

    Returns:
        str: A string indicating the result ('비겼다...', '이겼다!', '졌다ㅠㅠ').
    """
    global score
    if user == computer:
        return '비겼다...'
    elif win_cases[user] == computer:
        score += 1
        return '이겼다!'
    else:
        return '졌다ㅠㅠ'

def return_result(user: str, computer: str, result: str):
    """
    Formats the game round's result into a readable string.

    Args:
        user (str): The user's choice.
        computer (str): The computer's choice.
        result (str): The outcome of the round ('비겼다...', '이겼다!', '졌다ㅠㅠ').

    Returns:
        str: A formatted string displaying the choices, result, and current score.
    """
    return (
        "\n"
        "==================== 결과 ====================\n"
        f"내 선택: {user}\n"
        f"상대 선택: {computer}\n\n"
        f"결과: {result}\n"
        f"현재 점수: {score}\n"
        "===============================================\n"
    )

def game():
    """
    Handles the main game loop, allowing the user to play multiple rounds.
    Resets the score when the user quits the game.
    """
    while True:
        user_choice = get_user_choice()
        if user_choice == '끝내기' or user_choice is None:
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
    print('''가위바위보 게임!
가위, 바위, 보 중 하나를 입력하세요!
상대는 셋중 무작위로 하나를 냅니다.
가위는 보, 바위는 가위, 보는 바위를 이깁니다.''')

if __name__ == '__main__':
    main()