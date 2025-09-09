from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            # Move the smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example cases
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Expected 49
    print(sol.maxArea([1,1]))                # Expected 1

    # Edge cases
    print(sol.maxArea([4,3,2,1,4]))          # Expected 16
    print(sol.maxArea([1,2,1]))              # Expected 2
    print(sol.maxArea([1,2,4,3]))            # Expected 4

    # Large input (increasing sequence)
    print(sol.maxArea(list(range(1, 1001)))) # Should handle efficiently