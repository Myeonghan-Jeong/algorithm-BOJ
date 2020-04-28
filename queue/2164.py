# 2164 / suffle cards with sepcial rule and return the last card
from collections import deque

q = deque(range(1, int(input()) + 1))
while len(q) > 1:
    q.popleft()  # pop first card
    q.append(q.popleft())  # put first card to left
print(q[0])
