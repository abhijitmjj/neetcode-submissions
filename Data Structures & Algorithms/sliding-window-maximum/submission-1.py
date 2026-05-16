from collections import Counter, deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return [max(nums)]
        if k <= 0 or not nums:
            return []
        if k == 1:
            return nums[:]
        out = []
        
        dq = deque()
        for r, num in enumerate(nums):

            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(r)

            l = r - (k - 1)
            # drop indices out of window
            if dq[0] < l:
                dq.popleft()
            if l >= 0:
                out.append(nums[dq[0]])
        return out


        