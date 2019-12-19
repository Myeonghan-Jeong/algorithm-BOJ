# 11502 / calculate max price to purchase N cards

'''
in DP, the most important thing is making ignition equ.

for example, for buy N cards if bought j cards the last
max price to buy N cards is D[N] = D[N - j] + P[j]

so, change this equ to ignition equ, for buy i cards
max price to buy i cards is D[i] = D[i - j] _ P[j]
'''

N = int(input())
P = [0] + list(map(int, input().split()))

D = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, i + 1):
        D[i] = max(D[i], D[i - j] + P[j])
print(D[-1])
