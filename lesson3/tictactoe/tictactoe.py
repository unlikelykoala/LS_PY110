import os
import random
import time

import cowsay
from tabulate import tabulate


EMPTY_MARKER = ' '
HUMAN_MARKER = 'X'
PC_MARKER = '◯'
GAMES_TO_WIN = 2
PC_NAME = 'Wilbur'
MIDDLE_SQUARE = 5
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],    # horizontal
    [1, 4, 7], [2, 5, 8], [3, 6, 9],    # vertical
    [1, 5, 9], [3, 5, 7]                # diagonal
]

def enter_to_continue():
    prompt('Press \'Enter\' to continue.')
    input()

def enter_to_continue_clear():
    prompt('Press \'Enter\' to continue.')
    input()
    os.system('clear')

def clear_without_enter():
    os.system('clear')

def intro():
    clear_without_enter()
    cowsay.pig('Oink! Oink!\n'
               'Hello, friend!\n'
               f'My name is {PC_NAME}.')
    enter_to_continue_clear()
    cowsay.pig('I\'m the tic-tac-toe champion\n of this farm!')
    enter_to_continue_clear()
    if player_wants_instructions():
        display_instructions()
    else:
        cowsay.pig('Suit yourself!')
    enter_to_continue_clear()
    cowsay.pig(f'To win the match, you have to get {GAMES_TO_WIN} wins.')
    enter_to_continue_clear()
    

def player_wants_instructions():
    cowsay.pig('Would you like to see the instructions?')
    response = input("Press 'Y/y' or 'N/n': ")
    while response.casefold() not in ['y', 'n']:
        clear_without_enter()
        cowsay.pig('Sorry, I couldn\'t catch that.\n')
        response = input("Press 'Y/y' or 'N/n': ")
    clear_without_enter()
    return bool(response.casefold() == 'y')

def display_instructions():
    prompt('Each round you will pick a square to put your marker.')
    enter_to_continue()

    prompt('Place 3 of your markers in a row to win.\n'
           '(vertically, horizontally, or diagonally)')
    enter_to_continue()

    prompt('You will use the numbers below to choose the square:')
    print()
    time.sleep(0.2)

    print("EXAMPLE BOARD")
    print("     |     |")
    print(f"  {1}  |  {2}  |  {3}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {4}  |  {5}  |  {6}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {7}  |  {8}  |  {9}")
    print("     |     |")
    print()

def get_player_name():
    cowsay.pig('Oh, and before we start,\n'
               'what\'s your name, friend?')
    name = input('Name: ')
    while not name:
        clear_without_enter()
        cowsay.pig('Sorry, I couldn\'t catch that.\n')
        name = input('Name: ')
    return name

def welcome_player(name):
    cowsay.pig(f'Welcome to Zuckerman Farm, {name}!')
    enter_to_continue_clear()

def get_difficulty():
    cowsay.pig(f'Tell me, how easy should I take it on you?\n'
               '1 is easy, 2 is medium, and 3 is hard.')

    difficulty = input('Enter 1, 2, or 3: ')
    while difficulty not in ['1', '2', '3']:
        clear_without_enter()
        cowsay.pig('Sorry, I couldn\'t catch that.\n'
                   '1 is easy, 2 is medium, and 3 is hard.')
        difficulty = input('Enter 1, 2, or 3: ')
    clear_without_enter()
    return difficulty

def get_current_player(player_name, pc_name):
    cowsay.pig('We will alternate who goes first each round.')
    enter_to_continue_clear()
    cowsay.pig("I'm a gentlepig so I'll let you choose.\n"
               "Will you go first in Round 1?")
    prompt("Press '1' to go first or '2' to go second:")
    response = input()
    while response not in ['1', '2']:
        cowsay.pig("Speak up!\n"
                   "I can't hear you!")
        prompt("Press '1' to go first or '2' to go second:")
        response = input()
        clear_without_enter()   
    if response == '1':
        return player_name
    else:
        return pc_name

def switch_current_player(current_player, player_name, pc_name):
    if current_player == player_name:
        return pc_name
    else:
        return player_name

def init_score_table(player_name, pc_name):
    return [[player_name, 0], [pc_name, 0]]

def update_score_table(table, winner):
    if winner == table[0][0]:
        table[0][1] += 1
    else:
        table[1][1] += 1

def display_score(table):
    print('SCOREBOARD')
    print(tabulate(table))

def check_yn_input(response):
    while response.casefold() not in ['y', 'n']:
        clear_without_enter()
        cowsay.pig('Could you say that again?\n'
                   "I couldn't make that out.")
        response = input("Enter 'Y/y' or 'N/n': ")
    
    return response

def response_is_y(response):
    return bool(response.casefold() == 'y')

def get_match_winner(board, player_name, pc_name):
    if board[0][1] == GAMES_TO_WIN:
        return player_name
    elif board[1][1] == GAMES_TO_WIN:
        return pc_name

