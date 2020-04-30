# 1966 / find order of target doc when printed
from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    printer = deque(map(int, input().split()))

    idx, cnt = 0, 0
    while True:
        if printer[idx] == max(printer):
            cnt += 1
            printer[idx] = 0
            if idx == m:
                break
        idx += 1
        if idx >= len(printer):
            idx = 0
    print(cnt)
