class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # skip non-alphanumeric left
            while left < right and not s[left].isalnum():
                left += 1
            # skip non-alphanumeric right
            while left < right and not s[right].isalnum():
                right -= 1
            # compare lowercased chars
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# Example usage:
s1 = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s1))  # Output: True
s2 = "race a car"
print(Solution().isPalindrome(s2))  # Output: False
s3 = " "
print(Solution().isPalindrome(s3))  # Output: True
s4 = "0P"
print(Solution().isPalindrome(s4))  # Output: False
s5 = "ab_a"
print(Solution().isPalindrome(s5))  # Output: True