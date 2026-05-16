class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        def dp(left: int, right: int) -> int:
            prev1 = 0
            prev2 = 0
            for i in range(left, right + 1):
                curr = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = curr
            return prev1
        return max(dp(0, n - 2), dp(1, n - 1))
        