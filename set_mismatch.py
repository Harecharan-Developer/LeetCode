# 645. Set Mismatch
# Solved
# Easy
# Topics
# Companies
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
 

class Solution:
    def findErrorNums(self, nums):
        nums.sort()
        repeated_num = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                repeated_num = nums[i]
                break
        nums_set = set(nums)
        nums_range = set(range(1, len(nums) + 1))
        missing_num = nums_range.difference(nums_set).pop()
        
        return [repeated_num, missing_num]
# Create an instance of the Solution class
solution = Solution()

# Test case 1
nums1 = [1, 2, 2, 4]
result1 = solution.findErrorNums(nums1)
print(result1)  # Output: [2, 3]

# Test case 2
nums2 = [1, 1]
result2 = solution.findErrorNums(nums2)
print(result2)  # Output: [1, 2]
