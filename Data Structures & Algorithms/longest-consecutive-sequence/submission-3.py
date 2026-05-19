class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        set_nums = sorted(set(nums))
        map = {}
        for i in nums:
            map[i] = 1
        
        max_num = 1
        map_2 = map.copy()
        for i in set_nums:
            if i-1 in map.keys():
                map_2[i] = map_2[i-1] + 1
                if (map_2[i] > max_num):
                    max_num = map_2[i]
        return max_num 
            

        
        