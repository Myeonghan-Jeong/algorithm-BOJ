# 11286 / simulate absolute min heap
import heapq
import sys

q = []
for _ in range(int(input())):
    n = int(sys.stdin.readline().strip())
    if not n:
        if not len(q):
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(n), n))
