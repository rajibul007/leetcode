# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

def containsDuplicate(nums):
        distinctList = set(nums)
        if len(distinctList) != len(nums):
            return True 
        else:
            return False 
        
# #---------------
# 219. Contains Duplicate II

# Easy

# 2650

# 1946

# Add to List

# Share
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false


def containsNearbyDuplicate( nums , k):
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap and abs(hashmap[nums[i]] - i) <=k :
                 hashmap[nums[i]] = i 
                 return True
            hashmap[nums[i]] = i 
        return False
