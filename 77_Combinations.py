from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            # Base case: if the current combination has k numbers
            if len(path) == k:
                res.append(path[:])  # copy the list
                return

            # Choose next numbers
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)  # go deeper
                path.pop()  # backtrack

        backtrack(1, [])
        return res

print(Solution().combine(4, 2))  # Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(Solution().combine(1, 1))  # Output: [[1]]
print(Solution().combine(5, 3))  # Output: [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
print(Solution().combine(3, 2))  # Output: [[1,2],[1,3],[2,3]]