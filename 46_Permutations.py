class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        
        def backtrack(start):
            # If we've placed all elements, add a copy of the current permutation
            if start == len(nums):
                results.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap current element with the one at index i
                nums[start], nums[i] = nums[i], nums[start]
                # Recursively permute the remaining elements
                backtrack(start + 1)
                # Swap back to restore the original state (backtrack)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return results
if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,2,3,4,5,8,23,7]))
    # Expected:
    # [
    #   [1,2,3], [1,3,2],
    #   [2,1,3], [2,3,1],
    #   [3,1,2], [3,2,1]
    # ]
