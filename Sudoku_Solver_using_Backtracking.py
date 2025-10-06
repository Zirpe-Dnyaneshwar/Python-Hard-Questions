def valid(board, r, c, n):
    for i in range(9):
        if board[r][i] == n or board[i][c] == n:
            return False
    box_r, box_c = 3*(r//3), 3*(c//3)
    for i in range(box_r, box_r+3):
        for j in range(box_c, box_c+3):
            if board[i][j] == n:
                return False
    return True

def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for n in range(1,10):
                    if valid(board, r, c, n):
                        board[r][c] = n
                        if solve(board): return True
                        board[r][c] = 0
                return False
    return True
