# 18258 / simulate queue with commands
from collections import deque
import sys

q = deque()
for _ in range(int(input())):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 1:
        if cmd[0] == 'pop':
            print(q.popleft() if len(q) > 0 else -1)
        elif cmd[0] == 'size':
            print(len(q))
        elif cmd[0] == 'empty':
            print(1 if len(q) == 0 else 0)
        elif cmd[0] == 'front':
            print(q[0] if len(q) > 0 else -1)
        else:
            print(q[-1] if len(q) > 0 else -1)
    else:
        q.append(cmd[1])
