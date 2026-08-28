import random

SUITS = ['spades', 'diamonds', 'clubs', 'hearts']
CARD_NAMES = ['Ace', '2', '3', '4', '5', '6', 
              '7', '8', '9', '10', 'Jack', 'Queen', 'King']
CARD_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
INITIAL_HAND_SIZE = 2
STAY_ACTION_CODE = 's'
HIT_ACTION_CODE = 'h'
ACTION_CODE_MAP = {HIT_ACTION_CODE: 'hit', STAY_ACTION_CODE: 'stay'}
DEALER_HIT_MAX = 17


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
    prompt("Dealing...")
    for _ in range(INITIAL_HAND_SIZE):
        deal(player_hand, deck)
        deal(dealer_hand, deck)

def player_turn(player_hand, dealer_hand, deck):
    action = None

    while action != STAY_ACTION_CODE and not is_bust(player_hand):
        action = player_choose_hit_or_stay()

        if action == HIT_ACTION_CODE:
            deal(player_hand, deck)
            declare_hands(player_hand, dealer_hand)

def player_choose_hit_or_stay():
    while True:
        prompt(f"Hit or Stay? ({HIT_ACTION_CODE} or {STAY_ACTION_CODE})")
        choice = input().strip().lower()
        if choice in [HIT_ACTION_CODE, STAY_ACTION_CODE]:
            prompt(f"You chose to {ACTION_CODE_MAP[choice]}")
            return choice
        else:
            prompt("Invalid choice, choose again.")

def declare_winner(winner):
    prompt(f"{winner} wins!")

def dealer_turn(dealer_hand, deck):
    while dealer_hand['total'] < DEALER_HIT_MAX and not is_bust(dealer_hand):
        prompt("Dealer chose to hit")
        deal(dealer_hand, deck)

def declare_hands(player_hand, dealer_hand):
    player_cards = join_or(
        [card['name'] for card in player_hand['cards']],
        final_sep='and')

    dealers_first_card = dealer_hand['cards'][0]
    dealer_cards = join_or(
        [dealers_first_card['name'], "unknown card"],
        final_sep='and')

    prompt(f"You have {player_cards} (hand total is: {player_hand['total']})")
    prompt(f"Dealer has {dealer_cards}")

def join_or(elements, sep=',', final_sep='or'):
  if len(elements) == 0:
    return ""

  if len(elements) == 1:
    return str(elements[0])

  if len(elements) == 2:
    return f" {final_sep} ".join(str(e) for e in elements)

  last_element = elements[-1]
  elements_str = f"{sep} ".join(str(e) for e in elements[0:-1])
  return f"{elements_str} {final_sep} {last_element}"

def play_twenty_one():
    prompt('Welcome to Twenty One!')
    while True:
        deck = get_deck()
        player_hand, dealer_hand = get_initial_hands()
        do_first_deal(player_hand, dealer_hand, deck)

        declare_hands(player_hand, dealer_hand)

        player_turn(player_hand, dealer_hand, deck)
        if is_bust(player_hand):
            prompt(f'You bust! Your hand total was {player_hand['total']}')
            declare_winner('Dealer')
        else:
            dealer_turn(dealer_hand, deck)

        if is_bust(dealer_hand):
            prompt("Dealer bust")
            declare_winner('Player')

        # declare_winner()
        if play_again() != 'y':
            break

    prompt('Thanks for playing Twenty One!')

play_twenty_one()