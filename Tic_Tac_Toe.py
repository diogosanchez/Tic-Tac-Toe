"""
This the first milestone project for Jose Portilla's Python course (Udemy).
It's a Tic-Tac-Toe game.
Rules:
- 2 players should be able to play the game (both sitting at the same computer)
- The board should be printed out every time a player makes a move
- You should be able to accept input of the player position and then place a
  symbol on the board
"""


# functions definitions:
def print_board(p_board):
    print(" | ".join(p_board[1:4]))
    print("---------")
    print(" | ".join(p_board[4:7]))
    print("---------")
    print(" | ".join(p_board[7:10]))


def welcome():
    # Welcome message
    print('********************************')
    print('Welcome to the Tic-Tac-Toe game!')
    print('********************************')
    # Signing initial values to the board
    board = ['*', "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    print('This is the board and its position numbers:')
    print_board(board)
    input("Press ENTER to play!")
    print()


def pick_marker():
    req_mark = 'Player 1, pick a marker - "X" or "O": '
    player_1 = (input(req_mark)).upper()
    player_2 = ''
    marker = True
    while marker:
        if player_1 == 'X':
            player_2 = 'O'
            marker = False
        elif player_1 == 'O':
            player_2 = 'X'
            marker = False
        else:
            print('Incorrect marker.')
            player_1 = (input(req_mark)).upper()

    return {'1': player_1, '2': player_2}


def replace_index(n_player, pos, old_board):
    new_board = old_board
    for index, item in enumerate(board):
        if index == pos:
            new_board[index] = str(n_player)
    return new_board


def pick_position(p_num, t_pos):
    ref_position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    req_pos = f'Player {p_num}, enter a position number: '
    pos = int(input(req_pos))
    while True:
        if pos in t_pos:
            print('This position was already chosen!')
            pos = int(input(req_pos))
        elif pos in ref_position:
            break
        else:
            print('Wrong position!')
            pos = int(input(req_pos))
    return pos


def check_win(w_board):
    if ' ' != w_board[1] == w_board[2] == w_board[3]:
        return True
    elif ' ' != w_board[4] == w_board[5] == w_board[6]:
        return True
    elif ' ' != w_board[7] == w_board[8] == w_board[9]:
        return True
    elif ' ' != w_board[1] == w_board[4] == w_board[7]:
        return True
    elif ' ' != w_board[2] == w_board[5] == w_board[8]:
        return True
    elif ' ' != w_board[3] == w_board[6] == w_board[9]:
        return True
    elif ' ' != w_board[1] == w_board[5] == w_board[9]:
        return True
    elif ' ' != w_board[3] == w_board[5] == w_board[7]:
        return True
    else:
        return False


def clear():
    print('\n' * 100)


welcome()
clear()

board = ['*', " ", " ", " ", " ", " ", " ", " ", " ", " "]

player = pick_marker()
taken_pos = []
for i in range(1, 10):
    if i % 2:
        player_num = '1'
    else:
        player_num = '2'
    position = pick_position(player_num, taken_pos)
    taken_pos.append(position)
    board = replace_index(player[player_num], position, board)
    clear()
    print_board(board)
    winner = check_win(board)
    if winner:
        break

if winner:
    print(f'Player {player_num} won!')
else:
    print('Match!')
