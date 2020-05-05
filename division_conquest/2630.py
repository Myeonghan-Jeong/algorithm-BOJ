# 2630 / find all white and blue papers divide with rectangle
def cut(r, c, n):  # r, c: start point, n: paper len
    global paper
    color, div = paper[r][c], 0  # check div is needed
    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != color:
                div = 1
                break
        if div == 1:
            break

    w, b = 0, 0
    if div == 1:
        for k in range(4):  # div 4 papers
            f, s = cut(r + (n // 2) * (k // 2), c + (n // 2) * (k % 2), n // 2)
            w += f
            b += s
        return w, b
    else:
        if paper[r][c] == 0:  # white
            return 1, 0
        else:  # blue
            return 0, 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = cut(0, 0, N)
print(white)
print(blue)
