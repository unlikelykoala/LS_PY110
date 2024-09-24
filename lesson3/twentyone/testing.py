import os
import random
import sys
import time

from tabulate import tabulate


CARD_VALUE_RULES = ["- All number cards are worth their face values.\n\
    - e.g., a 2 of clubs is worth 2 points.",
    "- Jacks, Queens, and Kings are worth 10 points.",
    "- Aces can be either 1 point or 11 points.\n\
    - If a player already has 10 or fewer points, the Ace is 11 points.\n\
    - If a player already 11 or more points, the Ace is 1 point."
]
RULES = [
    "The Goal: get your cards' total value as close to 21 as possible without going over.\n\
    - You can have a score of 21 exactly.\n\
    - If you go over 21, you bust (lose).",
    '1. Both you and the dealer are dealt two cards.\n\
    - You can look at both of your cards as well one of the dealer\'s.',
    '2. Your turn: decide if you want to hit (receive another card) or stay (end your turn).',
    "3. Dealer's turn: the dealer also decides to hit or stay.\n\
    - The dealer must hit until their score is at least 17.\n\
    - If the dealer goes over 21, they bust, which means you win!",
    "4. After both you and the dealer stay, then you compare hands.\n\
    - The highest score wins as long as it's not over 21.",
]
ROUNDS_TO_WIN = 3
MAX_SCORE = 21
ACE_MAX = 11
ACE_MIN = 1
DEALER_HIT_THRESHOLD = 17
DEALER = 'Dealer'
SUITS = ['clubs', 'diamonds', 'hearts', 'spades',]
NAMES_AND_VALUES = (('ace', (ACE_MIN, ACE_MAX)),(2, 2), (3, 3), (4, 4),
                    (5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
                    ('jack', 10), ('queen', 10), ('king', 10))


def clear_terminal():
    os.system('clear')

def press_enter_to_continue_clear():
    prompt("(Press 'Enter' to continue)", ending='')
    input()
    clear_terminal()

def press_enter_clear_this_line():
    prompt("(Press 'Enter' to continue)", ending='')
    input()
    print("\033[F\033[K", end='')
    flush_print()
    pause()

def pause(seconds=0.3):
    time.sleep(seconds)

def transition(seconds=0.3):
    pause(seconds)
    clear_terminal()

def prompt(message, ending='\n'):
    print('==> ' + message, end=ending)

def flush_print():
    sys.stdout.flush()

def get_name():
    clear_terminal()
    prompt('Please enter your name: ', ending='')
    name = input().strip()
    while not name:
        transition()
        prompt('You forgot to enter your name!')
        print()
        prompt('Name: ', ending='')
        name = input().strip()

    return name

def welcome_player(player_name):
    transition()
    prompt(f'Welcome to the game of Twenty-one, {player_name}!')
    print()
    press_enter_to_continue_clear()
    transition()

def return_valid_yn_response(message, response):
    while response not in ['y', 'yes', 'n', 'no']:
        transition()
        prompt('Sorry, it looks like you made a mistake in your input.')
        print()
        prompt(message)
        prompt("Press 'y' or 'n': ", ending='')
        response = input().casefold().strip()

    return response

def prompt_player_wants_instructions():
    prompt('Would you like to see the instructions?')
    print()
    prompt("Press 'y' or 'n': ", ending='')
    response = return_valid_yn_response('Would you like to see the instructions?', input().casefold().strip())

    transition()

    return bool(response == 'y')

def instructions():
    prompt('The rules are simple:\n')
    for rule in RULES:
        press_enter_clear_this_line()
        print(rule)
        print()

    press_enter_to_continue_clear()
    prompt('The card values are as follows:\n')
    for rule in CARD_VALUE_RULES:
        press_enter_clear_this_line()
        print(rule)
        print()

    press_enter_to_continue_clear()
    prompt("That's all the instructions! Do you need to see them again?")
    prompt("Press 'y' or 'n': ", ending='')
    response = return_valid_yn_response("Do you need to see the instructions again?",
                                        input().casefold().strip())
    if response == 'y':
        transition()
        instructions()

    transition()

def init_deck():  
    return [(name, value, suit) for suit in SUITS
                 for name, value in NAMES_AND_VALUES]

def shuffle(deck):
    random.shuffle(deck)

def init_score_table(player_name):
    return [[player_name, 0], [DEALER, 0]]

def update_score_table(table, winner):
    if winner == DEALER:
        table[1][1] += 1
    else:
        table[0][1] += 1

def display_scoreboard(table):
    print('SCOREBOARD')
    print(tabulate(table))
    print()

def display_game_start(player_name):
    prompt(f"You need to win {ROUNDS_TO_WIN} rounds to win the game.")
    print()
    press_enter_to_continue_clear()
    transition()
    prompt(f"Ready, {player_name}? Let's start!")
    print()
    press_enter_to_continue_clear()

def deal_card_from_deck(deck):
    card = random.choice(deck)
    deck.remove(card)

    return card

def deal_both_hands(deck):
    player_hand = []
    dealer_hand = []

    for i in range(2):
        card = deal_card_from_deck(deck)
        player_hand.append(card)
        card = deal_card_from_deck(deck)
        dealer_hand.append(card)

    return player_hand, dealer_hand

def player_turn(deck, player_hand, dealer_hand):
    transition()

    while True:     
        points = calculate_hand_total_points(player_hand)

        display_dealer_hand(dealer_hand)
        display_player_hand(player_hand)
        display_player_points(points)
        
        hit_or_stay = prompt_player_hit_or_stay(points)
        if hit_or_stay in ['s', 'stay']:
            return 'stay'
        
        player_hits(deck, player_hand)

        points = calculate_hand_total_points(player_hand)
        if is_bust(points):
            return 'bust'

def dealer_turn(deck, dealer_hand):
    dealer_thinking()

    while True:
        points = calculate_hand_total_points(dealer_hand)

        if is_bust(points):
            return 'bust'

        if dealer_will_stay(points):
            return 'stay'

        dealer_hits(deck, dealer_hand)

def one_round(deck, player_hand, dealer_hand, player_name, score_table):
    stay_or_bust = player_turn(deck, player_hand, dealer_hand)
    player_points, dealer_points = compare_hands_return_both_scores(player_hand, dealer_hand)

    if stay_or_bust == 'stay':
        stay_or_bust = dealer_turn(deck, dealer_hand)

        if stay_or_bust == 'stay':
            player_points, dealer_points = compare_hands_return_both_scores(player_hand, dealer_hand)
            winner = return_winner_after_comparing(player_points, dealer_points, player_name)
        else:
            winner = player_name
    
    else:
        winner = DEALER
    
    display_round_results(winner, stay_or_bust, player_points, dealer_points)
    if winner in [DEALER, player_name]:
        update_score_table(score_table, winner)

def calculate_ace_points(hand, no_ace_total):
    aces_only_total = 0
    for card in hand:
        if card[0] == 'ace':
            if is_bust(no_ace_total + ACE_MAX):
                aces_only_total += ACE_MIN
            else:
                aces_only_total += ACE_MAX

    return aces_only_total

def calculate_hand_total_points(hand):
    no_ace_total = 0
    for card in hand:
        if card[0] != 'ace':
            no_ace_total += card[1]
 
    return no_ace_total + calculate_ace_points(hand, no_ace_total)

def display_player_hand(player_hand):
    prompt(f"You have: ", ending='')
    if len(player_hand) == 2:
        print(f"the {player_hand[0][0]} of {player_hand[0][2]}"
              f" and the {player_hand[1][0]} of {player_hand[1][2]}.")
    else:
        for card in player_hand[:-1]:
            print(f"the {card[0]} of {card[2]}, ", end='')
        print(f"and the {player_hand[-1][0]} of {player_hand[-1][2]}.")

    print()
    pause()

def display_dealer_hand(dealer_hand):
    prompt(f"{DEALER} has: an unknown card and the {dealer_hand[0][0]} of {dealer_hand[0][2]}.")
    print()
    pause()

def display_player_points(points):
    prompt(f"Your current point total: {points}")
    print()
    pause()

def is_bust(points):
    return points > MAX_SCORE

def ends_with_bust(winner):
    if winner == DEALER:
        prompt(f"Oh no! Your score went over {MAX_SCORE}. That's a bust!")
        print()
        pause()
        prompt(f"{DEALER} wins this round.")
    else:
        prompt(f"{DEALER} busted! You win this round!")
    print()
    pause()
    press_enter_to_continue_clear()

def ends_with_stay(winner, player_points, dealer_points):
    if winner == DEALER:
        prompt(f"Sorry, {DEALER} wins this round.")

    elif winner == 'tie':
        prompt(f"It's a push! That means you tied, so no winners this round.")

    else:
        prompt("You win this round!")

    pause()
    print()
    prompt(f'You had {player_points} and {DEALER} had {dealer_points}.')
    pause()
    print()
    press_enter_to_continue_clear()
    transition()

def prompt_player_hit_or_stay(player_points):
    prompt('Do you want to hit or stay?')
    prompt("Enter 'h' for hit or 's' for stay: ", ending='')
    response = input().casefold().strip()
    while response not in ['h', 'hit', 's', 'stay']:
        transition()
        display_player_points(player_points)
        print()
        pause()
        prompt('Sorry, it looks like you made a mistake in your input.')
        print()
        pause()
        prompt('Do you want to hit or stay?')
        prompt("Enter 'h' for hit or 's' for stay: ", ending='')
        response = input().casefold().strip()

    return response

def player_hits(deck, player_hand):
    new_card = deal_card_from_deck(deck)
    player_hand.append(new_card)
    transition()
    prompt("You chose to hit!")
    print()
    pause()
    prompt(f"Your new card is the {new_card[0]} of {new_card[2]}.")
    print()
    press_enter_to_continue_clear()
    pause()

def dealer_thinking():
    transition()
    prompt(f"{DEALER} is thinking.", ending='')
    pause()
    flush_print()
    print('.', end='')
    pause()
    flush_print()
    print('.', end='')
    pause()
    flush_print()
    print('.', end='')
    pause()
    flush_print()
    print('.', end='')
    pause()
    flush_print()
    print('.', end='')
    pause()
    flush_print()
    print('.')
    transition()

def dealer_will_stay(points):
    return points >= DEALER_HIT_THRESHOLD

def dealer_hits(deck, dealer_hand):
    card = deal_card_from_deck(deck)
    dealer_hand.append(card)

def compare_hands_return_both_scores(player_hand, dealer_hand):
    player_points = calculate_hand_total_points(player_hand)
    dealer_points = calculate_hand_total_points(dealer_hand)

    return player_points, dealer_points

def return_winner_after_comparing(player_points, dealer_points, player_name):
    if player_points > dealer_points:
        return player_name
    elif player_points < dealer_points:
        return DEALER
    return 'tie'

def display_round_results(winner, ending_action, player_points, dealer_points):
    transition()

    if ending_action == 'bust':
        ends_with_bust(winner)
        transition()
        return

    else:
        ends_with_stay(winner, player_points, dealer_points)

def match_is_over(score_table):
    return (score_table[0][1] == ROUNDS_TO_WIN
            or score_table[1][1] == ROUNDS_TO_WIN)

def display_match_results(score_table):
    press_enter_clear_this_line()

    if score_table[0][1] == ROUNDS_TO_WIN:
        prompt(F"Congratulations! That's {ROUNDS_TO_WIN}! You won the match!")
    else:
        prompt(F"Sorry, that's {ROUNDS_TO_WIN}. {DEALER} won the match.")

    print()
    pause()

    press_enter_to_continue_clear()

def prompt_play_next_round():
    prompt("Would you like to continue to the next round?")
    print()
    prompt("Press 'y' or 'n': ", ending='')
    response = return_valid_yn_response("Would you like to continue to the next round?", 
                                        input().casefold().strip())

    return response in ['y', 'yes']

def prompt_play_new_match():
    prompt("Would you like to play a new match?")
    print()
    prompt("Press 'y' or 'n': ", ending='')
    response = return_valid_yn_response("Would you like to play a new match?",
                                        input().casefold().strip())

    return response in ['y', 'yes']

def play_twentyone():
    player_name = get_name()
    welcome_player(player_name)

    score_table = init_score_table(player_name)

    if prompt_player_wants_instructions():
        instructions()

    display_game_start(player_name)

    while True:
        deck = init_deck()
        shuffle(deck)

        player_hand, dealer_hand = deal_both_hands(deck)

        one_round(deck, player_hand, dealer_hand, player_name, score_table)

        display_scoreboard(score_table)

        if match_is_over(score_table):
            display_match_results(score_table)
            if prompt_play_new_match():
                play_twentyone()
            else:
                break

        if not prompt_play_next_round():
            break
    
    transition()
    prompt('Thank you for playing Twenty-One!')


play_twentyone()
