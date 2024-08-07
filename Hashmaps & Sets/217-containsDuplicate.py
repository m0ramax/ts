# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# my way
def containsDuplicate1(nums: list[int]) -> bool:
    if len(nums) == 0: return False

    count = {} # hashmap to count occurrences
    for num in nums:
        if num in count:
            count[num] +=1
        else:
            count[num] = 1
        if num in count and count[num] >= 2:
            return True
    return False

# a more efficient way
def containsDuplicate(nums: list[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            print(hashset)  
            return True
        hashset.add(num)
        # print(hashset)  
    return False


print(containsDuplicate([1,3,4,5])) # should return false
print(containsDuplicate([1,2,3,1])) # should return true
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # should return true
