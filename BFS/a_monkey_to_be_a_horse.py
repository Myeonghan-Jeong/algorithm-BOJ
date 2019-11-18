# 1600(BFS) / find min route to reach end point
from collections import deque


# set function for find route
def find(n, m, k):
    global D, board, checked

    q = deque()
    q.append([0, 0, k])

    while q:
        i, j, can = q.popleft()

        for d in range(12):
            if can == 0 and d >= 4:  # if a monkey cannot jump obstacle, continue
                continue
            ni, nj = i + D[d][0], j + D[d][1]

            if 0 <= ni < n and 0 <= nj < m:  # else calculate
                if (ni, nj) != (0, 0):
                    if board[ni][nj] != 1:
                        if d < 4:  # walking
                            if not checked[ni][nj][can]:
                                q.append([ni, nj, can])
                                checked[ni][nj][can] = checked[i][j][can] + 1
                        else:  # jumping obstacle
                            if not checked[ni][nj][can - 1]:
                                q.append([ni, nj, can - 1])
                                checked[ni][nj][can - 1] = checked[i][j][can] + 1


# set default variables and values
D = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

res = float('inf')
checked = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

find(H, W, K)

for c in checked[H - 1][W - 1]:
    if c != 0:
        if res > c:
            res = c

if res == float('inf'):
    res = -1

print(res)
