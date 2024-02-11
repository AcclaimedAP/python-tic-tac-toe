
board = []

def create_board(row, column):
    for i in range(row):
        board.append([' '] * column)
    return board

def board_line():
    for i in range(len(board[0])):
        print('---', end=' ')
    print()

def print_board():
    print('    ', end='')
    for i in range(len(board[0])):
        print(i, end='   ')

    print('\n   ', end='')
    board_line()
    for i, row in enumerate(board):
        print(i, '|', end=' ')
        for cell in row:
            print(cell, end=' | ')
        
        print('\n   ', end='')
        board_line()
    print()

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)


def check_winner():
    for row in board:
        if all_equal(row) and row[0] != ' ':
            return row[0]
    for col in range(len(board[0])):
        if all_equal([board[row][col] for row in range(len(board))]) and board[0][col] != ' ':
            return board[0][col]
    if all_equal([board[i][i] for i in range(len(board))]) and board[0][0] != ' ':
        return board[0][0]
    if all_equal([board[i][len(board) - i - 1] for i in range(len(board))]) and board[0][len(board) - 1] != ' ':
        return board[0][len(board) - 1]
    return None

def is_full():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def main():
    setRow = int(input('Enter number of rows: '))
    setColumn = int(input('Enter number of columns: '))
    create_board(setRow, setColumn)
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
