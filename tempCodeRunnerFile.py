
def minEstimation (self, word1, word2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if word1[m-1] == word2[n-1]:
        return self.minEstimation(word1, word2, m-1, n-1)
    return 1 + min(self.minEstimation(word1, word2, m, n-1), self.minEstimation(word1, word2, m-1, n), self.minEstimation(word1, word2, m-1, n-1))