# 2839 / count bags to carry sugar
N = int(input())

# needed 5 bags, needed 3 bags, left sugar
share, rest, left = N // 5, N % 5 // 3, N % 5 % 3
bags = {3: rest, 5: share}
if left == 0:
    print(sum(bags.values()))
else:
    while True:
        # unpack 5 bags
        bags[5] -= 1
        if bags[5] < 0:  # if cannot pack all sugar
            print(-1)
            break

        # pack 3 bags and calculate left sugar
        bags[3] += (left + 5) // 3
        left = (left + 5) % 3
        if left == 0:
            print(sum(bags.values()))
            break
