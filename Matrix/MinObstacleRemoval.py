''' 
Hard
Topics
Companies
Hint
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
'''

# if eligible movements are only bottom and right, then we can use a 2D DP array to store the minimum number of obstacles to remove to reach each cell.
'''
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid) #rows
        n=len(grid[0]) #cols
        # dp=[[0]*n for _ in range(m)]
        # print(dp)
        for i in range(1,n):
            grid[0][i]+=grid[0][i-1]
        for i in range(m):
            grid[i][0]+=grid[i][i-1]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]

'''
# but this doesnt work cuz we can move in all 4 directions which means we need to keep track of the number of obstacles removed in each direction
from collections import deque
from typing import List
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Directions for movement (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Distance matrix to store minimum cost to reach each cell
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Deque for 0-1 BFS
        dq = deque([(0, 0)])
        
        while dq:
            x, y = dq.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check boundaries
                if 0 <= nx < m and 0 <= ny < n:
                    # Cost to move to (nx, ny)
                    new_cost = dist[x][y] + grid[nx][ny]
                    
                    # If we find a cheaper way to (nx, ny)
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        if grid[nx][ny] == 0:
                            dq.appendleft((nx, ny))  # Priority for empty cells
                        else:
                            dq.append((nx, ny))  # Obstacles go to the back
        print(dist[m-1][n-1])
        # Minimum cost to reach bottom-right corner
        return dist[m - 1][n - 1]
#example usage
sol = Solution()

sol.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]) #2
sol.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]) #0
