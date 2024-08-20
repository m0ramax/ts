// # Given an integer array nums of size n, 
// # return the number with the value closest to 0 in nums. 
// # If there are multiple answers, return the number with the largest value.

// # E# res = []xample 1:
// # Input: nums = [-4,-2,1,4,8]
// # Output: 1
// # Explanation:
// # The distance from -4 to 0 is |-4| = 4.
// # The distance from -2 to 0 is |-2| = 2.
// # The distance from 1 to 0 is |1| = 1.
// # The distance from 4 to 0 is |4| = 4.
// # The distance from 8 to 0 is |8| = 8.
// # Thus, the closest number to 0 in the array is 1.

// # Example 2:
// # Input: nums = [2,-1,1]
// # Output: 1
// # Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

// def findClosestNumber(nums: list[int]) -> int:
//     closest = nums[0]
//     for x in nums:
//         if abs(x) < abs(closest):
//             closest = x
//     if closest < 0 and abs(closest) in nums:
//         return abs(closest)
//     else:
//         return closest

// print(findClosestNumber([-100000,-100000]))
// print(findClosestNumber([-4,-2,1,4,8]))
function findClosestNumber(nums: number[]): number {
    let closest = nums[0]
    for(let i = 1; i < nums.length; i++){
      const num = nums[i]
      if (Math.abs(num) < Math.abs(closest)){
        closest = num
      } else if (Math.abs(num) === Math.abs(closest) && num > closest ){
        closest = num
      }
    }
    return closest
  };
  
  findClosestNumber([-4,-2,1,4,8])