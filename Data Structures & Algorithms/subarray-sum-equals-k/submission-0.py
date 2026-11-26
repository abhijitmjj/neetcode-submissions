class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter
        seen = Counter({0:1})
        prefix = 0
        count = 0 
        for elem in nums:
            prefix += elem
            count += seen[prefix - k]
            seen[prefix] += 1
        return count
        