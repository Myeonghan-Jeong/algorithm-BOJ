# 1927 / simulate min heap
import heapq
import sys

q = []
for _ in range(int(input())):
    n = int(sys.stdin.readline().strip())
    # check n is 0
    if not n:
        # check heap is empty
        if not len(q):
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, n)
