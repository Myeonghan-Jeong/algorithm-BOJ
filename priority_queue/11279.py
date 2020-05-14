# 11279 / simulate max heap
import heapq
import sys

heap = []
for _ in range(int(input())):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print(0) if len(heap) == 0 else print(heapq.heappop(heap)[-1])
    else:
        heapq.heappush(heap, (-n, n))
