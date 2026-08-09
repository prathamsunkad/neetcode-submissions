class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if(len(cost)==2):
            return min(cost[0],cost[1])
        n = len(cost)
        total_cost = [0,0] + [-1]*(n-1)
        for i in range(2,n+1):
            total_cost[i] = min(total_cost[i-1]+cost[i-1], total_cost[i-2] + cost[i-2])

        return total_cost[n]