from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return [[""]]
        
        result = []
        result.append([strs[0]])
        
        for i in strs[1:]:
            found = False
            for j in range(len(result)):
                if set(result[j][0]) == set(i):  # Check if the sets of characters are the same
                    result[j].append(i)
                    found = True
                    break
            
            if not found:
                result.append([i])
        
        return result


class Solution2:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for word in strs:
            count = [0] * 26  # Initialize a count array for each word
            for char in word:
                count[ord(char) - ord('a')] += 1  # Increment count for each character
            
            # Convert the count array into a tuple to use as a key in the hashmap
            key = tuple(count)
            anagrams[key].append(word)
        
        return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
solution2 = Solution2()

output = solution.groupAnagrams(strs)
print(output)
output = solution2.groupAnagrams(strs)
print(output)