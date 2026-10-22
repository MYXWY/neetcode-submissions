class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        total = 0
        l = 0
        r = len(heights)-1

        while(l<r):
            temp = min(heights[l],heights[r]) * (r-l)
            total = max(total,temp)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return total
