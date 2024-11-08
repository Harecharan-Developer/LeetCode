from typing import List
from functools import reduce
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        totalXor = 0
        for num in nums:
            totalXor ^= num
        
        allOnes = (1 << maximumBit) - 1
        
        answer = []
        
        for num in reversed(nums):
            k = totalXor ^ allOnes
            answer.append(k)
            
            totalXor ^= num
        
        return answer
class Solution1:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer=[]
        allOnes = (1 << maximumBit) - 1
        temp_xor = reduce(lambda x, y: x ^ y, nums)
        while len(nums):            
            answer.append(temp_xor^allOnes)
            temp_xor ^= nums[-1]
            nums.pop()


        return answer


# The xor property is that a^b=c, then a^c=b and b^c=a.
# below is driver code for both

if __name__ == "__main__":

#     nums = [0,1,2,2,5,7]
#     maximumBit = 3
#     print(Solution().getMaximumXor(nums, maximumBit))
    
    nums = [0,1,2,2,5,7]
    maximumBit = 3
    print(Solution1().getMaximumXor(nums, maximumBit))
    
    nums = [2,3,4,7]
    maximumBit = 3
    print(Solution1().getMaximumXor(nums, maximumBit))

    nums = [0,1,2,2,5,7]
    maximumBit = 3
    print(Solution1().getMaximumXor(nums, maximumBit))

        
            


