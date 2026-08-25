import random
import subprocess

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
MATCH_WINNING_GAME_NUM = 5

def display_scores(scores):
    for result, tally in scores.items():
        print(f"{result}: {tally}")

def display_board_and_scores(board, scores):
    subprocess.run(["clear"])

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

    display_scores(scores)

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def detect_match_winner(scores):
    if scores['Player'] == MATCH_WINNING_GAME_NUM:
        return 'Player'
    elif scores['Computer'] == MATCH_WINNING_GAME_NUM:
        return 'Computer'
    else:
        return None

def someone_won_match(scores):
    return bool(detect_match_winner(scores))

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

def play_again():
    prompt("Play again? (y or n)")
    return input().strip().lower()[0]

def initialize_scores():
    return {"Player" : 0, "Computer" : 0, "Tie": 0}

def update_scores(result, scores):
    scores[result] += 1

def reset_scores(scores):
    for result in scores:
        scores[result] = 0

def play_tic_tac_toe():
    scores = initialize_scores()
    while True:
        board = initialize_board()

        while True:
            display_board_and_scores(board, scores)

            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
            
            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
            
        display_board_and_scores(board, scores)

        if someone_won(board):
            result = detect_winner(board)
            prompt(f"{result} won!")
        else:
            result = 'Tie'
            prompt("It's a tie!")

        update_scores(result, scores)
        display_scores(scores)

        if someone_won_match(scores):
            winner = detect_match_winner(scores)
            prompt(f"{winner} won the match!")
            reset_scores(scores)

        if play_again() != 'y':
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()