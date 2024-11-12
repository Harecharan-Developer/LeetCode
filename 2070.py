# class Solution:
#     def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
#         def binary_search(arr, target):
#             lo, high = 0, len(arr) - 1
#             while lo <= high:
#                 mid = (lo + high) // 2
#                 if arr[mid][0] <= target:
#                     lo = mid + 1
#                 else:
#                     high = mid - 1
#             return high 

#         items.sort(key=lambda x : x[0])
#         answer=[]
#         for j in queries:
#             max_beauty=float('-inf')
#             index=binary_search(items,j)
#             for i in items[:index+1]:
#                 if i[0]<=j:
#                     max_beauty=max(i[1],max_beauty)
#                 else:
#                     break
#             if max_beauty!=float('-inf'):
#                 answer.append(max_beauty)
#             else:
#                 answer.append(0)
#         return answer
from typing import List
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price in ascending order
        items.sort()
        
        # Precompute the maximum beauty up to each price point
        prices = []
        max_beauty = []
        current_max = 0
        
        for price, beauty in items:
            current_max = max(current_max, beauty)
            prices.append(price)
            max_beauty.append(current_max)
        
        # Process each query
        answer = []
        for query in queries:
            # Find the rightmost price less than or equal to the query using binary search
            idx = bisect_right(prices, query) - 1
            if idx >= 0:
                answer.append(max_beauty[idx])
            else:
                answer.append(0)
        
        return answer
if __name__ == "__main__":
    solution = Solution()
    items = [[1, 2], [3, 2], [2, 4], [5, 6]]
    queries = [1, 2, 3, 4, 5, 6]
    print(solution.maximumBeauty(items, queries))