# 1676 / count number of 0 when 0 is not appear
N = int(input())
if N == 0:
    print(0)  # 0! = 1
else:
    t, cnt = 1, 0
    for n in range(1, N + 1):
        t *= n
    while True:
        if t % 10 == 0:
            cnt += 1
            t //= 10
        else:
            break
    print(cnt)
