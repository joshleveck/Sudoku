from Helpers import visual


def solve(board, win, colours, width, font):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            win.fill(colours["WHITE"])
            visual.drawFromArray(board, colours, win, width, font)
            if solve(board, win, colours, width, font):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    board_x_x = pos[1] // 3
    board_x_y = pos[0] // 3

    for i in range(board_x_y * 3, board_x_y * 3 + 3):
        for j in range(board_x_x * 3, board_x_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None