def is_match_winner(winner):
    return bool(winner)

def play_again():
    cowsay.pig('Do you want to play again?\n')
    response = check_yn_input(input("Enter 'Y/y' or 'N/n': "))
    return bool(response_is_y(response))

def player_wins_match(player_name):
    cowsay.pig('Oink! ~sniff~ Oink!\n'
               f'Congratulations, {player_name}. That\'s two out of three.\n'
               f'You won the match...')
    enter_to_continue_clear()
    cowsay.pig('Farmer Zuckerman won\'t be happy with me...\n')
    enter_to_continue_clear()

    
def pc_wins_match(pc_name):
    cowsay.pig('Oink! Oink!\n'
               "That's two out of three! I win!")
    enter_to_continue_clear()
    cowsay.pig(f"Looks like ol' {pc_name} avoids the frying pan\n for another day!")
    enter_to_continue_clear()

def end_of_match(winner, player_name, pc_name):
    if winner == player_name:
        player_wins_match(player_name)
    else:
        pc_wins_match(pc_name)

def init_board():
    return {square: EMPTY_MARKER for square in range(1, 10)}

def display_board(board):
    os.system('clear')
    
    prompt(f"You are {HUMAN_MARKER}. {PC_NAME} is {PC_MARKER}.")
    print()
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')

def prompt(message):
    return print(f'==> {message}')

def empty_squares(board):
    return [key for key, value in board.items() if value == EMPTY_MARKER]

def join_or(seq, delimiter=', ', conjunction='or'):
    if not seq:
        return ''
    elif len(seq) == 1:
        return str(seq[0])
    elif len(seq) == 2:
        return f'{seq[0]} {conjunction} {seq[1]}'
    
    str_seq = [str(ele) for ele in seq]
    minus_last = delimiter.join(str_seq[:-1])
    full_str = minus_last + f'{delimiter}{conjunction} {str_seq[-1]}'

    return full_str

def choose_square(board, current_player, difficulty):
    if current_player == PC_NAME:
        computer_chooses_square(board, difficulty)
    else:
        player_chooses_square(board)

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)})')
        square = input().strip()
        
        if square in valid_choices:
            break
        
        prompt('Sorry, that\'s not a valid choice.')
    
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board, difficulty):
    if len(empty_squares(board)) == 0:
        return
    square = None
    if difficulty == '2':
        square = return_winner_or_at_risk_square(board, PC_MARKER)
    
    if not square:
        square = return_winner_or_at_risk_square(board, HUMAN_MARKER)

    if not square and board[5] == EMPTY_MARKER:
        square = MIDDLE_SQUARE
    
    if not square:
        square = random.choice(empty_squares(board))
    
    board[square] = PC_MARKER

def return_winner_or_at_risk_square(board, marker):
    for line in WINNING_LINES:
        markers_in_line = [board[square] for square in line]

        if markers_in_line.count(marker) == 2:
            for square in line:
                if board[square] == EMPTY_MARKER:
                    return square
                
    return None

def detect_winner(board, player_name, pc_name):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER):
            return player_name
        elif (board[sq1] == PC_MARKER
            and board[sq2] == PC_MARKER
            and board[sq3] == PC_MARKER):
            return pc_name
        
    return None

def someone_won(board, player_name, pc_name):
    return bool(detect_winner(board, player_name, pc_name))

def board_full(board):
    return len(empty_squares(board)) == 0

def play_tictactoe():
    intro()
    
    player_name = get_player_name()
    clear_without_enter()
    welcome_player(player_name)

    difficulty = get_difficulty()

    current_player = get_current_player(player_name, PC_NAME)

    score_table = init_score_table(player_name, PC_NAME)

    while True:
        board = init_board()
        display_board(board)

        while True:
            choose_square(board, current_player, difficulty)
            display_board(board)
            current_player = switch_current_player(current_player, player_name, PC_NAME)
            time.sleep(0.3)
            if someone_won(board, player_name, PC_NAME) or board_full(board):
                break

        if someone_won(board, player_name, PC_NAME):
            winner = detect_winner(board, player_name, PC_NAME)
            update_score_table(score_table, winner)
            prompt(f'{winner} won!')
            enter_to_continue_clear()
            display_score(score_table)
            enter_to_continue_clear()
        else:
            prompt('It\'s a tie!')
            enter_to_continue_clear()
            display_score(score_table)
            enter_to_continue_clear()

        if is_match_winner(get_match_winner(score_table, player_name, PC_NAME)):
            match_winner = get_match_winner(score_table, player_name, PC_NAME)
            end_of_match(match_winner, player_name, PC_NAME)
            if play_again():
                play_tictactoe()
            else:
                break

    clear_without_enter()
    prompt('Thanks for playing Tic Tac Toe!')


play_tictactoe()
