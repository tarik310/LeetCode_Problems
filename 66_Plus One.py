from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # iterate from the last digit backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # no carry, just return
            digits[i] = 0  # set to 0 and continue loop (carry)
        
        # if loop finishes, all digits were 9
        return [1] + digits


print(Solution().plusOne([1,2,3]))  # Output: [1,2,4]
print(Solution().plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(Solution().plusOne([0]))  # Output: [1]
print(Solution().plusOne([9]))  # Output: [1,0]
print(Solution().plusOne([9,9,9]))  # Output: [1,0,0,0]
print(Solution().plusOne([1,9,9]))  # Output: [2,0,0]
print(Solution().plusOne([2,9,9]))  # Output: [3,0,0]
print(Solution().plusOne([1,2,9]))  # Output: [1,3,0]
print(Solution().plusOne([1,2,8]))  # Output: [1,2,9]