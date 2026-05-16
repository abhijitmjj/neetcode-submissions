from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = defaultdict(int)
        for elem in nums:
            c[elem] += 1
        heap = [(-freq, val) for (val, freq) in c.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

        
        