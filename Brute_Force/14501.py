# 14501 / calculate max profit that can earn
def find(idx, money, N):
    global moneys

    if idx == N:
        return money
    elif idx > N:
        return 0

    p = find(idx + moneys[idx][0], money + moneys[idx][1], N)  # if picked
    q = find(idx + 1, money, N)  # if not picked
    return max(p, q)


N = int(input())
moneys = [[]] * N
for _ in range(N):
    moneys[_] = list(map(int, input().split()))

print(find(0, 0, N))
