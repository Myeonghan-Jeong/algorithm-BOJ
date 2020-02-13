# 7568 / rank size of person
N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]  # size of people
for i in range(N):
    rank = 1
    for j in range(N):
        a, b = people[i], people[j]
        if a[0] < b[0] and a[1] < b[1]:  # if people is samller
            rank += 1
    print(rank, end=' ')
