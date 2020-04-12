# 3036 / calculate turn of each rings when first ring spin 1 cycle
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while True:
        a, b = b, a % b
        if b == 0:
            return a


N = int(input())
rings = list(map(int, input().split()))
for ring in rings[1:]:
    g = gcd(rings[0], ring)
    print(f'{rings[0] // g}/{ring // g}')
