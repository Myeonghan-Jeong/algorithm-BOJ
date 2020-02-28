# 15649 / make permutes with select M numbers in N numbers


def npr(n, k, N):
    global permute, used

    if n == k:
        permuted = ' '.join(list(map(str, permute)))
        print(permuted)
    else:
        for i in range(N):
            if not used[i]:
                used[i] = 1
                permute[n] = i + 1
                npr(n + 1, k, N)
                used[i] = 0


N, M = map(int, input().split())

permute = [0] * M
used = [0] * N
npr(0, M, N)

# 15650 / make permutes with ascending and select M numbers in N numbers


def npr(n, s, k, N):
    global permute

    if n == k:
        permuted = ' '.join(list(map(str, permute)))
        print(permuted)
    else:
        for i in range(s, N):
            permute[n] = i + 1
            npr(n + 1, i + 1, k, N)


N, M = map(int, input().split())

permute = [0] * M
npr(0, 0, M, N)

# 15651 / make permutes with duplicated and select M numbers in N numbers


def npr(n, r, t):
    global permute

    if n == r:
        for p in permute:
            print(p, end=' ')
        print()
    else:
        for i in range(t):
            permute[n] = i + 1
            npr(n + 1, r, t)


N, M = map(int, input().split())

permute = [0] * M
npr(0, M, N)

# 15652 / make permutes with duplicated, ASC numbers and select M numbers in N numbers


def npr(n, r, t):
    global permute

    if n == r:
        for p in permute:
            print(p, end=' ')
        print()
    else:
        if n == 0:
            for i in range(t):
                permute[n] = i + 1
                npr(n + 1, r, t)
        else:
            for i in range(permute[n - 1], t + 1):
                permute[n] = i
                npr(n + 1, r, t)


N, M = map(int, input().split())

permute = [0] * M
npr(0, M, N)
