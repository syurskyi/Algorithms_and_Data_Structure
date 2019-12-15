class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)-1
        count = 0
        while l > -1:
            if s[l] == ' ':
                l -= 1
                
            if s[l].isalpha():
                count += 1
                l -= 1
                if s[l] == ' ':
                    break
        return count