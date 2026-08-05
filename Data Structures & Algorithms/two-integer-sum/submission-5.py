class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        dic_index = {}
        for i in range(len(nums)):
            dic[nums[i]] = target - nums[i]
            dic_index[nums[i]] = i
        
        for j in range(len(nums)):
            if dic[nums[j]] in nums:
                index1, index2 = j, dic_index[dic[nums[j]]]
                if(index1 == index2):
                    continue
                else:
                    break

        small = min(index1, index2)
        large = max(index1, index2)

        return [small, large]
        