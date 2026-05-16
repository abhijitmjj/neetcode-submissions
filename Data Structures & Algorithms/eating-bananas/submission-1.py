class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1; r = max(piles)
        

        res = r
        while l <= r:
            k = l + (r - l) // 2
            totalTime = sum(math.ceil(float(x)/k) for x in piles)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


        