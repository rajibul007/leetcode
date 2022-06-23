
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false





class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = sorted(s)
        b = sorted(t)
        if a == b :
            return True
        else:
            return False   

--------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS , countT = {} , {}
        for i in range(len(s)):
            if s[i] in countS:
                countS[s[i]] = countS[s[i]] + 1  
            else:
                countS[s[i]] = 1   
            if t[i]  in countT:
                countT[t[i]] = countT[t[i]] + 1    
            else:
                countT[t[i]] = 1             
        print(countS , countT)
        for i in  countS:
            if countS[i] != countT.get(i,0):
               return False    
        return True    
        
        
        
