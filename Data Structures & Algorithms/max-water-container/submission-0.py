class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        left = 0
        right = length - 1
        area = 0
        while right>left:
            product = (right - left)*min(heights[left],heights[right])
            area  = max(area, product)
            if(heights[left]<heights[right]):
                left+=1
                continue

            if(heights[right]<=heights[left]):
                right-=1
                continue

        return area
        