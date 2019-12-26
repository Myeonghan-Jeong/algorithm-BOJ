# 4673 / practice sieve of eratostenes
nums = [True] * 10001
for i in range(1, 10001):
    if nums[i]:
        print(i)
        n = i
        while True:  # calculate generator with given rule
            string = str(n)
            for s in string:
                n += int(s)
            if n > 10000:
                break
            nums[n] = False
