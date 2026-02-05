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
    return random.choice(rps)

def get_result(user: str, computer: str):
    global score
    if user == computer:
        return '비겼다...'
    elif win_cases[user] == computer:
        score += 1
        return '이겼다!'
    else:
        return '졌다ㅠㅠ'

def return_result(user: str, computer: str, result: str):
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
    print('''가위바위보 게임!
가위, 바위, 보 중 하나를 입력하세요!
상대는 셋중 무작위로 하나를 냅니다.
가위는 보, 바위는 가위, 보는 바위를 이깁니다.''')

if __name__ == '__main__':
    main()