class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)

        max_sub = float("-inf")
        array_hist = [1]*length


        for i in range(length):
            if(i == 0):
                array_hist[i] = 1
                max_sub = max(max_sub, array_hist[i])

            else:
                target = nums[i]

                # if(nums[i]>nums[i-1]):
                #     array_hist[i] = array_hist[i-1] + 1

                

                # else:
                for j in range(i-1,-1,-1):
                    if(target>nums[j]):
                        array_hist[i] = max(array_hist[j] + 1, array_hist[i])
                        max_sub = max(max_sub, array_hist[i])
                        
        print(array_hist)
        return max_sub
        