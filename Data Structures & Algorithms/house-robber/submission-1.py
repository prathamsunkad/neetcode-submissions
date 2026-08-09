class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==1):
            return nums[0]
        if(n==2):
            return max(nums[0],nums[1])

        max_array_till = [nums[0], nums[1]] + [-1]*(n-2)
        max_money = nums[0]
        for i in range(2,n):
            max_array_till[i] = max_money + nums[i]
            max_money = max(max_array_till[i-1], max_money)

        return max(max_money, max_array_till[n-1])



        