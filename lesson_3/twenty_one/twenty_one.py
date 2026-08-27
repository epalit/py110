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
    hand['cards'].append(get_card(deck))
    update_hand(hand)

def update_hand(hand):
    if has_ace(hand):
        set_ace_values(hand)
    else:
        recalculate_hand_total(hand)

def has_ace(hand):
    for card in hand['cards']:
        if card['name'] == 'Ace':
            return True
    return False

def recalculate_hand_total(hand):
    total = calculate_hand_total(hand)
    hand['total'] = total

def set_ace_values(hand):
    aces = []

    # set all aces to 1
    for card in hand['cards']:
        if card['name'] == 'Ace':
            card['value'] = 1
            aces.append(card)
    recalculate_hand_total(hand)

    # if hand is bust with all aces set to 1, leave it as is
    if is_bust(hand):
        return

    # can only have 1 ace with value 11 per hand (11 + 11 = 22 which is bust)
    if aces:
        aces[0]['value'] = 11 # arbitrarily pick first ace to set to 11
        recalculate_hand_total(hand)
        if is_bust(hand):
            aces[0]['value'] = 1 # if setting to 11 busts the hand keep it as 1
            recalculate_hand_total(hand)

def calculate_hand_total(hand):
    return sum([card['value'] for card in hand['cards']])

def is_bust(hand):
    return hand['total'] > 21

def get_initial_hands():
    player_hand = {'cards': [], 'value': 0}
    dealer_hand = {'cards': [], 'value': 0}
    return player_hand, dealer_hand

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