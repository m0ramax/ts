# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
from collections import defaultdict

# that solution is from neetcode I really don't get it
# def groupAnagrams(strs:list[str]) -> list[list[str]]:
#     res = defaultdict(list)
#     print(res)
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c)-ord('a')] +=1
#         res[tuple(count)].append(s)
#     # print(res)
#     return res.values()

# so, im gonna try to solve on my own


def groupAnagrams(strs):
    res = {}
    # print(res)
    for s in strs:
        count = [0] * 26 # a .... z
        for c in s:
            # ord converts a char into a number (ASCII) value
            count[ord(c) - ord("a")] += 1
        key = tuple(count)
        print(key)
        res[key] = res.get(key, []) + [s]
    return list(res.values())

a = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(a)
