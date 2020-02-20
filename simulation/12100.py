# 12100 / play 2048 game and find max number block
def npr(k, n):  # permutaion
    global permute, permutes, idx

    if k == n:
        permutes[idx] = permute[:]
        idx += 1
    else:
        # 0: up, 1: right, 2: down, 3: left
        for i in range(4):
            permute[k] = i
            npr(k + 1, n)


def move(commands, n):
    global fake_board

    for command in commands:
        if command == 0:  # up
            for i in range(n):
                for j in range(n):
                    if fake_board[i][j] != 0:
                        ti = i
                        while True:  # find same number and sum to down
                            ti += 1
                            if ti >= n or (fake_board[ti][j] != 0 and fake_board[i][j] != fake_board[ti][j]):
                                break
                            if fake_board[i][j] == fake_board[ti][j]:
                                fake_board[i][j] *= 2
                                fake_board[ti][j] = 0
                                break
                        ti = i
                        while True:  # move block to up
                            ti -= 1
                            if ti < 0 or fake_board[ti][j] != 0:
                                fake_board[i][j], fake_board[ti +
                                                             1][j] = fake_board[ti + 1][j], fake_board[i][j]
                                break
        elif command == 1:  # right
            for i in range(n):
                for j in range(n - 1, -1, -1):
                    if fake_board[i][j] != 0:
                        tj = j
                        while True:  # find same number and sum to left
                            tj -= 1
                            if tj < 0 or (fake_board[i][tj] != 0 and fake_board[i][j] != fake_board[i][tj]):
                                break
                            if fake_board[i][j] == fake_board[i][tj]:
                                fake_board[i][j] *= 2
                                fake_board[i][tj] = 0
                                break
                        tj = j
                        while True:  # move block to right
                            tj += 1
                            if tj >= n or fake_board[i][tj] != 0:
                                fake_board[i][j], fake_board[i][tj -
                                                                1] = fake_board[i][tj - 1], fake_board[i][j]
                                break
        elif command == 2:  # down
            for i in range(n - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if fake_board[i][j] != 0:
                        ti = i
                        while True:  # find same number and sum to up
                            ti -= 1
                            if ti < 0 or (fake_board[ti][j] != 0 and fake_board[i][j] != fake_board[ti][j]):
                                break
                            if fake_board[i][j] == fake_board[ti][j]:
                                fake_board[i][j] *= 2
                                fake_board[ti][j] = 0
                                break
                        ti = i
                        while True:  # move block to down
                            ti += 1
                            if ti >= n or fake_board[ti][j] != 0:
                                fake_board[i][j], fake_board[ti -
                                                             1][j] = fake_board[ti - 1][j], fake_board[i][j]
                                break
        else:  # left
            for i in range(n):
                for j in range(n):
                    if fake_board[i][j] != 0:
                        tj = j
                        while True:  # find same number and sum to right
                            tj += 1
                            if tj >= n or (fake_board[i][tj] != 0 and fake_board[i][j] != fake_board[i][tj]):
                                break
                            if fake_board[i][j] == fake_board[i][tj]:
                                fake_board[i][j] *= 2
                                fake_board[i][tj] = 0
                                break
                        tj = j
                        while True:  # move block to left
                            tj -= 1
                            if tj < 0 or fake_board[i][tj] != 0:
                                fake_board[i][j], fake_board[i][tj +
                                                                1] = fake_board[i][tj + 1], fake_board[i][j]
                                break

    max_block = 0
    for i in range(n):
        max_block = max(max_block, max(fake_board[i]))
    return max_block


permute = [0] * 5
permutes = [[]] * (4 ** 5)
idx = 0
npr(0, 5)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

sco = -1
for permute in permutes:
    fake_board = [board[i][:] for i in range(N)]
    res = move(permute, N)
    sco = max(sco, res)
print(sco)
