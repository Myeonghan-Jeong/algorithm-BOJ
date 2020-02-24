# 11651 / sort points ASC in y than x
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort(key=lambda point: (point[1], point[0]))
for point in points:
    print(point[0], point[1])
