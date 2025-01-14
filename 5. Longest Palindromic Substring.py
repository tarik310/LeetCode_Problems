class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd-length palindromes
            odd = expand_center(i, i)
            # Even-length palindromes
            even = expand_center(i, i + 1)
            # Update longest palindrome
            longest = max(longest, odd, even, key=len)
        
        return longest

# Test cases
solution = Solution()

# Example 1
print(f"Example 1: {solution.longestPalindrome('babad')}")  # Expected Output: "bab" or "aba"

# Example 2
print(f"Example 2: {solution.longestPalindrome('cbbd')}")  # Expected Output: "bb"

# Additional Test Cases
print(f"Example 3: {solution.longestPalindrome('a')}")  # Expected Output: "a"
print(f"Example 4: {solution.longestPalindrome('ac')}")  # Expected Output: "a" or "c"
print(f"Example 5: {solution.longestPalindrome('racecar')}")  # Expected Output: "racecar"
print(f"Example 6: {solution.longestPalindrome('forgeeksskeegfor')}")  # Expected Output: "geeksskeeg"
