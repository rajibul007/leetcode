# Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]



-------


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer_one = 0 # to check 0 
        
        for pointer_two in range(len(nums)): # to iterate 
            if nums[pointer_two] != 0 :
                nums[pointer_two] , nums[pointer_one] = nums[pointer_one] , nums[pointer_two]
                pointer_one += 1
        return nums
               
        
