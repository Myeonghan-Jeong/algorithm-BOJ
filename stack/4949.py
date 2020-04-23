# 4949 / check all VPS have right pair
import sys


def f(line):
    stack = []
    for t in line:
        if t == '(' or t == '[':
            stack.append(t)
        elif t == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 'no'
        elif t == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                return 'no'

    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'


while True:
    text = sys.stdin.readline().replace('\n', '')
    if text == '.':
        break
    print(f(text))
