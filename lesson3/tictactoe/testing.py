import cowsay
PC_NAME = 'Wilbur'

def format_cowsay_message(message):
    line_length = 30
    new_message = ''
    
    lines = message.split('\n')
    for line in lines:
        total_spaces = line_length - len(line)
        if total_spaces % 2 == 0:
            spaces_per_side_str = ' ' * (total_spaces // 2)
            new_line = spaces_per_side_str + line + spaces_per_side_str + '\n'
        else:
            spaces_left_side_str = ' ' * (total_spaces // 2)
            spaces_right_side_str = spaces_left_side_str + ' '
            new_line = spaces_left_side_str + line + spaces_right_side_str + '\n'
        
        new_message += new_line

    return new_message 

def prompt(message):
    return print(f'==> {message}')

def enter_to_continue():
    prompt('Press \'Enter\' to continue.')
    input()

def intro():
    cowsay.pig(format_cowsay_message('Oink! Oink!\n'
               'Hello, friend!\n'
               f'My name is {PC_NAME}'))
    enter_to_continue()
    cowsay.pig(format_cowsay_message('I\'m the tic-tac-toe champion\n of this farm!'))
    enter_to_continue()
    cowsay.pig(format_cowsay_message('This will be a best of three match.'))

intro()
