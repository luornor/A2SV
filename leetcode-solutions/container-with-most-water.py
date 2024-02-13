class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
       
        max_area = -1
        while l<r:
            h= min(height[l],height[r])
            w = r-l
            max_area = max(max_area, w*h)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
            

        return max_area


        