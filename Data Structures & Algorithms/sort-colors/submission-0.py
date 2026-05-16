from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        c = Counter(nums)
        j = 0
        for num in sorted(c):
            k = 0
            while j < len(nums) and k < c[num]:
                nums[j] = num
                k += 1
                j += 1
        return nums  

        