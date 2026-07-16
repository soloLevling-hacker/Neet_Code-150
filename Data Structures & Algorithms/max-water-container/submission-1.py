class Solution:
    def maxArea(self, heights: List[int]) -> int:
        height = heights
        left = 0
        right = len(height) - 1
        max_area = 0
    
        while left < right:
            # Fetch heights once to avoid double indexing
            h_left = height[left]
            h_right = height[right]
        
            # Calculate area using if/else instead of min() and max() function calls
            if h_left < h_right:
                area = h_left * (right - left)
                left += 1
            else:
                area = h_right * (right - left)
                right -= 1
        
            # Manual comparison instead of max() function call
            if area > max_area:
                max_area = area
    
        return max_area

                
