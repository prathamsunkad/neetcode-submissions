class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]
        if(n==2):
            return max(nums)
        if(n==3):
            return max(nums)

        
        max_array_listfromstart = [nums[0], nums[1]] + [-1]*(n-2)
        max_array_listfromsecond = [nums[0], nums[1], nums[2]] + [-1]*(n-3)
        max_element_start = nums[0]
        max_element_second = nums[1]

        for i in range(2,n):
            if(i!=n-1):
                max_array_listfromstart[i] = nums[i] + max_element_start
                max_element_start = max(max_element_start, max_array_listfromstart[i-1])

            if i != 2:     
                max_array_listfromsecond[i] = nums[i] + max_element_second
                max_element_second = max(max_element_second, max_array_listfromsecond[i-1])

        
        max1 = max(max_element_second, max_array_listfromsecond[n-1])
        max2 = max(max_element_start, max_array_listfromstart[n-2])

        return max(max1,max2)

        