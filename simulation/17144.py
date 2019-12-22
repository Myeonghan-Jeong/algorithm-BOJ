# 17144 / count left dusts in the room
def check():  # find initial dusts
    global R, C, air

    top, bottom, dusts = (), (), {}
    for i in range(R):
        for j in range(C):
            if air[i][j] >= 1:
                dusts[(i, j)] = air[i][j]
            elif not top and not bottom and air[i][j] == -1:
                top = (i, j)
                bottom = (i + 1, j)

    return top, bottom, dusts


def div_and_sum(dusts):
    global R, C, air, new_dusts

    for key, val in dusts.items():
        i, j = key
        cut = 0

        # divide all dusts
        temp_dusts = []
        if val >= 5:
            for di, dj in D:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and air[ni][nj] != -1:
                    temp_dusts.append((ni, nj, val // 5))
                    cut += 1

        if val - (val // 5) * cut > 0:
            temp_dusts.append((i, j, val - (val // 5) * cut))

        # add divided dusts in the dust dict
        for temp_dust in temp_dusts:
            i, j, val = temp_dust

            if (i, j) not in new_dusts:
                new_dusts[(i, j)] = val
            else:
                new_dusts[(i, j)] += val


D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

R, C, T = map(int, input().split())
air = [list(map(int, input().split())) for _ in range(R)]

top, bottom, dusts = check()

while T > 0:
    new_dusts = {}
    div_and_sum(dusts)

    air = [[0] * C for _ in range(R)]
    for key, val in new_dusts.items():
        i, j = key

        # circulation air
        if j == 0:
            if 0 <= i < top[0] - 1:
                air[i + 1][j] = val
            elif bottom[0] + 1 < i < R:
                air[i - 1][j] = val
        elif j == C - 1:
            if i == 0:
                air[i][j - 1] = val
            elif 0 < i <= top[0]:
                air[i - 1][j] = val
            elif bottom[0] <= i < R - 1:
                air[i + 1][j] = val
            elif i == R - 1:
                air[i][j - 1] = val
        else:
            if i == 0 or i == R - 1:
                air[i][j - 1] = val
            elif i == top[0] or i == bottom[0]:
                air[i][j + 1] = val
            else:
                air[i][j] = val

    dusts = check()[-1]
    T -= 1

# count
cnt = 0
for i in range(R):
    for j in range(C):
        if air[i][j] > 0:
            cnt += air[i][j]

print(cnt)
