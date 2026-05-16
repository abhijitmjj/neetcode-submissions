# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l = r = 1
#         n = len(nums)
#         while r < n:
#             if nums[r] != nums[r - 1]:
#                 nums[l] = nums[r]
#                 l += 1
#             r += 1
#         return l
        
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        l = r = 0
        while r < n:
            nums[l] = nums[r]
            while r < n and nums[r] == nums[l]:
                r += 1
            l += 1
        return l