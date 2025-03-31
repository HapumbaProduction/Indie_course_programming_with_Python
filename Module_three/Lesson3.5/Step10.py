print((lambda nums: 3 if nums[0] == nums[1] == nums[2] else 2 if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2] else 0)([int(input()) for _ in range(3)]))
