class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # Two pointers starting at both ends of the array
        l, r = 0, len(height) - 1
        # Track the tallest wall seen so far from the left and from the right
        leftMax, rightMax = height[l], height[r]

        res = 0  # Total trapped water
        while l < r:
            # The side with the SMALLER max wall is the one that limits
            # how much water can be trapped at the current position,
            # so we always process (move) that side.
            if leftMax < rightMax:
                l += 1
                # Update the tallest wall seen so far from the left
                leftMax = max(leftMax, height[l])
                # Water trapped here = height of the tallest left wall
                # minus the height of the current bar
                # (safe because rightMax is guaranteed >= leftMax,
                # so leftMax is the true limiting wall)
                res += leftMax - height[l]
            else:
                r -= 1
                # Update the tallest wall seen so far from the right
                rightMax = max(rightMax, height[r])
                # Water trapped here = height of the tallest right wall
                # minus the height of the current bar
                res += rightMax - height[r]

        return res