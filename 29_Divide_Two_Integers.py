class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge cases for overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow scenario
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        # Subtract divisor from dividend until it becomes smaller than divisor
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            dividend -= temp_divisor
            quotient += multiple
        
        # Apply the sign
        if negative:
            quotient = -quotient
        
        # Ensure the result is within the 32-bit integer range
        return max(INT_MIN, min(INT_MAX, quotient))

# Test examples
solution = Solution()

# Test cases
test_cases = [
    (10, 3),    # Expected output: 3
    (7, -3),    # Expected output: -2
    (1, 1),     # Expected output: 1
    (-10, 2),   # Expected output: -5
    (-7, -3),   # Expected output: 2
    (0, 1),     # Expected output: 0
    (-2**31, 1), # Expected output: -2**31
    (-2**31, -1) # Expected output: 2**31 - 1 (overflow case)
]

# Print test results
for dividend, divisor in test_cases:
    result = solution.divide(dividend, divisor)
    print(f"divide({dividend}, {divisor}) = {result}")
