class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity: int) -> bool:
            day, currCap = 1, capacity
            for w in weights:
                if currCap - w < 0:
                    day += 1
                    if day > days:
                        return False
                    currCap = capacity # reset for the next day
                currCap -= w
            return True
        
        # do bin search on range -> min is max(weights) and max is sum(weights)
        l = max(weights)
        r = sum(weights)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
                

        