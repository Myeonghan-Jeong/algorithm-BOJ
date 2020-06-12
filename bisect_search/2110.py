# 2110 / calculate max dist of 2 wifi modules
import sys


def install(arr, num):
    res, s, e = 0, 1, arr[-1] - arr[0]
    while s <= e:
        mid = (s + e) // 2  # dist of 2 wifi modules
        cnt, idx = 1, 0
        for i in range(1, len(arr)):
            if mid <= homes[i] - homes[idx]:
                cnt += 1
                idx = i
        if cnt < num:  # if cannot install all modules
            e = mid - 1  # down dist
        else:
            res = mid
            s = mid + 1  # up dist
    return res


n, c = map(int, input().split())
homes = [int(sys.stdin.readline().strip()) for _ in range(n)]
homes.sort()
print(install(homes, c))
