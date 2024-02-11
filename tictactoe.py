
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board():
    print ('\n    0   1   2', end=' ')
    print('\n  -------------')
    for i, row in enumerate(board):
        print(i, '|', end=' ')
        for cell in row:
            print(cell, end=' | ')
        print('\n  -------------')
    print()

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def is_full():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def main():
    print_board()
    player = 'X'
    while True:
        row = int(input('Enter row: '))
        col = int(input('Enter col: '))
        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print('Cell already occupied')
            continue
        print_board()
        winner = check_winner()
        if winner:
            print(f'{winner} wins!')
            break
        if is_full():
            print('It\'s a tie!')
            break
        player = 'X' if player == 'O' else 'O'

if __name__ == '__main__':
    main()
