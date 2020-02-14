# 1018 / count points for paint to make chess board
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

lines = [['W', 'B'] * 4, ['B', 'W'] * 4]
white, black = [[]] * 8, [[]] * 8  # boards start with white, black
for i in range(8):
    if i % 2 == 0:
        white[i], black[i] = lines[0], lines[1]
    else:
        white[i], black[i] = lines[1], lines[0]

res = 64
for i in range(N - 7):
    for j in range(M - 7):
        # move partial board
        white_cnt, black_cnt = 0, 0
        new_board = [board[i + _][j:j + 8][:] for _ in range(8)]
        for r in range(8):  # count
            for c in range(8):
                if new_board[r][c] != white[r][c]:
                    white_cnt += 1
                if new_board[r][c] != black[r][c]:
                    black_cnt += 1
        res = min(res, white_cnt, black_cnt)
print(res)
