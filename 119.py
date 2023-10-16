class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        
        for i in range(1, rowIndex + 1):
            next_row = [1]  
            for j in range(1, i):
                next_row.append(dp[j - 1] + dp[j])
            next_row.append(1)
            dp = next_row 
        
        return dp
# 119. Pascal's Triangle II
# Solved
# Easy
# Topics
# Companies
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

