class Solution:
    def trap(self, height: List[int]) -> int:
        # when to calculate area-
        # smaller numbers present between two large numbers

        # how to calculate area-
        # net of two maximum height + ((net of two maximum height - smaller numbers)*num of smallnums)
      
        if not height:
            return 0

        total_water = 0
        left = 0
        right = len(height) - 1
        left_max = right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water
