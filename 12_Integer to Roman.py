class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                result.append(numerals[i])
        return "".join(result)

print(Solution().intToRoman(3))    # Output: "III"
print(Solution().intToRoman(4))    # Output: "IV"
print(Solution().intToRoman(9))    # Output: "IX"
print(Solution().intToRoman(58))   # Output: "LVIII"
print(Solution().intToRoman(1994)) # Output: "MCMXCIV
print(Solution().intToRoman(1))    # Output: "I"
print(Solution().intToRoman(3999)) # Output: "MMMCMXCIX
print(Solution().intToRoman(44))   # Output: "XLIV"
print(Solution().intToRoman(1453)) # Output: "MCDLIII
print(Solution().intToRoman(2021)) # Output: "MMXXI"
print(Solution().intToRoman(1987)) # Output: "MCMLXXXVII"
print(Solution().intToRoman(276))  # Output: "CCLXXVI
print(Solution().intToRoman(621))  # Output: "DCXXI"
print(Solution().intToRoman(888))  # Output: "DCCCLXXXVIII"
print(Solution().intToRoman(2421)) # Output: "MMCDXXI"
print(Solution().intToRoman(160))  # Output: "CLX"
print(Solution().intToRoman(73))   # Output: "LXXIII"