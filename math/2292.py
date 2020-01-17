# 2292 / count rooms to reach room N
N = int(input())

row = 1
start, end = 1, 1
while True:
    # check room is in range
    if start <= N <= end:
        print(row)
        break
    else:
        start += 6 * (row - 1) if row > 1 else 1
        end += 6 * row
        row += 1
