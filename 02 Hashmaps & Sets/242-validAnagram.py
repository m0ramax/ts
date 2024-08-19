#242-validAnagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s: str, t: str) -> bool:
    # if the length of the string are different they are not anagrams
    if len(s) != len(t):
        return False
    # save the quantity of each char into a hashmap
    seen = {}
    for char in (s):
        # acc = 0
        if char in seen:
            seen[char] +=1
        else: 
            seen[char] = 1 
    # check if the t string is in seen and same amount of letters
    for char in t:
        if char not in seen or seen[char] == 0:
            return False
        seen[char] -=1

    return True

print(isAnagram('salas','salsa'))
print(isAnagram('salas','salst'))
print(isAnagram('rac','cat'))
print(isAnagram('rat','tar'))