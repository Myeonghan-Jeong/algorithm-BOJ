# 14681 / find quadrant of point (x, y)
x, y = int(input()), int(input())
if x * y > 0:
    print(1) if x > 0 else print(3)
else:
    print(2) if x < 0 else print(4)
