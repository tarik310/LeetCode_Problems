class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in pairs:  # If it's a closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack


# Example usage:
solution = Solution()
print(solution.isValid("()"))          # Output: True
print(solution.isValid("()[]{}"))      # Output: True
print(solution.isValid("(]"))          # Output: False
print(solution.isValid("([)]"))        # Output: False
print(solution.isValid("{[]}"))        # Output: True
print(solution.isValid("((()))"))      # Output: True
print(solution.isValid("((())"))       # Output: False
print(solution.isValid(")("))          # Output: False
print(solution.isValid("]"))           # Output: False
print(solution.isValid("["))           # Output: False
print(solution.isValid(""))             # Output: True
print(solution.isValid("(([]){})"))    # Output: True