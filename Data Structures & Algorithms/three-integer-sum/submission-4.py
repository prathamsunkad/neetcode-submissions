class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        length = len(nums)
        if length == 3:
            if(sum(sorted_nums) == 0):
                return [sorted_nums]


        dic_check = {}
        for i in range(length):
            target = -sorted_nums[i]
            new_array = sorted_nums[0:i] + sorted_nums[i+1:length]
            left = 0
            right = length - 2
            while right>left:
                if(new_array[right] + new_array[left] == target):
                    dic_check[tuple(sorted([-target, new_array[right], new_array[left]]))] = 1
                    right-=1
                    left+=1
                    continue

                if(new_array[right] + new_array[left] > target):
                    right-=1
                    continue

                if(new_array[right] + new_array[left] < target):
                    left+=1
                    continue
            
        empty_list = []
        for keys,values in dic_check.items():
            empty_list.append(list(keys))

        return empty_list

            
        