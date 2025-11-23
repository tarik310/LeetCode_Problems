from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                # Row, column, and box identifiers
                row_key = ("row", r, val)
                col_key = ("col", c, val)
                box_key = ("box", r // 3, c // 3, val)

                # If any already exists, invalid
                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                # Otherwise add them
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True



# Example usage:
solution = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board))  # Output: True