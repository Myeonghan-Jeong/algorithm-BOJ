# 1011 / count min move to reach final planet
for _ in range(int(input())):
    x, y = map(int, input().split())
    l = y - x

    # find sqrt number of length
    cnt = 1
    while not(cnt ** 2 <= l < (cnt + 1) ** 2):
        cnt += 1

    # count min move with finded rule
    if cnt ** 2 == l:
        print(2 * cnt - 1)
    elif cnt ** 2 < l <= cnt ** 2 + cnt:
        print(2 * cnt)
    else:
        print(2 * cnt + 1)
