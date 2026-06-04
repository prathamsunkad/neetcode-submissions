class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 1:
            return 0

        i = 0
        j = 1

        while(j<len(prices)):
            if(prices[i] <= prices[j]):
                diff = prices[j] - prices[i]
                profit = max(profit,diff)
                j+=1
                continue

            if(prices[i]>prices[j]):
                i = j
                j+=1

        return profit
        