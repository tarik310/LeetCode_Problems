class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last index of each character
        char_map = {}
        # Pointer to the start of the current window
        start = 0
        # Variable to store the maximum length of substring found
        max_length = 0
        
        for end in range(len(s)):
            # If the character is in the dictionary and is within the current window
            if s[end] in char_map and char_map[s[end]] >= start:
                # Move the start pointer just after the last occurrence of the current character
                start = char_map[s[end]] + 1
            # Update the dictionary with the current character's index
            char_map[s[end]] = end
            # Calculate the length of the current substring and update max_length
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Example Test Cases
solution = Solution()

# Test Case 1
s1 = "abcabcbb"
print(f"Test Case 1: {s1} -> Longest Substring Length: {solution.lengthOfLongestSubstring(s1)}")  
# Expected Output: 3 (The answer is "abc")

# Test Case 2
s2 = "bbbbb"
print(f"Test Case 2: {s2} -> Longest Substring Length: {solution.lengthOfLongestSubstring(s2)}")  
# Expected Output: 1 (The answer is "b")

# Test Case 3
s3 = "pwwkew"
print(f"Test Case 3: {s3} -> Longest Substring Length: {solution.lengthOfLongestSubstring(s3)}")  
# Expected Output: 3 (The answer is "wke")

# Test Case 4
s4 = "a"
print(f"Test Case 4: {s4} -> Longest Substring Length: {solution.lengthOfLongestSubstring(s4)}")  
# Expected Output: 1 (The answer is "a")

# Test Case 5
s5 = "dvdf"
print(f"Test Case 5: {s5} -> Longest Substring Length: {solution.lengthOfLongestSubstring(s5)}")  
# Expected Output: 3 (The answer is "vdf")
