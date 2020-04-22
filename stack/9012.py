# 9012 / check VPS
def f(ps):
    s = []
    for p in ps:
        if p == '(':
            s.append(p)
        else:
            if len(s) == 0:
                return 'NO'
            else:
                s.pop()

    if len(s) == 0:
        return 'YES'
    else:
        return 'NO'


for _ in range(int(input())):
    print(f(list(input())))
