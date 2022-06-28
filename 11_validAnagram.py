Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS,countT = {} , {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1 
            countT[t[i]] = countT.get(t[i],0) + 1 
        for i in t:
            if countT[i] != countS.get(i,0):
                 return False
        return True 
