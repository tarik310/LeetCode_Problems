class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            # If current value is smaller than the next one, subtract it
            if i + 1 < n and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total


# ----------------------------
# ✅ Test Cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example cases
    print(sol.romanToInt("III"))      # 3
    print(sol.romanToInt("LVIII"))    # 58
    print(sol.romanToInt("MCMXCIV"))  # 1994

    # Additional tests
    print(sol.romanToInt("I"))        # 1
    print(sol.romanToInt("IV"))       # 4
    print(sol.romanToInt("IX"))       # 9
    print(sol.romanToInt("XL"))       # 40
    print(sol.romanToInt("XC"))       # 90
    print(sol.romanToInt("CD"))       # 400
    print(sol.romanToInt("CM"))       # 900
    print(sol.romanToInt("MMXXV"))    # 2025
    print(sol.romanToInt("MMMCMXCIX")) # 3999 (max valid value)
