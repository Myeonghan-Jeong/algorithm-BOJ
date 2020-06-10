# 1654 / calculate max len of lan for make n lans with k lans, has diff len each others
import sys


def paramatic_search(n, arr):
    low, high = 0, arr[-1]  # set left, right boundary

    res = 0  # max len
    while low <= high:  # loop whenever left overflows right
        mid = (high + low) // 2
        if not mid:  # when mid is 0, connot calculate max len
            return 1

        cnt = 0
        for var in arr:
            cnt += var // mid  # cut lans and throw out left lans
            # if number of cutted lans is over n and now len is longer than result
            if cnt >= n and mid > res:
                res = mid  # set result
                break

        if cnt < n:  # if number of lans lacks
            high = mid - 1  # down right boundary
        else:
            low = mid + 1  # up left boundary

    return res


k, n = map(int, sys.stdin.readline().strip().split())
arr = [int(sys.stdin.readline().strip()) for _ in range(k)]
arr.sort()
print(paramatic_search(n, arr))
