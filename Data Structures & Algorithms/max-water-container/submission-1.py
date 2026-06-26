class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n=len(heights)
        l = 0 
        r= n-1

        best_area = 0
        while l<r:
            w = (r-l)
            h = (min(heights[l],heights[r]))
            new_area=w*h
            if new_area<best_area:
                if heights[l]>heights[r]:
                    r-=1
                else:
                    l+=1
            elif new_area >= best_area:
                best_area = new_area
                if heights[l]>heights[r]:
                    r-=1
                else:
                    l+=1
        return best_area

            