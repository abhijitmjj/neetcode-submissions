from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap: int) -> bool:
            used_days = 1
            load = 0
            for w in weights:
                if load + w > cap:
                    used_days += 1
                    load = 0
                    if used_days > days:
                        return False
                load += w
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid      # mid works, try smaller
            else:
                left = mid + 1   # mid fails, need bigger
        return left
