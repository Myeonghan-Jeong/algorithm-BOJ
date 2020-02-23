# 11650 / sort points ASC
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort(key=lambda point: (point[0], point[1]))
for point in points:
    print(point[0], point[1])
