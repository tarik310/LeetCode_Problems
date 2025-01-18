class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # If there's only one row or the string is too short, no reformatting is needed
        if numRows == 1 or len(s) <= numRows:
            return s

        # Prepare a list of strings, one for each row
        rows = [""] * numRows
        # Current row pointer
        current_row = 0
        # Direction: +1 for downward, -1 for upward
        step = 1

        # Build the zigzag
        for char in s:
            rows[current_row] += char

            # If we reach the bottom row, reverse upward; if top, reverse downward
            if current_row == 0:
                step = 1
            elif current_row == numRows - 1:
                step = -1

            # Move to the next row based on the direction
            current_row += step

        # Join all rows to form the result
        return "".join(rows)

# ---------------
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))  # Expected: "PAHNAPLSIIGYIR"
    print(sol.convert("PAYPALISHIRING", 4))  # Expected: "PINALSIGYAHRPI"
    print(sol.convert("A", 1))               # Expected: "A"
