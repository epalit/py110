## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input:
output:

rules:
  requirements:
    - Deck: Start with a standard 52-card deck consisting of the 4 suits (Hearts, Diamonds, Clubs, and Spades), and 13 values (2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace)
    - The game consists of a dealer and a player. Both participants are initially dealt a hand of two cards. The player can see their two cards, but can only see one of the dealer's cards
    - Card values:
      - 2 - 10: face value
      - Jack, Queen, King: 10
      - Ace: 1 or 11
        - value is determined each time a new card is drawn from the deck
        - ace is worth 11 unless that busts the hand, then it is worth 1
    - Turns:
      - player always goes first and can hit or stay. Hit means deal them another card. Stay means switch to dealers turn
      - dealer must hit until the total is at least 17
    - Winning:
      - go over 21 and you bust and lose
      - if neither busts, player with the highest value wins
      - if players have the same value, it is a tie


questions:
  -

assumptions:
  - 
```

## E: Examples / Test cases
```python
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
Will want to easily remove cards from the deck - list would be ideal. Each element can be a card modelled by a dictionary containing the name, value and suit. This will allow an ace value to be updated dynamically when that card is in a hand.

Each hand should be a list of cards (same dicts as from the deck)

## A: Algorithm
1. Initialize deck
  a. build deck from constants representing deck of cards
  b. shuffle deck
2. Deal cards to player and dealer
  a. create hands
  b. deal two cards, alternating one each, recalculate value each time
3. Player turn: hit or stay
   - repeat until bust or stay
    - ask hit or stay
    - if hit, deal a card, calculate value, calculate if bust
4. If player bust, dealer wins
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins
7. Compare cards and declare winner

## C: Code
```bash
python twenty_one.py
```
