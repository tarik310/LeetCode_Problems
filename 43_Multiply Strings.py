class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # multiply from rightmost digits
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1, pos2 = i + j, i + j + 1
                total = mul + res[pos2]

                res[pos2] = total % 10
                res[pos1] += total // 10

        # skip leading zeros
        result = []
        for num in res:
            if not (len(result) == 0 and num == 0):
                result.append(str(num))

        return "".join(result) if result else "0"


print(Solution().multiply("2", "3"))  # Output: "6"
print(Solution().multiply("123", "456"))  # Output: "56088"
print(Solution().multiply("0", "456"))  # Output: "0"
print(Solution().multiply("9", "9"))  # Output: "81"
print(Solution().multiply("99", "99"))  # Output: "9801"
print(Solution().multiply("123456789", "987654321"))  # Output:
print(Solution().multiply("123456789", "987654321"))  # Output: "121932631112635269"
print(Solution().multiply("1", "1"))  # Output: "1"
print(Solution().multiply("25", "4"))  # Output: "100"
print(Solution().multiply("999", "999"))  # Output: "998001"
print(Solution().multiply("1000", "1000"))  # Output: "1000000"
print(Solution().multiply("12345678901234567890", "98765432109876543210"))  # Output: "1219326311370217952237463801111263526900"