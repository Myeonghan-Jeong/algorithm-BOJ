# 6549 / calculate max rectangle area in the histogram
from collections import deque
import sys

while True:
    n, *num = list(map(int, sys.stdin.readline().strip().split()))
    if n == 0:  # end
        break

    num.append(0)  # for terminate histogram, append 0 to end
    area, hist = 0, deque()
    for i, h in enumerate(num):
        # if histogram is not empty and top heigh is higher than h
        while hist and num[hist[-1]] > h:
            ih = num[hist.pop()]  # height
            # width is from now index to next top height in histogram and -1 or index
            w = i - hist[-1] - 1 if hist else i
            area = max(area, w * ih)  # caluclate area
        hist.append(i)  # append index
    print(area)
