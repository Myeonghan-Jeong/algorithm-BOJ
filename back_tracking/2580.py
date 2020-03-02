# 2580 / solve uncompleted sudoku
def horizontal(x, val):  # check row
    if val in sudoku[x]:
        return False
    return True


def vertical(y, val):  # check col
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True


def bythree(x, y, val):  # check 3 by 3 box
    nx, ny = x // 3 * 3, y // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nx + i][ny + j]:
                return False
    return True


def dfs(idx):
    if idx == len(zeros):  # if filled all blanks
        for row in sudoku:  # print sudoku
            for n in row:
                print(n, end=' ')
            print()
        return 0  # end function
    else:
        for i in range(1, 10):
            nx, ny = zeros[idx]
            if horizontal(nx, i) and vertical(ny, i) and bythree(nx, ny, i):
                sudoku[nx][ny] = i  # fill some number
                if dfs(idx + 1) == 0:  # check ended
                    return 0  # if ended, end function
                sudoku[nx][ny] = 0  # unfill some number


sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
dfs(0)
