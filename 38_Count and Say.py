class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Get previous term
        prev = self.countAndSay(n - 1)
        result = []
        
        # Run-length encoding
        i = 0
        while i < len(prev):
            count = 1
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
                i += 1
            result.append(str(count))
            result.append(prev[i])
            i += 1
        
        return "".join(result)


# ---------- Test Cases ----------
if __name__ == "__main__":
    sol = Solution()
    
    # Example cases
    print(sol.countAndSay(1))  # Output: "1"
    print(sol.countAndSay(4))  # Output: "1211"
    
    # Additional tests
    print(sol.countAndSay(2))  # Output: "11"
    print(sol.countAndSay(3))  # Output: "21"
    print(sol.countAndSay(5))  # Output: "111221"
    print(sol.countAndSay(20))  # Output: "312211"
