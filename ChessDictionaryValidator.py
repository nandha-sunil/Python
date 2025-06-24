name=input("SREENANDHA A.S: ")
USN=input("1AY24BT052: ")
def is_valid_chess_board(board):
    white_king = 0
    black_king = 0

    for piece in board.values():
        if piece == 'wking':
            white_king += 1
        elif piece == 'bking':
            black_king += 1

    if white_king == 1 and black_king == 1:
        return True
    else:
        return False

# Example chess board
chess_board = {
    'e1': 'wking',
    'e8': 'bking',
    'a2': 'wpawn',
    'a7': 'bpawn',
}

# Check and print result
if is_valid_chess_board(chess_board):
    print("Board is valid.")
else:
    print("Board is invalid.")
