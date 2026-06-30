class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for idx in range(len(nums)):
            if (target - nums[idx]) in seen:
                return [seen[(target - nums[idx])], idx]
            seen[nums[idx]] = idx
        return []
        