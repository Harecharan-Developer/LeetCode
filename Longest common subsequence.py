import numpy as np

class Solution:
    def longestCommonSubsequence(self, text1, text2) :

        rowval = "0" + text2
        colval = "0" + text1
        answer_subsequence=""

        dp = [[0 for _ in range(len(rowval))] for _ in range(len(colval))]

        for i in range(1, len(colval)):
            for j in range(1, len(rowval)):
                if colval[i] == rowval[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        transposed=np.transpose(dp)
        
        i_pointer=len(rowval)-1
        j_pointer=len(colval)-1


        while i_pointer>0 and j_pointer>0:
            curr=transposed[i_pointer][j_pointer]
            left=transposed[i_pointer][j_pointer-1]
            up=transposed[i_pointer-1][j_pointer]
            if curr==left:
                j_pointer-=1
            elif curr==up:
                i_pointer-=1
            elif curr!=left and curr!=up:
                answer_subsequence=rowval[i_pointer]+answer_subsequence
                j_pointer-=1
                i_pointer-=1
        print(answer_subsequence)

        for element in dp:
            for subelement in element:
                print(subelement,end=" ")
            print(" ")
        return dp[len(colval) - 1][len(rowval) - 1]
    



v=Solution()
print(v.longestCommonSubsequence("ABAZDC","BACBAD"))