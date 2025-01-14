class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            # Partition both arrays
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Handle edge cases for partitions
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if partitions are valid
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If the total number of elements is odd
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # If the total number of elements is even
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                # Move left in nums1
                high = partition1 - 1
            else:
                # Move right in nums1
                low = partition1 + 1
        
        raise ValueError("Input arrays are not sorted or invalid")

# Test cases
solution = Solution()

# Example 1
nums1 = [1, 3]
nums2 = [2]
print(f"Example 1: {solution.findMedianSortedArrays(nums1, nums2)}")  
# Expected Output: 2.0

# Example 2
nums1 = [1, 2]
nums2 = [3, 4]
print(f"Example 2: {solution.findMedianSortedArrays(nums1, nums2)}")  
# Expected Output: 2.5

# Additional Test Cases
nums1 = [0, 0]
nums2 = [0, 0]
print(f"Example 3: {solution.findMedianSortedArrays(nums1, nums2)}")  
# Expected Output: 0.0

nums1 = []
nums2 = [1]
print(f"Example 4: {solution.findMedianSortedArrays(nums1, nums2)}")  
# Expected Output: 1.0

nums1 = [2]
nums2 = []
print(f"Example 5: {solution.findMedianSortedArrays(nums1, nums2)}")  
# Expected Output: 2.0
