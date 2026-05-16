class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prefix = 1
        for idx, elem in enumerate(nums):
            res[idx] = prefix
            prefix *= elem
        suffix = 1
        for idx in range(len(nums) - 1, -1, -1):
            res[idx] *= suffix
            suffix *= nums[idx]
        return res

            
        