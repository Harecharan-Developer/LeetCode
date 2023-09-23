
# 1048. Longest String Chain
# Medium
# Topics
# Companies
# Hint
# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.

# works only for test cases. tle 

class Solution:
    def longestStrChain(self,words):
        words = sorted(words, key=len)
        
        max_chain_length = 1

        for i in range(len(words)):
            chain_length = self.findLongestChain(words, i, 1)
            max_chain_length = max(max_chain_length, chain_length)

        return max_chain_length

    def findLongestChain(self, words, current_word_index, current_chain_length):
        current_word = words[current_word_index]
        max_chain_length = current_chain_length

        for i in range(current_word_index + 1, len(words)):
            next_word = words[i]
            if self.isPredecessor(current_word, next_word):
                chain_length = self.findLongestChain(words, i, current_chain_length + 1)
                max_chain_length = max(max_chain_length, chain_length)

        return max_chain_length

    def isPredecessor(self, word1, word2):
        if len(word1) + 1 != len(word2):
            return False

        i = j = 0
        found_difference = False

        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                if found_difference:
                    return False
                found_difference = True
                j += 1
            else:
                i += 1
                j += 1

        return True
