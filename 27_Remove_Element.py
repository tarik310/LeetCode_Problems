class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Pointer to place the next valid element
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != val:
                # Place the current element at the kth position
                nums[k] = nums[i]
                k += 1
        
        # Return the count of elements not equal to val
        return k

# Test examples
solution = Solution()

# Test cases
test_cases = [
    ([3, 2, 2, 3], 3, 2),          # Expected k = 2, nums = [2, 2, _, _]
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5), # Expected k = 5, nums = [0, 1, 4, 0, 3, _, _, _]
    ([1, 1, 1, 1], 1, 0),          # Expected k = 0, nums = [_, _, _, _]
    ([1, 2, 3, 4, 5], 6, 5),       # Expected k = 5, nums = [1, 2, 3, 4, 5]
    ([], 1, 0),                    # Expected k = 0, nums = []
]

# Run and print test results
for nums, val, expected_k in test_cases:
    result = solution.removeElement(nums, val)
    print(f"removeElement({nums}, {val}) = {result}, nums = {nums[:result]}")
