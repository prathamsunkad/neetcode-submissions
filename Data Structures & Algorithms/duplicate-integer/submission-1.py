class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        dic = {}
        for i in nums:
            dic[i] = dic.setdefault(i, 0) + 1
            if dic[i]>1:
                return True
            
        return False
        