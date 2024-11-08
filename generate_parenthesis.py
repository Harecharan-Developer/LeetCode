
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        dp = [[] for _ in range(n+1)]
        #print dp
        print("dp=",dp)
        dp[0] = ['']
        
        for i in range(1, n+1):
            for j in range(i):
                left = dp[j]
                right = dp[i-j-1]
                print("left=" , left)
                print("right=" , right)
                
                for l in left:
                    for r in right:
                        dp[i].append('(' + l + ')' + r)
                        print("l=" , l)
                        print("r=" , r)
                        print("dp[i]=",dp[i])
                        print("dp",dp)
        
        return dp[i]
solution = Solution()
n = 3  # Replace with the desired value of n
result = solution.generateParenthesis(n)
print(result)