# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0
 

# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.

from collections import Counter
def maxNumberOfBalloons(text: str) -> int:
    hashMap = {}
    balloon ={}
    example = 'balloon'

    for n in text:
        hashMap[n] = 1+hashMap.get(n,0)
    for x in example:
        balloon[x] = 1 + balloon.get(n,0)

    res = len(text)
    for c in balloon:
        res = min(res, hashMap[c]// balloon[c] if c in hashMap else 0)
    return res
    # 25ms
    countText = Counter(text)
    balloon = Counter('balloon')
    res = len(text) # or float('inf')
    for c in balloon:
        res = min(res,countText[c]//balloon[c])
    return res
    
    
    # 36ms
    # a = 'balloon'
    # count = defaultdict(int) 
    # for char in text:
    #     if char in a:
    #         count[char] +=1
    
    # if any(char not in count for char in a):
    #     return 0
    # else:
    #     return min(count['b'], count['a'], count['l']//2, count['o']//2, count['n'])


print(maxNumberOfBalloons('nlaebolko')) # 1
print(maxNumberOfBalloons('loonbalxballpoon')) # 2
print(maxNumberOfBalloons('leetcode')) # 0