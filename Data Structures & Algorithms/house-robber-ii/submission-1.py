from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        def rob_range(left: int, right: int) -> int:
            @cache
            def dp(i: int) -> int:
                if i < left:
                    return 0
                return max(dp(i - 1), dp(i - 2) + nums[i])
            return dp(right)
        return max(rob_range(0, n - 2), rob_range(1, n - 1))
        
        