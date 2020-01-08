# 2908 / compare reversed numbers
nums = input().split()
nums[0], nums[1] = int(nums[0][::-1]), int(nums[1][::-1])

print(nums[0]) if nums[0] > nums[1] else print(nums[1])
