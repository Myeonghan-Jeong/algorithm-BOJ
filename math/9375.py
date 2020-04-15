# 9375 / calculate all kinds of pashion
for _ in range(int(input())):
    clothes = {}
    for _ in range(int(input())):
        name, code = input().split()
        if code in clothes:
            clothes[code].append(name)
        else:
            clothes[code] = [name]

    res = 1
    for items in clothes.values():
        res *= len(items) + 1  # plus kind of no item
    print(res - 1)  # del kind of no cloth
