# Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    print(nums)
    closest = float('inf')
    
    for i in range(len(nums)-2):
        l = i+1
        r = len(nums) -1
        if i > 0 and nums[i-1] == nums[i]:
                continue
        
        while l < r:
            total = nums[i]+nums[l]+nums[r]
            a=abs(closest-target)
            b=abs(total-target)

            if total == target:
                return total
            
            if b < a:
                closest = total
            
            if total < target:
                l +=1
            else:
                r -= 1
    return closest

print(threeSumClosest([-1,2,1,-4],1)) #2
print(threeSumClosest([0,0,0],1)) # 0
# print(threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2)) #-2
# print(threeSumClosest([1,1,1,0],-100)) # 2
