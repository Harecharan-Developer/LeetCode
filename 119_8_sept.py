#118. Pascal's Triangle

#Given an integer numRows, return the first numRows of Pascal's triangle.

#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []

        output = [[1]]
        
        for i in range(1, numRows):
            prev = output[-1]
            l1= [1]

            for j in range(1, i):
                l1.append(prev[j - 1] + prev[j])

            l1.append(1)
            output.append(l1)

        return output

 