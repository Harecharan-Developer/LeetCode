from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]
        h = sorted(heights)
        return [d[height] for height in h[::-1]]

class Solution1:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height_pairs = [(i, name, height) for i, (name, height) in enumerate(zip(names, heights))]
        
        name_height_pairs.sort(key=lambda x: x[2], reverse=True)
        
        sorted_names = [name for _, name, _ in name_height_pairs]
        
        return sorted_names

wrapper = Solution()
wrapper1 = Solution1()

names = ["Alex", "Kevin", "James"]
heights = [5, 4, 6]
print(wrapper.sortPeople(names, heights)) # ["James", "Alex", "Kevin"]
print(wrapper1.sortPeople(names, heights)) # ["James", "Alex", "Kevin"]
