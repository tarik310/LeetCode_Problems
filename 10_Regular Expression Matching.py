class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Handle patterns like a*, a*b*, etc.
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[m][n]



# Example usage:
solution = Solution()
print(solution.isMatch("aab", "c*a*b"))  # Output: True
print(solution.isMatch("mississippi", "mis*is*p*."))  # Output: False
print(solution.isMatch("ab", ".*"))  # Output: True
print(solution.isMatch("aaa", "a.a"))  # Output: True
print(solution.isMatch("aaa", "ab*a*c*a"))  # Output: True
print(solution.isMatch("a", "ab*"))  # Output: True
print(solution.isMatch("a", ".*..a*"))  # Output: False
print(solution.isMatch("", "c*"))  # Output: True
print(solution.isMatch("bbbba", ".*a*a"))  # Output: True
print(solution.isMatch("a", ".*..a*"))  # Output: False


