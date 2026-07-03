class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for elem in nums:
            if count == 0:
                candidate = elem
            count += (1 if elem == candidate else -1)
        return candidate

        