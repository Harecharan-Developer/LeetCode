from itertools import combinations

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(s) == len(set(s))

        max_length = 0

        for r in range(1, len(arr) + 1):
            for combination in combinations(arr, r):
                current_str = ''.join(combination)
                if is_unique(current_str):
                    max_length = max(max_length, len(current_str))

        return max_length

solution = Solution()
arr1 = ["un", "iq", "ue"]
arr2 = ["cha", "r", "act", "ers"]
arr3 = ["abcdefghijklmnopqrstuvwxyz"]

print(solution.maxLength(arr1))  # Output: 4
print(solution.maxLength(arr2))  # Output: 6
print(solution.maxLength(arr3))  # Output: 26