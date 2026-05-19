class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for number in nums:
            if number == 0:
                zero_count +=1
                continue
            product = product*number
        
        output = []
        for number in nums:
            if number == 0 and zero_count == 1:
                output.append(product)
            elif zero_count >= 1:
                output.append(0)

            else:
                output.append(int(product/number))

        return output
        