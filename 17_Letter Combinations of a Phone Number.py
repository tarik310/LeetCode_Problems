from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        def backtrack(index: int, current: str):
            # Base case: if the combination is complete
            if index == len(digits):
                result.append(current)
                return
            
            # Get letters for current digit
            for letter in digit_to_letters[digits[index]]:
                backtrack(index + 1, current + letter)
        
        backtrack(0, "")
        return result



# Example usage:
solution = Solution()
print(solution.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(solution.letterCombinations(""))     # Output: []
print(solution.letterCombinations("2"))    # Output: ["a","b","c"]
print(solution.letterCombinations("9"))    # Output: ["w","x","y","z"]
print(solution.letterCombinations("79"))   # Output: ["pw","px","py","pz","qw","qx","qy","qz","rw","rx","ry","rz","sw","sx","sy","sz"]