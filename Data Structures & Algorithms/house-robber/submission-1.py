from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        # This is like arranging 0's and 1's -> you should not
        # have two ones adjacent
        @cache
        def dp(i: int) -> int:
            # think about last house
            # if i rob this, i cannot rob (n - 1)
            # how? use max( , )
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(dp(i - 2) + nums[i], dp(i - 1))
        return dp(len(nums) - 1)

        