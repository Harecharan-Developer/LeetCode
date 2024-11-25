from typing import List, Tuple

class Node:
    def __init__(self, position: Tuple[int, int], value: int, neighbours: List[Tuple[int, int]]):
        self.pos = position
        self.val = value
        self.near = neighbours

class Graph:
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.graph = {}
        self.rows = len(board)
        self.cols = len(board[0])

    def create_graph(self):
        for i in range(self.rows):
            for j in range(self.cols):
                neighbours = []
                if i > 0:  # Up
                    neighbours.append((i - 1, j))
                if i < self.rows - 1:  # Down
                    neighbours.append((i + 1, j))
                if j > 0:  # Left
                    neighbours.append((i, j - 1))
                if j < self.cols - 1:  # Right
                    neighbours.append((i, j + 1))
                node = Node((i, j), self.board[i][j], neighbours)
                self.graph[(i, j)] = node

    def bfs(self):
        # Find the initial position of '0'
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    start = (i, j)

        # Initialize BFS
        q = [((start, self.board), 0)]  # ((position of 0, current board), steps)
        visited = set()
        visited.add(self.board_to_tuple(self.board))
        target = [[1, 2, 3], [4, 5, 0]]  # Goal state

        while q:
            (zero_pos, current_board), steps = q.pop(0)

            # If we reached the target
            if current_board == target:
                return steps

            # Iterate through neighbors of zero
            for neighbor in self.graph[zero_pos].near:
                new_board = [row[:] for row in current_board]  # Copy current board
                # Swap 0 with the neighbor
                ni, nj = neighbor
                zi, zj = zero_pos
                new_board[zi][zj], new_board[ni][nj] = new_board[ni][nj], new_board[zi][zj]

                # Check if this state is already visited
                board_tuple = self.board_to_tuple(new_board)
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    q.append(((neighbor, new_board), steps + 1))

        return -1  # If BFS completes without finding the target state

    @staticmethod
    def board_to_tuple(board: List[List[int]]) -> Tuple[Tuple[int]]:
        return tuple(tuple(row) for row in board)

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        g = Graph(board)
        g.create_graph()
        return g.bfs()



# Example usage
if __name__ == "__main__":
    solution = Solution()
    board = [[1, 2, 3], [4, 0, 5]]
    print(solution.slidingPuzzle(board))  # Output: 1

    board = [[1, 2, 3], [5, 4, 0]]
    print(solution.slidingPuzzle(board))  # Output: -1

    board = [[4, 1, 2], [5, 0, 3]]
    print(solution.slidingPuzzle(board))  # Output: 5

    board = [[3, 2, 4], [1, 5, 0]]
    print(solution.slidingPuzzle(board))  # Output: 14
'''
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
'''