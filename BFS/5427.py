# 5427 / check @ can exit building
def fire():
    global D, W, H, building, fired

    checked = [[0] * W for _ in range(H)]

    f, r = -1, -1
    q = [[0, 0] for _ in range(W * H)]

    person = [0, 0]
    for i in range(H):
        for j in range(W):
            if building[i][j] == '*':
                r += 1
                q[r] = [i, j]
                fired[i][j] = 1
                checked[i][j] = 1
            elif building[i][j] == '@':
                person = [i, j]

    while f != r:
        f += 1
        i, j = q[f]

        for di, dj in D:
            ni, nj = i + di, j + dj

            if 0 <= ni < H and 0 <= nj < W:
                if building[ni][nj] != '#':

                    if checked[ni][nj] == 0:
                        if fired[ni][nj] == 0:
                            fired[ni][nj] = fired[i][j] + 1
                        else:
                            fired[ni][nj] = min(fired[ni][nj], fired[i][j] + 1)

                        r += 1
                        q[r] = [ni, nj]
                        checked[ni][nj] = 1

    return person


def find():
    global W, H, building, fired, person, res

    checked = [[0] * W for _ in range(H)]
    checked[person[0]][person[1]] = 1

    f, r = -1, -1
    q = [[0, 0] for _ in range(W * H)]

    r += 1
    q[r] = person

    while f != r:
        f += 1
        i, j = q[f]

        if i == 0 or i == H - 1 or j == 0 or j == W - 1:
            if checked[i][j] != 0:
                res = checked[i][j]
                return

        for di, dj in D:
            ni, nj = i + di, j + dj

            if 0 <= ni < H and 0 <= nj < W:
                if building[ni][nj] != '#':

                    if checked[ni][nj] == 0:
                        if checked[i][j] + 1 < fired[ni][nj] or fired[ni][nj] == 0:
                            checked[ni][nj] = checked[i][j] + 1

                            r += 1
                            q[r] = [ni, nj]


D = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for T in range(int(input())):
    W, H = map(int, input().split())
    building = [list(input()) for _ in range(H)]

    fired = [[0] * W for _ in range(H)]
    person = fire()

    res = W * H + 1
    find()

    if res == W * H + 1:
        print('IMPOSSIBLE')
    else:
        print(res)
