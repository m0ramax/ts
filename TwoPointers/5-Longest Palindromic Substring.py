# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

def longestPalindrome(s: str) -> str:
    res = ''
    resLen = 0 # longest
    for i in range(len(s)):
        # odd
        l,r=i,i
        # print(l,r)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if( r- l +1) > resLen:
                res = s[l:r+1]
                resLen = r -l+1
            l -=1
            r +=1
        # even
        l,r = i, i+1
        isPalindrome(res, s, l,r)
    return res
       
def isPalindrome(res,s,l,r):
     while l>=0 and r < len(s) and s[l]==s[r]:
        if r -l + 1> resLen:
            res = s[l:r+1]
            resLen = r -l +1
        l -=1
        r +=1

print(longestPalindrome('babad'))
print(longestPalindrome("cbbd"))