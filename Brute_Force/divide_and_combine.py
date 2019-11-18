# 2231(Brute Force) / calculate min number of creator for make number N
N = int(input())

res, n = 0, 1
while True:
    if n >= N:  # if target number is lower than 1, result is 0
        break
    
    # divide number and plus numbers
    c, t = str(n), n
    for i in range(len(c)):
        t += int(c[i])

    # check calculated number is same as original number
    if t == N:
        res = n
        break

    n += 1

print(res)
