# 2231 / calculate min number of creator of N
N = int(input())

res, n = 0, 1
while True:
    if n >= N:  # if target is lower than 1
        break

    # divide and plus numbers
    c, t = str(n), n
    for i in range(len(c)):
        t += int(c[i])

    # check calculated number is same as original
    if t == N:
        res = n
        break

    n += 1

print(res)
