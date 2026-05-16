class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        l, r = 0, n - 1
        left_max, right_max = height[l], height[r]
        water = 0
        while l < r:

            if left_max <= right_max:
                l += 1
                left_max = max(left_max, height[l])
                water += max(min(left_max, right_max) - height[l], 0)
            else:
                r -= 1
                right_max = max(right_max, height[r])
                water += max(min(left_max, right_max) - height[r], 0)
        return water