from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = [], {}
        for i in range(len(matches)):
            winners.append(matches[i][0])
            if matches[i][1] not in losers:
                losers[matches[i][1]] = 1
            else:
                losers[matches[i][1]] += 1

        result = [[], []]

        for i in range(len(winners)):
            if winners[i] not in losers:
                result[0].append(winners[i])

        for i in losers:
            if losers[i] == 1:
                result[1].append(i)
                
        result[0].sort()
        result[1].sort()
        return result

# Driver code
if __name__ == "__main__":
    solution = Solution()
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    winners = solution.findWinners(matches)
    print("Winners:", winners[0])
    print("Losers with 1 loss:", winners[1])
