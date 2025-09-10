from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Take the first string as reference
        prefix = strs[0]
        
        # Compare prefix with each word
        for word in strs[1:]:
            # Shrink prefix until it's a prefix of word
            while word.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# ----------------------------
# ✅ Test Cases
# ----------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example cases
    print(sol.longestCommonPrefix(["flower","flow","flight"]))  # "fl"
    print(sol.longestCommonPrefix(["dog","racecar","car"]))    # ""
    
    # Edge cases
    print(sol.longestCommonPrefix(["a"]))                      # "a"
    print(sol.longestCommonPrefix(["",""]))                    # ""
    print(sol.longestCommonPrefix(["interstellar","internet","internal"])) # "inte"
    print(sol.longestCommonPrefix(["throne","throne"]))        # "throne"
    print(sol.longestCommonPrefix(["abc","abcd","ab"]))        # "ab"
    print(sol.longestCommonPrefix([""]))                       # ""
