# # 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

def sortedSquares(nums: list[int]) -> list[int]:
    #  that works in an inefficient way
    # res = []
    # for i in nums:
    #     res.append(pow(i,2))
    # res.sort()
    # return res

    # using two pointers 142ms 18.9MB
    n = len(nums)
    left, right = 0, n -1
    res = [0] * n
    pos = n -1

    while left <= right:
        lef_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if lef_square > right_square:
            res[pos] = lef_square
            left +=1
        else:
            res[pos] = right_square
            right -=1
        pos -=1
    return res
    
print(sortedSquares([-4,-1,0,3,10]))    