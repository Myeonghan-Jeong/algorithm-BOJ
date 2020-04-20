# 2004 / count 0 from behind of nCm
def count(num, fac):
    ans = 0
    while num != 0:
        num //= fac  # div num with fac
        ans += num  # add num of fac
    return ans


n, m = map(int, input().split())
if m == 0 or m == n:
    print(0)
else:
    # num of 0 is same as min of num of 2 or 5(div is same as minus)
    fives = count(n, 5) - count(m, 5) - count(n - m, 5)
    twos = count(n, 2) - count(m, 2) - count(n - m, 2)
    print(min(fives, twos))
