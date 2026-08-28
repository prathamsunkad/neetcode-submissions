class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        possum = sum(nums)
        if (possum%2):
            return False

        dp = [0] * (possum + 2)
        dp[0] = 1

        for j in range(len(nums)):
            for i in range((possum), -1, -1):
                dp[i] = max(dp[i - nums[j]], dp[i]) 

        print(dp)
        return bool(dp[possum//2])