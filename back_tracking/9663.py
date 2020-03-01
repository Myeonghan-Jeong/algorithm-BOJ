# 9663 / count routes for put n queens on boards(https://rebas.kr/761)
def queen(i, n):
    global res

    if i == n:  # if put all queens, plus count 1
        res += 1
        return

    for j in range(n):
        if not (up[j] or left[i + j] or right[i - j + n - 1]):  # check up, left, right with rules
            up[j] = left[i + j] = right[i - j + n - 1] = True
            queen(i + 1, n)
            up[j] = left[i + j] = right[i - j + n - 1] = False


N, res = int(input()), 0
up, left, right = [False] * N, [False] * (2 * N - 1), [False] * (2 * N - 1)

queen(0, N)
print(res)
