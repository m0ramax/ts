# # 383. Ransom Note
# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true 
 

# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

def canConstruct(ransomNote: str, magazine: str) -> bool:
    # 41ms
    for l in set(ransomNote):
            if ransomNote.count(l) > magazine.count(l):
                return False
    return True
    # 52 ms
    # d = defaultdict(int)
    # for char in magazine:
    #     d[char] +=1
    # for char in ransomNote:
    #     if char not in d or d[char] <= 0:
    #         return False
    #     d[char] -=1
    # return True

    # 69ms
    # seen={}
    # for char in magazine:
    #     if char in ransomNote:
    #         seen[char] = seen.get(char,0)+1

    # for char in ransomNote:
    #     if char not in seen:
    #         return False
    #     elif seen[char] ==1:
    #         del seen[char]
    #     else:
    #         seen[char] -=1
    # return True

print(canConstruct('a','b'))
print(canConstruct('aa','ab'))
print(canConstruct('aa','aab'))
print(canConstruct("fihjjjjei","hjibagacbhadfaefdjaeaebgi"))