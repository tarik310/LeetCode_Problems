from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            # if we reach the end of the current jump, we must jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break
        return jumps



# Example usage:
solution = Solution()
print(solution.jump([2,3,1,1,4]))  # Output: 2
print(solution.jump([2,1,1,1,4]))  # Output: 3
print(solution.jump([0]))  # Output: 0
print(solution.jump([1,2]))  # Output: 1
print(solution.jump([1,1,1,1]))  # Output: 3
print(solution.jump([3,2,1,0,4]))  # Output: 2
print(solution.jump([5,9,3,2,1,0,2,3,3,1,0,0]))  # Output: 3
print(solution.jump([1,4,3,7,1,2,6,7,6,10]))  # Output: 4
print(solution.jump([2,4,1,1,1,1,1,1]))  # Output: 3
print(solution.jump([10,9,8,7,6,5,4,3,2,1,0]))  # Output: 1
print(solution.jump([1,3,5,8,9,2,6,7,6,8,9]))  # Output: 3
print(solution.jump([2,3,0,1,4]))  # Output: 2
print(solution.jump([1,2,0,1]))  # Output: 2