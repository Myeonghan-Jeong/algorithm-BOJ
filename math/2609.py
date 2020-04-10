# 2609 / calculate GCD, LCM with special equation
a, b = map(int, input().split())
a, b = max(a, b), min(a, b)

ta, tb = a, b
gcd, lcm = None, None
while True:
    if ta % tb == 0:
        gcd, lcm = tb, a * b // tb
        for _ in [gcd, lcm]:
            print(_)
        break
    else:
        ta, tb = tb, ta % tb  # euclidean algorithm
