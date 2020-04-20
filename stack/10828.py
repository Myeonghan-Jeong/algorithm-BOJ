# 10828 / simulate stack
import sys

stack = []
for _ in range(int(input())):
    cd = sys.stdin.readline().split()  # for high speed

    if cd[0] == 'push':
        stack.append(cd[1])
    elif cd[0] == 'pop':
        print(-1) if len(stack) == 0 else print(stack.pop())
    elif cd[0] == 'size':
        print(len(stack))
    elif cd[0] == 'empty':
        print(1) if len(stack) == 0 else print(0)
    else:
        print(-1) if len(stack) == 0 else print(stack[-1])
