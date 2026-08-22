class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def traverse(index):
            if index == len(s):
                return True
            if index in memo:
                return memo[index]

            for i in range(index + 1, len(s) + 1):
                if s[index:i] in wordSet and traverse(i):
                    memo[index] = True
                    return True

            memo[index] = False
            return False

        return traverse(0)