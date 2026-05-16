class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for idx, elem in enumerate(nums):
            if (target - elem) in seen:
                return [seen[target - elem], idx, ]
            seen[elem] = idx
        return [-1,-1]
            


        