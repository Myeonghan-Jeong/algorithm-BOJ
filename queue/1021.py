# 1021 / calculate min cnt for pop target numbers
from collections import deque

n, m = map(int, input().split())
ts = deque(map(int, input().split()))  # target numbers

res = 0
queue = deque(range(1, n + 1))
while len(ts) > 0:
    if ts[0] == queue[0]:  # if target number can pop
        queue.popleft()
        ts.popleft()
    else:  # rotate numbers
        idx = queue.index(ts[0])
        if idx <= len(queue) // 2:
            queue.rotate(-idx)
            res += idx
        else:
            queue.rotate(len(queue) - idx)
            res += len(queue) - idx
print(res)
