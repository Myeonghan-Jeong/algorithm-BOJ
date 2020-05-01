# 10866 / simulate deque
from collections import deque
import sys

deque = deque()
for _ in range(int(input())):
    cmd = sys.stdin.readline().replace('\n', '').split()
    if len(cmd) > 1:
        cmd, n = cmd
        deque.appendleft(n) if cmd == 'push_front' else deque.append(n)
    else:
        cmd = cmd[0]
        if cmd == 'pop_front':
            print(deque.popleft()) if len(deque) > 0 else print(-1)
        elif cmd == 'pop_back':
            print(deque.pop()) if len(deque) > 0 else print(-1)
        elif cmd == 'size':
            print(len(deque))
        elif cmd == 'empty':
            print(1) if len(deque) == 0 else print(0)
        elif cmd == 'front':
            print(deque[0]) if len(deque) > 0 else print(-1)
        else:
            print(deque[-1]) if len(deque) > 0 else print(-1)
