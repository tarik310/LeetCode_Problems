class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            # Append current bit
            result.append(str(total % 2))
            carry = total // 2

        # Reverse because we built it backwards
        return ''.join(reversed(result))
if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("11", "1"))       # Expected "100"
    print(sol.addBinary("1010", "1011"))  # Expected "10101"
    print(sol.addBinary("0", "0"))        # Expected "0"
    print(sol.addBinary("1111", "1111"))  # Expected "11110"
    print(sol.addBinary("101", "100000")) # Expected "100101"
