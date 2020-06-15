# 1300 / calculate kth number in array, transformed by n by n matrix
def mat(s, e, n, k):
    ans = 0
    while s <= e:
        # set bisect search
        mid, cnt = (s + e) // 2, 0
        for i in range(1, n + 1):
            # count 2 numbers` multiple sets(as same as number divided share of row)
            cnt += min(mid // i, n)  # number of sets is lower than matrix size

        if cnt >= k:  # if order is higher than number of sets
            ans, e = mid, mid - 1  # set ans and down upper bound
        else:
            s = mid + 1  # up lower bound
    return ans


# n, k: matrix size, order of number in array
n, k = int(input()), int(input())
print(mat(1, k, n, k))
