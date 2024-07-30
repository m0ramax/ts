# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false


# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.


def isSubsequence(s: str, t: str) -> bool:
    S = len(s)
    T = len(t)

    if s == "":
        return True
    if S > T:
        return False
    j = 0
    for i in range(T):
        if t[i] == s[j]:
            if j == S - 1:
                return True
            j += 1
    return False

    # ese era mi enfoque pero no cumplia los casos borde
    # l,r=0,len(t)-1
    # aux = [i for i in s] # convert string into a list
    # aux1 = [i for i in t]
    # aux1.sort() # sort list to match after

    # if len(aux) == 0 and len(aux1) > 0:
    #     # print('here')
    #     return False

    # while l < r:
    #     if aux[l] not in aux1:
    #         l += 1
    #         r -= 1
    #         return False
    #     # if aux[l] in aux1:
    #     #     # print(aux[l])
    #     #     l += 1
    #     #     r -= 1
    #     #     continue
    #     else:
    #         return True
    # # return True


print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("", "ahbgdc"))
print(isSubsequence("", ""))
print(isSubsequence("b", "c"))
