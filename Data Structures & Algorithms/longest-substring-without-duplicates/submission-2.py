class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_len = 0
        i = 0

        for j in range(len(s)):
            if s[j] in dic and dic[s[j]] >= i:
                i = dic[s[j]] + 1   # shrink window past the duplicate
            dic[s[j]] = j
            max_len = max(max_len, j - i + 1)

        return max_len

        
        