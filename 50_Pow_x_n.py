class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        # handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        while n > 0:
            if n % 2 == 1:   # if odd exponent
                result *= x
            x *= x
            n //= 2
        return result


print(Solution().myPow(2.00000, 10))  # Output: 1024.00000
print(Solution().myPow(2.10000, 3))   # Output: 9.26100
print(Solution().myPow(2.00000, -2))  # Output: 0.25000
print(Solution().myPow(2.00000, 0))   # Output: 1.00000
print(Solution().myPow(1.00000, -2147483648))  # Output: 1.00000
print(Solution().myPow(0.44528, 0))  # Output: 1.00000
print(Solution().myPow(0.00001, 2147483647))  # Output: 0.00000
print(Solution().myPow(34.00515, -3))  # Output: 0.00003
print(Solution().myPow(2.00000, -2147483648))  # Output: 0.00000
print(Solution().myPow(8.88023, 3))  # Output: 700.28163
print(Solution().myPow(0.00001, 2147483647))  # Output: 0.00000