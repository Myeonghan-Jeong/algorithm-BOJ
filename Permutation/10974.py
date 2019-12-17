# 10974 / permute numbers from 1 to N with ordered dict
def npr(n, k):
    global used, per, arr

    if n == k:
        for p in per:
            print(p, end=' ')
        print()
    else:
        for i in range(k):
            if not used[i]:
                used[i] = 1
                per[n] = arr[i]
                npr(n + 1, k)
                used[i] = 0


N = int(input())

used, per = [0] * N, [0] * N
arr = list(range(1, N + 1))
npr(0, N)
