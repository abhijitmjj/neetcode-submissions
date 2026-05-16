class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        if (ans := self.binSearch(0, pivot - 1, target, nums)) != -1:
            return ans
        elif (ans := self.binSearch(pivot, len(nums) - 1, target, nums)) != -1:
            return ans
        return ans

    def binSearch(self, l, r, target, nums) -> int:
        left = l
        right = r
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return -1  
        