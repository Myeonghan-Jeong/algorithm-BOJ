# 1193 / find number in point n
m = n = int(input())

cnt = 1  # find line number
while n > cnt:
    n -= cnt
    cnt += 1

if cnt % 2 == 0:  # in even line, bottom is cnt
    t, b = 1, cnt
    for i in range(sum(range(1, cnt)) + 1, m):
        t, b = t + 1, b - 1
else:  # in odd line, top is cnt
    t, b = cnt, 1
    for i in range(sum(range(1, cnt)) + 1, m):
        t, b = t - 1, b + 1

print(f'{t}/{b}')
