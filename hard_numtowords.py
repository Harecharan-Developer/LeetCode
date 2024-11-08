class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones_dict = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
        }
        teens_dict = {
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
        }
        tens_dict = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }
        thousands_dict = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return []
            if n < 10:
                return [ones_dict[n]]
            elif n < 20:
                return [teens_dict[n]]
            elif n < 100:
                return [tens_dict[n // 10]] + helper(n % 10)
            else:
                return [ones_dict[n // 100]] + ["Hundred"] + helper(n % 100)

        answer = []
        for i, chunk in enumerate(self.split_by_thousands(num)):
            if chunk > 0:
                answer = helper(chunk) + [thousands_dict[i]] + answer
        return ' '.join(answer).strip()

    def split_by_thousands(self, num):
        chunks = []
        while num > 0:
            chunks.append(num % 1000)
            num //= 1000
        return chunks

# Example usage
sol = Solution()
print(sol.numberToWords(1234567))  # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
