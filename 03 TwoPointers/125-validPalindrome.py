# 125-validPalindrome.py
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "racaecar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


def isPalindrome(s: str) -> bool:
    n = len(s)
    L = 0
    R = n -1

    while L < R:
        if not s[L].isalnum():
            L +=1
            continue
        if not s[R].isalnum():
            R -=1
            continue
        if s[L].lower() != s[R].lower():
            return False
        L =+1
        R -=1
    return True

    # s1 = "".join(c.lower() for c in s if c.isalpha())
    s1=[c.lower() for c in s if c.isalnum()]
    print(s1)
    l = 0
    r = len(s1) - 1
    while l < r:
        # print(l)
        # print(r)
        if (s1[l] != s1[r]) :
            return False
        l +=1
        r -=1
    return True

    # str_cleaned = ''.join(char.lower() for char in s if char.isalpha())
    # # Compare forward to backward
    # return str_cleaned == str_cleaned[::-1]


print(isPalindrome("0SALas! , @ #")) # true
# print(isPalindrome("race a car")) # false
# print(isPalindrome(" ")) # true
# print(isPalindrome("A man, a plan, a canal: Panama")) #true
# print(isPalindrome("0P")) #false
