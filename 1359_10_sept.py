# 1359. Count All Valid Pickup and Delivery Options
# Hard
# 2K
# 164
# Companies
# Given n orders, each order consist in pickup and delivery services. 

# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

# Since the answer may be too large, return it modulo 10^9 + 7.

#  my solution seemed logical but only 10 test cases ;-)

# import math
# class Solution:
#     def countOrders(self, n: int) -> int:
#         return int((math.factorial(2*n)/(pow(2,n)))%(pow(10,9)+7))

# gpt solution

def countOrders(n):
    MOD = 10**9 + 7

    # Initialize a dynamic programming array dp, where dp[i] represents the number
    # of valid sequences for i pairs of pickups and deliveries.
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: there's one way to deliver 0 pairs (no pairs).

    for i in range(1, n + 1):
        # To find dp[i], we consider inserting the i-th pair.
        # There are three steps: pick up, deliver, and insert the new pair.
        # For each pair, there are 2*i - 1 positions to insert it.
        dp[i] = (dp[i - 1] * (2 * i - 1) * (2 * i)) % MOD

    return dp[n]

# Example usage:
n = 3
print(countOrders(n))  # Output: 90
