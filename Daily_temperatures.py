# 739. Daily Temperatures
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

#brute force

class Solution:
    def dailyTemperatures(self, temperatures) :
        answer=[0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            counter=1
            
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    answer[i]=counter
                    break
                else:
                    counter+=1
        return answer




# efficien way 
#                 
class Solution1:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        
        return answer

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
solution = Solution()
solution1 = Solution1()

print(solution.dailyTemperatures(temperatures))
print(solution1.dailyTemperatures(temperatures))