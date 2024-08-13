# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# 𝑂(1)
# O(1) additional space.

# Input: numbers = [1,2,3,4], target = 3
# Output: [1,2]
def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) -1
    while left < right:
        res = numbers[left] + numbers[right] 
        if res == target:
            return [left+1, right+1]
        elif res < target:
            left +=1
        else:
            right -=1    

print(twoSum([1,2,3,4],3))



   # res = []
    # nums.sort()
    # for i, a in enumerate(nums):
    #     if i > 0 and a == nums[i-1]:
    #         continue
    #     l,r = i+1, len(nums) -1
    #     while l < r:
    #         threeSum = a +  nums[l] + nums[r]
    #         if threeSum > 0:
    #             r -=1
    #         elif threeSum < 0:
    #             l +=1
    #         else:
    #             res.append([a, nums[l], nums[r]])
    #             l+=1
    #             while(nums[1] ==nums[l -1] and l < r):
    #                 l +=1
    # return res