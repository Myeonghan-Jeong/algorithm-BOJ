# 1002 / find joint points in two circles
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    l = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    R, r = r1 + r2, abs(r1 - r2)
    if l == 0 and r == 0:  # two circles are same
        print(-1)
    elif l > R or (l < r != 0):  # two circles cannot joint
        print(0)
    elif l == R or l == r:  # two circles joint one point
        print(1)
    else:
        print(2)
