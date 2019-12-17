# 17136 / calculate min number of paper for cover all holes
def f(n, s):
    global minV

    if s == 0:  # if there is no more holes
        if minV > n:
            minV = n
    elif minV == 4:  # if holes can cover only 4 same papers
        return
    elif sum(paper) == 0:  # if there is no more papers
        return
    else:
        for i in range(10):
            for j in range(10):
                # find holes
                if m[i][j] == 1 and visited[i][j] == 0:
                    for k in range(5, 0, -1):
                        if paper[k] > 0 and i + k <= 10 and j + k <= 10:
                            # cover holes
                            cover = 0
                            for r in range(i, i + k):
                                for c in range(j, j + k):
                                    if visited[r][c] == 0:
                                        cover += m[r][c]

                            # check visited and cover next holes
                            if cover == (k * k):
                                for r in range(i, i + k):
                                    for c in range(j, j + k):
                                        visited[r][c] = 1
                                paper[k] -= 1
                                f(n + 1, s - k * k)
                                for r in range(i, i + k):
                                    for c in range(j, j + k):
                                        visited[r][c] = 0
                                paper[k] += 1
                    return  # if there is no more holes


m = [list(map(int, input().split()))for _ in range(10)]
visited = [[0] * 10 for _ in range(10)]

s = 0
minV = 26
paper = [0, 5, 5, 5, 5, 5]
for i in range(10):
    for j in range(10):
        if m[i][j] == 1:
            s += 1

f(0, s)
if minV == 26:
    minV = -1

print(minV)
