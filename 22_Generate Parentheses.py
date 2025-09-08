from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        buf = [''] * (2 * n)

        def backtrack(pos: int, open_count: int, close_count: int) -> None:
            if pos == 2 * n:
                res.append(''.join(buf))
                return

            if open_count < n:
                buf[pos] = '('
                backtrack(pos + 1, open_count + 1, close_count)

            if close_count < open_count:
                buf[pos] = ')'
                backtrack(pos + 1, open_count, close_count + 1)

        backtrack(0, 0, 0)
        return res



# ------------------ Test Cases ------------------
if __name__ == "__main__":
    s = Solution()

    # Example 1
    print("n=3:", s.generateParenthesis(3))
    # Expected (order may vary):
    # ["((()))","(()())","(())()","()(())","()()()"]

    # Example 2
    print("n=1:", s.generateParenthesis(1))
    # Expected: ["()"]

    # Extra test
    print("n=2:", s.generateParenthesis(2))
    # Expected: ["(())", "()()"]

    # Edge case
    print("n=0:", s.generateParenthesis(0))
    # Expected: [""]
    print("n=4:", s.generateParenthesis(4))
    # Expected: [""]