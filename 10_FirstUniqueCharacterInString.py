387. First Unique Character in a String
Easy

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1



class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {} 
        for i in range(len(s)):
            map[s[i]] = map.get(s[i],0) + 1
        for j in range(len(s)):
            if map[s[j]] == 1:
                return j
        return -1
            
        
        -------using python method 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
        
