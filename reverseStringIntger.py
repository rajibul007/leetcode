Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 

-----------------------------------------------------------


class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0 
        r = len(s) -1 
        while(l<r):
            s[l] , s[r] = s[r] , s[l]
            l = l + 1
            r = r - 1 
        
    
    
    --------------------------
 
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 

Constraints:

    -231 <= x <= 231 - 1





class Solution:
    def reverse(self, x: int) -> int:
        sign = [1,-1][x<0]
        final = 0 
        strnum = str(abs(x))
        #print(strnum , strnum[::-1])
        final = sign*int(strnum[::-1])
        if -(2**31) <= final <= 2**31 -1 :
            return final
        else:
            return 0
           
    
