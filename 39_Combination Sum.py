from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sorting helps with pruning

        def dfs(start, target, path):
            if target == 0:
                res.append(path[:])  # Found a valid combination
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > target:  # pruning
                    break
                path.append(num)
                dfs(i, target - num, path)  # i (not i+1) because we can reuse same element
                path.pop()  # backtrack

        dfs(0, target, [])
        return res
print(Solution().combinationSum([2,3,6,7], 7))  # Output: [[7], [2,2,3]]
print(Solution().combinationSum([2,3,5], 8))  # Output: [[2,2,2,2], [2,3,3], [3,5]]
print(Solution().combinationSum([2], 1))  # Output: []
print(Solution().combinationSum([1], 1))  # Output: [[1]]
print(Solution().combinationSum([1], 2))  # Output: [[1,1]]
print(Solution().combinationSum([3,2,4], 6))  # Output: [[2,2,2], [2,4], [3,3]]
print(Solution().combinationSum([8,7,4,3], 11))  # Output: [[3,4,4], [4,7], [3,8]]
print(Solution().combinationSum([1,2,3], 4))  # Output: [[1,1,1,1], [1,1,2], [1,3], [2,2]]
print(Solution().combinationSum([2,4,6,3], 9))  # Output: [[3,6], [3,3,3], [2,2,2,3]]
print(Solution().combinationSum([10,1,2,7,6,1,5], 8))  # Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
print(Solution().combinationSum([2,3,5], 8))  # Output: [[2,2,2,2], [2,3,3], [3,5]]
print(Solution().combinationSum([1,2], 4))  # Output: [[1,1,1,1], [1,1,2], [2,2]]
print(Solution().combinationSum([4,2,8], 8))  # Output: [[4,4], [2,2,2,2], [2,2,4], [8]]
print(Solution().combinationSum([1], 3))  # Output: [[1,1,1]]