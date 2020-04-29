# 11866 / simulate Yoseph`s permutation
from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n + 1))

print('<', end='')
idx = 0
while len(q) != 0:
    idx += k - 1
    if idx >= len(q):  # if out of range
        idx %= len(q)
    if len(q) > 1:
        print(q[idx], end=', ')
    else:
        print(q[idx], end='')
    del q[idx]
print('>')
