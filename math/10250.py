# 10250 / find the closest room from elevator
for T in range(int(input())):
    H, W, N = map(int, input().split())

    cnt = 1  # room number start with 1
    while N > H:
        N -= H
        cnt += 1

    print(str(N) + ('0' + str(cnt))[-2:])
