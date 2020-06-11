# 2805 / calculate height can make m trees with cutting n trees
import sys


def cut(h, arr):
    low, high = 0, arr[0]
    res = 0

    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            return 0

        cnt = 0
        for t in arr:
            # compare tree`s height and cutter`s height
            cnt += t - mid if t >= mid else 0
            if cnt >= h and mid > res:
                res = mid
                break

        if cnt < h:  # down height
            high = mid - 1
        else:  # up height
            low = mid + 1

    return res


n, m = map(int, input().split())
trees = list(map(int, sys.stdin.readline().strip().split()))
trees.sort(reverse=True)
print(cut(m, trees))
