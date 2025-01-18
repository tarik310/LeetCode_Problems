class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer bounds
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Track the sign; work with the absolute value
        sign = 1 if x >= 0 else -1
        x_abs = abs(x)
        
        # Reverse by string manipulation
        reversed_str = str(x_abs)[::-1]
        reversed_int = sign * int(reversed_str)
        
        # If out of 32-bit range, return 0
        if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0
        return reversed_int

# -------------------------------------------------------------------------
# Example usage (outside the LeetCode environment):
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))    # Expected 321
    print(sol.reverse(-123))   # Expected -321
    print(sol.reverse(120))    # Expected 21
    print(sol.reverse(0))      # Expected 0
    print(sol.reverse(1534236469))  # Likely 0 due to overflow
