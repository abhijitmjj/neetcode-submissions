class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = max_currrent = nums[0]
        n = len(nums)
        for i in range(1, n):
            max_currrent = max(nums[i], max_currrent+nums[i])
            result = max(result, max_currrent)
        return result



        