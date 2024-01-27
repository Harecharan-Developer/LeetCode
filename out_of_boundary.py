# 576. Out of Boundary Paths
# Medium
# Topics
# Companies
# Hint
# There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

# Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.


''' 
Only 34 testcases Passed need to update
'''


class my_solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def is_edge(x, y):
            if (x == 0 or x == m - 1) and (0 < y < n - 1):
                return True
            if (y == 0 or y == n - 1) and (0 < x < m - 1):
                return True
            return False

        def is_corner(x, y):
            return (x == 0 or x == m - 1) and (y == 0 or y == n - 1)

        def in_bounds(x, y):
            return 0 <= x < m and 0 <= y < n
        
        arr = [[] for _ in range(maxMove)]
        print("arr: ", arr)
        arr[-1] = [(startRow, startColumn)]
        print("arr: ", arr)

        for i in range(maxMove -2 , -1, -1):
            for j in arr[i + 1]:
                x, y = j[0], j[1]
                if in_bounds(x + 1, y):
                    arr[i].append((x + 1, y))
                if in_bounds(x - 1, y):
                    arr[i].append((x - 1, y))
                if in_bounds(x, y + 1):
                    arr[i].append((x, y + 1))
                if in_bounds(x, y - 1):
                    arr[i].append((x, y - 1))
            print("arr: ", arr)

        count = 0
        for positions in arr:
            for x, y in positions:
                if is_edge(x, y):
                    if m==1:
                        count += 2
                    else:
                        count += 1
                elif is_corner(x, y):
                    if m==1 and n!=1:
                        count += 3  
                    elif m!=1 and n==1:
                        count += 3
                    elif m==1 and n==1:
                        count += 4
                    else:
                        count += 2
        return count

# Test the my_solution
my_solution = my_solution()
print(my_solution.findPaths(2, 2, 2, 0, 0))  # Output: 6
print(my_solution.findPaths(1, 3, 3, 0, 1))    # Output: 12

from functools import lru_cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def rec(i,j,moves):
            if i>=m or j>=n or i<0 or j<0:
                return 1
            elif moves == 0:
                return 0
            out = rec(i+1,j,moves-1)
            out += rec(i-1,j,moves-1)
            out += rec(i,j+1,moves-1)
            out += rec(i,j-1,moves-1)
            return out
        return rec(startRow,startColumn,maxMove) % (10**9+7)

# Test the my_solution
solution = Solution()
print(solution.findPaths(2, 2, 2, 0, 0))  # Output: 6
print(solution.findPaths(1, 3, 3, 0, 1))    # Output: 12