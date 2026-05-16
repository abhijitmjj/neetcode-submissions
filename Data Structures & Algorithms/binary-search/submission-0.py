class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr) - 1
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                ans = mid
                return ans
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return ans
            

        