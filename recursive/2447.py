# 2447 / print stars with find rule
def star_maker(n, point, length):
    global stars

    s, e = point
    if n == 1:
        return
    else:
        # remove stars
        for i in range(s + length, s + 2 * length):
            for j in range(e + length, e + 2 * length):
                stars[i][j] = ' '
        # move to next mini sqaure
        for i in range(3):
            for j in range(3):
                star_maker(n // 3, (s + i * length,
                                    e + j * length), length // 3)


N = int(input())
stars = [['*'] * N for _ in range(N)]

star_maker(N, (0, 0), N // 3)
for _ in range(N):
    print(''.join(stars[_]))
