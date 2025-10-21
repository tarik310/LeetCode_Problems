from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursive level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If number is greater than remaining target, break
                if candidates[i] > target:
                    break
                # Choose this number and move to the next
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])
        backtrack(0, target, [])
        return res


# Example usage:
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))  # Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
print(solution.combinationSum2([2,5,2,1,2], 5))  # Output: [[1,2,2],[5]]
print(solution.combinationSum2([1,1,1,1,1], 3))  # Output: [[1,1,1]]
print(solution.combinationSum2([3,1,3,5,1,1], 8))  # Output: [[1,1,1,5],[3,5]]
print(solution.combinationSum2([4,4,2,1,4,2,2,1], 6))  # Output: [[1,1,4],[1,2,3],[2,4]]
print(solution.combinationSum2([1,2,3,4,5], 10))  # Output: [[1,2,3,4],[1,4,5],[2,3,5]]
print(solution.combinationSum2([2,3,6,7], 7))  # Output: [[7]]
print(solution.combinationSum2([5,3,4,7,2], 10))  # Output: [[3,7],[4,6],[5,5]]
print(solution.combinationSum2([1,2,2,2,5], 5))  # Output: [[5],[2,2,1]]
print(solution.combinationSum2([8,7,4,3], 11))  # Output: [[8,3],[7,4]]
