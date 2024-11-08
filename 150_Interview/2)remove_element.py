from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
        
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0  # Pointer to place the next non-val element
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        
        return left
nums = [3, 2, 2, 3]
val = 3

solution = Solution()
result = solution.removeElement(nums, val)
print(result)

solution1 = Solution1()
result1 = solution1.removeElement(nums, val)
print(result1)