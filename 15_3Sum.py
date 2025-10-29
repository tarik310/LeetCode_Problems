from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicate i

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res


# Example usage:
solution = Solution()
# print(solution.threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]
# print(solution.threeSum([0,1,1]))  # Output: []
# print(solution.threeSum([0,0,0]))  # Output: [[0,0,0]]
# print(solution.threeSum([-2,0,1,1,2]))  # Output: [[-2,0,2],[-2,1,1]]
print(solution.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))  # Output: [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
# print(solution.threeSum([]))  # Output: []
# print(solution.threeSum([1,2,-2,-1]))  # Output: []
# print(solution.threeSum([-1,0,1,0]))  # Output: [[-1,0,1]]
# print(solution.threeSum([-5,2,3,0,1,-4,-2,4]))  # Output: [[-5,2,3],[-4,0,4],[-2,-1,3],[-2,1,1]]
# print(solution.threeSum([-3,0,1,2,-1,1,-2]))  # Output: [[-3,1,2],[-2,0,2],[-2,1,1],[-1,0,1]]
# print(solution.threeSum([3,0,-4,-1,-2,1,2]))  # Output: [[-4,1,3],[-2,-1,3],[-2,0,2],[-1,0,1]]
# print(solution.threeSum([-2,-1,0,1,2,3]))  # Output: [[-2,-1,3],[-2,0,2],[-1,0,1]]