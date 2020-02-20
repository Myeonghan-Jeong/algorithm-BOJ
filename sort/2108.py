# 2108 / calculate avg, mid, the most appearance num, range of numbers
nums = [int(input()) for _ in range(int(input()))]

pop = {}
for num in nums:
    pop[num] = pop[num] + 1 if num in pop else 1
pop = sorted(pop.items(), key=lambda p: (p[1], p[0]))
pop = [num for num in pop if num[-1] == pop[-1][-1]]
if len(pop) > 1:  # if there is same cnt, return second least number
    pop = pop[1][0]
else:
    pop = pop[0][0]

avg = round(sum(nums) / len(nums))
mid = sorted(nums)[len(nums) // 2]
ran = max(nums) - min(nums)
for num in [avg, mid, pop, ran]:
    print(num)
