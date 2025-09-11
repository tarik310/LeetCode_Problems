class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # remove trailing spaces
        s = s.rstrip()
        
        # split by spaces and take the last word
        last_word = s.split(" ")[-1]
        
        return len(last_word)
