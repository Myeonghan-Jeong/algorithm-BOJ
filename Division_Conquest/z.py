# 1074(division-conquest, recursive) / set find function for find index of number
def find(ln, si, ei, sj, ej, r, c, idx):
    # ln : len of searching mat, i & j : index of searching mat
    # r & c : original inputted row and column, idx : start index of searching mat
    global res

    if ln == 2:  # if len of searching mat is 2x2 mat
        points = [(si, sj), (si, sj + 1), (si + 1, sj), (si + 1, sj + 1)]  # row and col of each point
        for k in range(4):
            if points[k] == (r, c):  # if row and col of point is original row and col
                res = idx + k  # result is sum of start index and k
                return

    if si <= r <= si - 1 + ln // 2:  # if original point is in 1st or 4th quadrant
        ei = ei // 2
        if sj <= c <= sj - 1 + ln // 2:  # if original point is in 4th quadrant
            ej = ej // 2
            position = 0
        else:  # if original point is in 1st quadrant
            sj += ln // 2
            position = 1
    else:  # if original point is in 2nd or 3rd quadrant
        si += ln // 2
        if sj <= c <= sj - 1 + ln // 2:  # if original point is in 3rd quadrant
            ej = ej // 2
            position = 2
        else:  # if original point is in 2nd quadrant
            sj += ln // 2
            position = 3

    idx += (ln ** 2) // 4 * position  # renewal start index

    find(ln // 2, si, ei, sj, ej, r, c, idx)  # recursive


# calculate index number in inputted row and column
N, r, c = map(int, input().split())

res = 0
find(2 ** N, 0, 2 ** N - 1, 0, 2 ** N - 1, r, c, 0)

print(res)
