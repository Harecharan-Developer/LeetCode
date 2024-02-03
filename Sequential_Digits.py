# 1291. Sequential Digits
# Medium
# Topics
# Companies
# Hint
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.


class Solution:
    def sequentialDigits(self, low, high) :
        num_list=['1','2','3','4','5','6','7','8','9']
        low_digits=len(str(low))
        high_digits=len(str(high))

        result=[]
        for i in range(low_digits,high_digits+1):
            for j in range(10-i):
                concat_string=''.join(num_list[j:j+i])
                result.append(int(concat_string))
        return result
sol=Solution()
print(sol.sequentialDigits(100,300)) # [123,234]