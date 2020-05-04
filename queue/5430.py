# 5430 / simulate AC
from collections import deque

for _ in range(int(input())):
    cmd, n = input(), int(input())
    cmd.replace('RR', '')  # double reverse is same as original
    if n != 0:
        numbers = deque(input()[1:-1].split(','))
    else:
        _ = input()
        numbers = deque([])

    is_reversed = False
    for c in cmd:
        if c == 'R':  # reverse deque
            is_reversed = not is_reversed
        else:  # pop numbers
            if len(numbers) > 0:
                numbers.popleft() if not is_reversed else numbers.pop()
            else:
                print('error')
                break
    else:
        if is_reversed:
            numbers.reverse()
        print('[' + ','.join(numbers) + ']')
