# # 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

def longestCommonPrefix(strs: list[str]) -> str:
    print(sorted(strs)[0])
    print(sorted(strs)[-1])
    first_word = sorted(strs)[0]
    # print(first_word)
    last_word = sorted(strs)[-1]
    # print('last_word',last_word)
    # print(min(len(first_word), len(last_word)))
    ans = ""
    for i in range(min(len(first_word), len(last_word))):
        if first_word[i] != last_word[i]:
            return ans
        # print('< -- >')
        ans += first_word[i]
        # print(ans)
    return ans

print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["dog","racecar","car"]))


# @varunpatani
# hace 6 horas (editado)
# There is a better way to solve this problem 
# this would work best if your doing your leet in python 

# Initialize two variables 
# first_word = sorted(strs)[0]
# last_word = sorted(strs)[-1]

# what this will do is it will sort the "strs" list in order of the characters inside of it and then we can just compare each character of the first and last word in the sorted list 
# cause once we sort the list we wont have to worry about checking each character of each word

# then you can do something like this:
#        for i in range(min(len(first_word), len(last_word))):
#             if first_word[i] != last_word[i]:
#                 return ans
#             ans += first_word[i]
#         return ans

# remeber to initialize ans = ""  (as an empty string)