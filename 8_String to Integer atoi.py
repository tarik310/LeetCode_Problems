class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        i, n = 0, len(s)
        # 1. Skip leading spaces
        while i < n and s[i] == " ":
            i += 1
        if i == n:
            return 0
        
        # 2. Sign
        sign = 1
        if s[i] in ["+", "-"]:
            sign = -1 if s[i] == "-" else 1
            i += 1
        
        # 3. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")
            
            # 4. Check for overflow BEFORE adding
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num


print(Solution().myAtoi("   -42"))  # Output: -42
print(Solution().myAtoi("4193 with words"))  # Output:
print(Solution().myAtoi("words and 987"))  # Output: 0
print(Solution().myAtoi("-91283472332"))  # Output: -2147483648
print(Solution().myAtoi("3.14159"))  # Output: 3
print(Solution().myAtoi("+1"))  # Output: 1
print(Solution().myAtoi("+-2"))  # Output: 0
