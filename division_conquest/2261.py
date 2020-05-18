# 2261 / calculate min distance of two points
import sys


def dist(a, b, c, d):  # calculate dist
    return (a - c) ** 2 + (b - d) ** 2


def div(s, e):
    global points

    l = e - s
    if l == 2:  # if there is two points
        return dist(*points[s], *points[s + 1])
    elif l == 3:  # if there is three points
        return min(dist(*points[s], *points[s + 1]), dist(*points[s + 1], *points[s + 2]), dist(*points[s], *points[s + 2]))

    m = (s + e) // 2  # set mid line
    far = min(div(s, m), div(m, e))  # calculate min dist of each division

    mid, tmp = points[m][0], []
    for i in range(s, e):  # find targets closer than dist
        if (mid - points[i][0]) ** 2 <= far:
            tmp.append(points[i])
    tmp.sort(key=lambda x: x[1])

    tmp_len = len(tmp)
    if tmp_len >= 2:
        for i in range(tmp_len - 1):
            for j in range(i + 1, tmp_len):
                if (tmp[i][1] - tmp[j][1]) ** 2 > far:  # if dist of y is far than res
                    break
                elif tmp[i][0] < mid and tmp[j][0] < mid:  # if two points in same side
                    continue
                elif tmp[i][0] > mid and tmp[j][0] > mid:
                    continue
                # if two points in other sides
                far = min(far, dist(*tmp[i], *tmp[j]))

    return far


arr = []
for _ in range(int(input())):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

points = list(set(arr))
if len(points) != len(arr):  # if len is diff, duplicated points dist is 0
    print(0)
else:  # else
    points.sort()  # sort points with x
    print(div(0, len(points)))
