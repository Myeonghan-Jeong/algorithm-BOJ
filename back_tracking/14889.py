# 14889 / calculate min diff of team start and team link
from itertools import combinations

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
teams = list(combinations(range(N), N // 2))  # use combination

res = float('INF')
for team in teams:
    start, link = team, tuple(set(range(N)) - set(team))

    r1 = 0  # calculate sum of each team
    for p1 in start:
        for p2 in start:
            if p1 != p2:
                r1 += people[p1][p2]

    r2 = 0
    for q1 in link:
        for q2 in link:
            if q1 != q2:
                r2 += people[q1][q2]

    diff = abs(r1 - r2)  # check diff
    if res > diff:
        res = diff

print(res)
