from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i: int) -> int:
            if (i == 0) or (i == 1):
                return 1
            return dp(i-1) + dp(i - 2)
        return dp(n)    