class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        longest = 0

        for elem in nums:

            if (elem - 1) not in seen:
                l = 0
                while (elem + l) in seen:
                    l += 1
                longest = max(longest, l)

        return longest
        