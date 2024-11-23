from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in range(len(box)):
            for col in range(len(box[row]) - 1, -1, -1):
                if box[row][col] == "#":
                    r, c = row, col
                    while c + 1 < len(box[row]) and box[r][c + 1] == ".":
                        box[r][c], box[r][c + 1] = box[r][c + 1], box[r][c]
                        c += 1
        
        # Initialize the rotated box with the correct dimensions
        rotatedbox = [[0] * len(box) for _ in range(len(box[0]))]
        
        # Rotate the box 90 degrees clockwise
        for i in range(len(box)):
            for j in range(len(box[0])):
                rotatedbox[j][len(box) - 1 - i] = box[i][j]
        
        return rotatedbox

# Example usage
if __name__ == "__main__":
    solution = Solution()
    box = [["#", ".", "#"], ["#", ".", "#"], ["#", ".", "#"]]
    print(solution.rotateTheBox(box))


'''
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.
'''