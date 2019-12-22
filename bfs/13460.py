# 13460 / check get out red ball from box
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


# n: moving counter, c: returned ball, go: moving direction
# iR, jR, iB, jB: point of each balls
def f(n, iR, jR, iB, jB, c, go):
    global res

    if c == 1:  # if returned ball is red only
        if res > n:
            res = n
    elif c > 1:  # if returned ball is blue or more than 2
        return
    elif n == 10:  # if moving counter reached 10
        return
    else:
        for k in range(4):
            p = [iR, jR, iB, jB]
            # check balls can move
            if go == -1 or k != go and k != (go + 2) % 4:
                c, p = move(p, k)  # move balls
                if c == 0 and iR == p[0] and jR == p[1] and iB == p[2] and jB == p[3]:
                    continue
                else:
                    f(n + 1, p[0], p[1], p[2], p[3], c, k)  # next moving


# p: point of balls, d: direction
def move(p, d):

    niR, njR = p[0], p[1]
    niB, njB = p[2], p[3]

    # check balls can get out box
    cnt = 0
    while bd[niR + di[d]][njR + dj[d]] != '#' and bd[niR + di[d]][njR + dj[d]] != 'O':
        niR, njR = niR + di[d], njR + dj[d]
    if bd[niR + di[d]][njR + dj[d]] == 'O':
        cnt += 1

    while bd[niB + di[d]][njB + dj[d]] != '#' and bd[niB + di[d]][njB + dj[d]] != 'O':
        niB, njB = niB + di[d], njB + dj[d]
    if bd[niB + di[d]][njB + dj[d]] == 'O':
        cnt += 2

    # if some balls getted out
    if cnt > 0:
        return cnt, p

    # check balls are in same point
    if niR == niB and njR == njB:
        if d == 0:
            t1 = njR - 1 if p[1] < p[3] else njR
            t3 = njB if p[1] < p[3] else njB - 1
            p = [niR, t1, niB, t3]
        elif d == 1:
            t0 = niR - 1 if p[0] < p[2] else niR
            t2 = niB if p[0] < p[2] else niB - 1
            p = [t0, njR, t2, njB]
        elif d == 2:
            t1 = njR if p[1] < p[3] else njR + 1
            t3 = njB + 1 if p[1] < p[3] else njB
            p = [niR, t1, niB, t3]
        elif d == 3:
            t0 = niR if p[0] < p[2] else niR + 1
            t2 = niB+1 if p[0] < p[2] else niB
            p = [t0, njR, t2, njB]
    else:
        p = [niR, njR, niB, njB]

    return cnt, p


N, M = map(int, input().split())
bd = [list(input()) for _ in range(N)]

R, B = [], []
for i in range(N):
    for j in range(M):
        if bd[i][j] == 'R':
            R.append(i)
            R.append(j)
            bd[i][j] = '.'
        if bd[i][j] == 'B':
            B.append(i)
            B.append(j)
            bd[i][j] = '.'

res = 11
f(0, R[0], R[1], B[0], B[1], 0, -1)

if res == 11:
    res = -1
print(res)
