# 3052 / count amount of rests devided by 42
res = set()
for i in range(10):
    res.add(int(input()) % 42)

print(len(res))
