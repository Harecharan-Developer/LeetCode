# 135. Candy
# Solved
# Hard
# Topics
# Companies
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

 

# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.



# my solution but it only passes 25 test cases using dp greedy algorithm logic
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         dp=[1 for i in range(len(ratings))]
#         for i in range(1,len(ratings)):
#             curr=i
#             prev=i-1
#             if ratings[curr]>ratings[prev]:
#                 if not dp[curr]>dp[prev]:
#                     dp[curr]=dp[prev]+1
#             elif ratings[curr]<ratings[prev]:
#                 if not dp[prev]>dp[curr]:
#                     dp[prev]=dp[curr]+1
#         return sum(dp)


from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Initialize each child with 1 candy

        # Left-to-right pass: Ensure right neighbors have more candies if their rating is higher
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-left pass: Ensure left neighbors have more candies if their rating is higher
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Sum up the total candies
        total_candies = sum(candies)

        return total_candies

# Test the class-based solution
ratings = [1, 2, 87, 87, 87, 2, 1]
solution = Solution()
result = solution.candy(ratings)
print(result)  # Output should be 13
