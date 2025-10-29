from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # shorten prefix
                if not prefix:
                    return ""
        return prefix


# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
# print(solution.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
# print(solution.longestCommonPrefix(["interspecies","interstellar","interstate"]))  # Output: "inters"
# print(solution.longestCommonPrefix(["throne","throne"]))  # Output: "throne"
# print(solution.longestCommonPrefix(["cir","car"]))  # Output: "c"
# print(solution.longestCommonPrefix(["a"]))  # Output: "a"
# print(solution.longestCommonPrefix([""]))  # Output: ""
# print(solution.longestCommonPrefix([]))  # Output: ""
# print(solution.longestCommonPrefix(["prefix","preform","prevent"]))  # Output: "pre"
# print(solution.longestCommonPrefix(["apple","app","apricot"]))  # Output: "ap"
# print(solution.longestCommonPrefix(["abcd","abce","abcf"]))  # Output: "abc"
# print(solution.longestCommonPrefix(["zxy","zxyz","zx"]))  # Output: "zx"
# print(solution.longestCommonPrefix(["hello","helium","helicopter"]))  # Output: "hel"