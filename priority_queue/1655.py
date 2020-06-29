# 1655 / find mid number in numbers
import heapq
import sys

# max_heap saves lower number than mid, min_heap saves higher number than mid
max_heap, min_heap = [], []
for _ in range(int(input())):
    num = int(sys.stdin.readline().strip())
    # check len of 2 heaps
    if len(max_heap) == len(min_heap):
        # mid number is always in front of max_heap
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))

    # if mid number is higher than first number in min_heap
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        # pop each numbers
        temp_max = heapq.heappop(max_heap)[1]
        temp_min = heapq.heappop(min_heap)[1]
        # trade numbers and set new mid number
        heapq.heappush(max_heap, (-temp_min, temp_min))
        heapq.heappush(min_heap, (temp_max, temp_max))

    print(max_heap[0][1])
