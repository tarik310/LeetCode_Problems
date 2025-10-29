from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')  # infinity initially
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                # If exactly equal to target, we found the best possible
                if current_sum == target:
                    return current_sum
                # Update closest sum if current is closer to target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                # Move pointers
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum


# Example usage:
solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4], 1))  # Output: 2
print(solution.threeSumClosest([0,0,0], 1))      # Output: 0
print(solution.threeSumClosest([1,1,1,0], -100)) # Output: 2
print(solution.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))  # Output: -2
print(solution.threeSumClosest([1,2,5,10,11], 12))  # Output: 13
print(solution.threeSumClosest([-3,-2,-5,3,-4], -1))  # Output: -2
print(solution.threeSumClosest([0,2,1,-3], 1))  # Output: 0