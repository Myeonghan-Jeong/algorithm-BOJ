# 1085 / calculate min diff of length
x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))
