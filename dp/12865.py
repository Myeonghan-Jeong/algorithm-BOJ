# 12865 / calculate max value of bag with 0/1 Knapsack
N, K = map(int, input().split())  # number of items, max weight of bag
items = [list(map(int, input().split())) for _ in range(N)]

bag = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    W, V = items[i - 1]  # checking item
    for j in range(1, K + 1):
        # compare weight of bag and item
        # if bag is heavier, put more items in left area
        # if item is heavier, bag cannot put any item
        put = V + bag[i - 1][j - W] if j >= W else 0
        bag[i][j] = max(bag[i - 1][j], put)  # compare previous value and now
print(bag[-1][-1])
