from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs = float('inf')
        negative_count = 0

        # Traverse the matrix
        for row in matrix:
            for value in row:
                total_sum += abs(value)  # Add absolute value to the total sum
                min_abs = min(min_abs, abs(value))  # Track the smallest absolute value
                if value < 0:
                    negative_count += 1  # Count negatives

        # If the total number of negatives is odd, subtract twice the smallest absolute value
        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs

        return total_sum
#example code to run 
solution=Solution()
matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
print(solution.maxMatrixSum(matrix)) # 16
matrix = [[-1,0,-1],[-2,-3,-3],[-1,-2,-3]]
print(solution.maxMatrixSum(matrix)) # 16
matrix = [[1,-1],[-1,1]]
print(solution.maxMatrixSum(matrix)) # 4
matrix = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-3]]
print(solution.maxMatrixSum(matrix)) # 21
matrix = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-3]]
print(solution.maxMatrixSum(matrix)) # 21
