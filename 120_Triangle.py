from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        return dp[0]


# Example usage:
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle1))  # Output: 11
# triangle2 = [[-10]]
# print(Solution().minimumTotal(triangle2))  # Output: -10
# triangle3 = [[1],[2,3]]
# print(Solution().minimumTotal(triangle3))  # Output: 3
# triangle4 = [[1],[2,3],[1,-1,-3]]
# print(Solution().minimumTotal(triangle4))  # Output: 1
# triangle5 = [[-1],[2,3],[1,-1,-3]]
# print(Solution().minimumTotal(triangle5))  # Output: -1


