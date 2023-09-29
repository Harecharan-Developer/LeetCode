# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true
# Example 2:

# Input: nums = [6,5,4,4]
# Output: true
# Example 3:

# Input: nums = [1,3,2]
# Output: false
 
class Solution:
    def isMonotonic(self, nums):
        x,y=0,0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                x+=1
            elif nums[i-1]>nums[i]:
                y+=1
            else:
                x+=1
                y+=1
        if x==len(nums)-1 or y==len(nums)-1:
            return True
        return False
x=Solution()
print (x.isMonotonic([1,1,1,1,2,2,2,2]))