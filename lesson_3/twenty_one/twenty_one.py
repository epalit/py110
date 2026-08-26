import random

SUITS = ['spades', 'diamonds', 'clubs', 'hearts']
CARD_NAMES = ['Ace', '2', '3', '4', '5', '6', 
              '7', '8', '9', '10', 'Jack', 'Queen', 'King']
CARD_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
INITIAL_HAND_SIZE = 2

def prompt(msg):
    print(f'==> {msg}')

def play_again():
    while True:
        prompt("Play again? (y or n)")
        choice = input().strip().lower()
        if choice in ['y', 'n']:
            return choice
        else:
            prompt("Invalid choice, choose again.")

def build_deck():
    deck = []
    for suit in SUITS:
        for card_name, card_val in zip(CARD_NAMES, CARD_VALUES):
            card = dict(
                suit = suit,
                name = card_name,
                value = card_val,
            )
            deck.append(card)

    return deck

def get_deck():
    deck = build_deck()
    random.shuffle(deck)
    return deck

def get_card(deck):
    return deck.pop()

def deal(hand, deck):
    hand.append(get_card(deck))

def get_initial_hands():
    return [], []

def do_first_deal(player_hand, dealer_hand, deck):
    for _ in range(INITIAL_HAND_SIZE):
        deal(player_hand, deck)
        deal(dealer_hand, deck)

def play_twenty_one():
    prompt('Welcome to Twenty One!')
    while True:
        deck = get_deck()
        player_hand, dealer_hand = get_initial_hands()
        do_first_deal(player_hand, dealer_hand, deck)
        # player_turn()
        # dealer_turn()
        # declare_winner()
        if play_again() != 'y':
            break

    prompt('Thanks for playing Twenty One!')

play_twenty_one()