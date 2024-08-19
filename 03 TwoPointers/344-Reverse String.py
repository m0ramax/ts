# # 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
 
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.

# The entire logic for reversing a string is based on using the opposite directional two-pointer approach!

def reverseString(s: list[str]) -> None:
        # more efficient way, my solution 170ms 
        n = len(s)
        l,r = 0, n -1
        while l < r:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1

        # Stack is more inefficient but another form 
        # Time: O(n)  Space: O(n)
        stack = []
        for c in s:
               stack.append(c)
        i = 0
        while stack:
               s[i] = stack.pop()
               i+=1


        # recursive is more inefficient but another form 
        # Time: O(n)  Space: O(n)
        def reverse(l,r):
                if l<r:
                     s[l],s[r] = s[r],s[l]
                     reverse(l+1,r-1)
        reverse(0,len(s)-1)
      
s = ["h","e","l","l","o"]
s1 = ["H","a","n","n","a","h"]
reverseString(s)
reverseString(s1)
print(s)
print(s1)