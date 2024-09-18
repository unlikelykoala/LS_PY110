import os
import random


EMPTY_MARKER = ' '
HUMAN_MARKER = 'X'
PC_MARKER = '◯'


def innit_board():
    return {square: EMPTY_MARKER for square in range(1, 10)}

def display_board(board):
    os.system('clear')
    
    prompt(f"You are {HUMAN_MARKER}. Computer is {PC_MARKER}.")
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


def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)})')
        square = input().strip()
        
        if square in valid_choices:
            break
        
        prompt('Sorry, that\'s not a valid choice.')
    
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = PC_MARKER

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == PC_MARKER
            and board[sq2] == PC_MARKER
            and board[sq3] == PC_MARKER):
            return 'Computer'
        
    return None

def someone_one(board):
    return bool(detect_winner(board))

def board_full(board):
    return len(empty_squares(board)) == 0

def play_tictactoe():
    while True:
        board = innit_board()
        display_board(board)

        while True:
            player_chooses_square(board)
            display_board(board)

            if someone_one(board) or board_full(board):
                break

            computer_chooses_square(board)
            display_board(board)

            if someone_one(board) or board_full(board):
                break

        if someone_one(board):
            prompt(f'{detect_winner(board)} won!')
        else:
            prompt('It\'s a tie!')

        prompt('Play again? (y or n)')
        answer = input().lower()

        if answer[0] != 'y':
            break
    
    prompt('Thanks for playing Tic Tac Toe!')


play_tictactoe()
