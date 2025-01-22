class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: empty needle
        if not needle:
            return 0
        
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        # Loop through haystack up to the point where needle can fit
        for i in range(haystack_length - needle_length + 1):
            # Check if the substring matches needle
            match = True
            for j in range(needle_length):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i  # Found the first occurrence
        
        return -1  # Needle not found in haystack

# Test examples
solution = Solution()

# Test cases
test_cases = [
    ("sadbutsad", "sad", 0),       # Expected output: 0
    ("leetcode", "leeto", -1),     # Expected output: -1
    ("hello", "ll", 2),            # Expected output: 2
    ("aaaaa", "bba", -1),          # Expected output: -1
    ("", "", 0),                   # Expected output: 0 (edge case: empty strings)
    ("abc", "", 0),                # Expected output: 0 (needle is empty)
    ("a", "a", 0),                 # Expected output: 0 (single character match)
    ("mississippi", "issip", 4)    # Expected output: 4
]

# Run and print test results
for haystack, needle, expected in test_cases:
    result = solution.strStr(haystack, needle)
    print(f"strStr({haystack!r}, {needle!r}) = {result} (Expected: {expected})")
