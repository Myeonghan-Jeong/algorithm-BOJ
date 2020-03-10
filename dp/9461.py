# 9461 / calculate Nth sea-wave number
tri = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
for i in range(10, 101):
    tri[i] = tri[i - 1] + tri[i - 5]

for _ in range(int(input())):
    print(tri[int(input())])
