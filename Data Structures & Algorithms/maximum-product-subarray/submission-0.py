class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        ans = max(nums)
        maxProd, minProd = 1,1

        for number in nums:
            if number == 0:
                maxProd, minProd = 1,1
                continue
            tmp = maxProd*number
            maxProd = max(maxProd*number, number, minProd*number)
            minProd = min(tmp, number, minProd*number)
            ans = max(ans, maxProd, minProd)


        
        return ans
        