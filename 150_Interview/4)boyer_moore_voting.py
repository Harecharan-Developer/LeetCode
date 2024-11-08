from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize candidate and count
        candidate = None
        count = 0
        
        # First pass: find the candidate for majority element
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Optionally, verify the candidate (not strictly necessary for O(1) space)
        # This step ensures correctness at the cost of slightly increased space complexity
        # count = nums.count(candidate)
        # return candidate if count > len(nums) // 2 else None
        
        return candidate
        # Driver code
if __name__ == "__main__":
    nums = [3, 2, 3]  # Example input
    solution = Solution()
    result = solution.majorityElement(nums)
    print(f"Majority element: {result}")