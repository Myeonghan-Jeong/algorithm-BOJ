# 14889 / calculate min diff of team start and team link
from collections import deque

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

res = float('inf')
for i in range(1 << N):
    start, link = deque(), deque()  # devide teams
    for j in range(N):
        if i & (1 << j):
            start.append(j)
        else:
            link.append(j)

    if len(start) > 1 and len(link) > 1:  # calculate sum of score
        s = 0
        for i in range(len(start)):
            for j in range(i + 1, len(start)):
                s += people[start[i]][start[j]] + people[start[j]][start[i]]
        l = 0
        for i in range(len(link)):
            for j in range(i + 1, len(link)):
                l += people[link[i]][link[j]] + people[link[j]][link[i]]
        diff = abs(s - l)
        if res > diff:
            res = diff
print(res)
