# from typing import List
# class Solution:
#     def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

#         row_dict={}
#         for row in range(len(matrix)):
#             row_dict[row]=row_dict.get(row,0)+len(matrix[row])-sum(matrix[row])
#         print(row_dict)
#         row_dict=sorted(row_dict,reverse=True)
#         key_,value_=row_dict[0],row_dict[1]
#         columns_to_change=matrix[key_]
#         for row in matrix:
#             for column in range(len(row)):
#                 if columns_to_change[column]==0:
#                     row[column]=1-row[column]
#         print(matrix)
#         answer=0
#         for row in matrix:
#             if sum(row)==len(row) or sum(row)==0:
#                 answer+=1
#         return answer
#above is my soluton which is not working for half of test cases
#below is the correct solution
'''
what im doing is finding the row with maximum different elements 
( like [0,0,0,1] and [0,1,0,1], latter has most 1s and 0s distributed count of 0s and 1s are closer to each other)
and then flipping the columns of that row and then checking if the other rows are equal to the flipped row or not

but this not always work because the row with most different elements may not be the row with most equal elements after flipping

so if we can just find max no of rows that are complement to each other
we get solution cuz
0,0,1,1 and 1,0,1,0 whichever column u flip u cannot get the other row to have 
same values cuz for one to get it other has to change and vice versa

'''

from typing import List
from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = Counter()
        
        for row in matrix:
            # Represent the row as a tuple
            normal = tuple(row)
            # Represent the complement of the row as another tuple
            complement = tuple(1 - cell for cell in row)
            
            # Increment the count of both patterns
            pattern_count[normal] += 1
            pattern_count[complement] += 1
        
        # Return the maximum count of identical rows
        return max(pattern_count.values())

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxEqualRowsAfterFlips([[0, 1], [1, 1]]))  # Output: 1
    print(solution.maxEqualRowsAfterFlips([[0, 1], [1, 0]]))  # Output: 2
    print(solution.maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]))  # Output: 2
    print(solution.maxEqualRowsAfterFlips([
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    ]))  # Output: 3



"""
1072. Flip Columns For Maximum Number of Equal Rows
Medium

You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.

"""