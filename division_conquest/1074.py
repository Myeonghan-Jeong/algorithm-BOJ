# 1074 / find index of number
def find(ln, si, ei, sj, ej, r, c, idx):
    # ln : len of mat, i & j : index of mat
    # r & c : original row and column, idx : start index of mat
    global res

    if ln == 2:  # if len of mat is 2 x 2
        points = [(si, sj), (si, sj + 1), (si + 1, sj), (si + 1, sj + 1)]
        for k in range(4):
            if points[k] == (r, c):  # if row and col of point is same as target
                res = idx + k  # return sum of start index and k
                return

    if si <= r <= si - 1 + ln // 2:  # if point is in 1st or 4th quadrant
        ei //= 2
        if sj <= c <= sj - 1 + ln // 2:  # if point is in 4th quadrant
            ej //= 2
            position = 0
        else:  # if point is in 1st quadrant
            sj += ln // 2
            position = 1
    else:  # if point is in 2nd or 3rd quadrant
        si += ln // 2
        if sj <= c <= sj - 1 + ln // 2:  # if point is in 3rd quadrant
            ej //= 2
            position = 2
        else:  # if point is in 2nd quadrant
            sj += ln // 2
            position = 3

    idx += (ln ** 2) // 4 * position  # renewal start index

    find(ln // 2, si, ei, sj, ej, r, c, idx)  # recursive


# calculate index number of row and column
N, r, c = map(int, input().split())

res = 0
find(2 ** N, 0, 2 ** N - 1, 0, 2 ** N - 1, r, c, 0)

print(res)
