class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1
        
        k_list=[[] for _ in range(len(nums))]

        for key,value in map.items():
            k_list[value-1].append(key)
        
        k_copy = k
        final_list = []
        j = len(nums)-1
        while k_copy > 0:
            while(len(k_list[j]) > 0 and k_copy > 0):
                final_list.append(k_list[j].pop())
                k_copy-=1
            j-=1

        return final_list

        