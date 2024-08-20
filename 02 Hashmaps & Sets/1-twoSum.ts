// # two sum
// # given an array = [1,2,3,4]
// # and an integer = 3
// # find the elements that sum that
// # in that case [0,1]

function twoSum(nums: number[], target: number): number[] {    
    const seen = new Map<number, number>()
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const complement = target - num;

        if (seen.has(complement)) {
            return [seen.get(complement)!, i];
        }

        seen.set(num, i);
    }
    return []
};