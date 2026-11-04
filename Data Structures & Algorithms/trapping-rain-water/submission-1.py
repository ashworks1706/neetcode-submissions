class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize two pointers at the start and end of the list.
        left, right = 0, len(height) - 1  
        # These variables will keep track of the highest bar seen so far
        # from the left and the right, respectively.
        left_max, right_max = 0, 0  
        water = 0  # This accumulates the total water trapped.

        # Process the elevation by moving the two pointers
        while left < right:
            # Compare the heights at both pointers.
            # The side with the lower height limits the water that can be trapped.
            if height[left] < height[right]:
                # Update left_max or add trapped water for the left side.
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1  # Move the left pointer inward.
            else:
                # Update right_max or add trapped water for the right side.
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1  # Move the right pointer inward.

        return water
