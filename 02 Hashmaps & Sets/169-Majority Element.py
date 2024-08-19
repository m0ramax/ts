# # 169. Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 
# Follow-up: Could you solve the problem in linear time and in O(1) space?
def majorityElement(nums: list[int]) -> int:
    # my solution, inefficient way  5958ms 18MB
    # n = len(nums)//2
    # count = {}
    # for i in nums:
    #     if i in nums:
    #         count[i] = count.get(i, 0) +1
    # for v, c in count.items():
    #     if c > n:
    #         return v

    # 183ms 18MB
    # count = {}
    # res, maxCount = 0 , 0

    # for n in nums:
    #     count[n] = 1 + count.get(n,0)
    #     res = n if count[n] > maxCount else res
    #     maxCount = max(count[n], maxCount)
    # return res

# boyer_moore algorithm  172ms 18MB
    res, count  = 0,0
    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res


print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
