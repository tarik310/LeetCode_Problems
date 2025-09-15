class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if n & 1:   # check the least significant bit
                count += 1
            n >>= 1     # shift right to process the next bit
        return count
print(Solution().hammingWeight(11))  # Output: 3
print(Solution().hammingWeight(128))  # Output: 1
print(Solution().hammingWeight(4294967293))  # Output: 31
print(Solution().hammingWeight(0))  # Output: 0
print(Solution().hammingWeight(1))  # Output: 1
print(Solution().hammingWeight(15))  # Output: 4
print(Solution().hammingWeight(255))  # Output: 8
print(Solution().hammingWeight(1023))  # Output: 10
print(Solution().hammingWeight(2147483647))  # Output: 31
print(Solution().hammingWeight(4294967295))  # Output: 32
print(Solution().hammingWeight(5))  # Output: 2
print(Solution().hammingWeight(6))  # Output: 2
