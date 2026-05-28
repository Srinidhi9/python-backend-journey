def twoSum(nums, target):
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in prevMap:
            return [prevMap[diff], i]

        prevMap[n] = i


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))