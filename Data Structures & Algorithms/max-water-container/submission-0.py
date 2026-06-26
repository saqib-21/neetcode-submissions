class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        area=0 
        l, r = 0, len(heights)-1 

        while l<r:
            width = r-l
            h = min(heights[l], heights[r])
            area =  width * h

            if area > max_area:
                max_area= area
            
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l+= 1
            else:
                l+= 1
                r -= 1
        return max_area

