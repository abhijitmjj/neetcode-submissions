class Solution:
    from collections import deque
    def jump(self, nums: List[int]) -> int:
        queue: deque[tuple[int, int]] = deque([(0,0)])
        visited: set[int] = set([0])

        n = len(nums)
        if not nums or n == 0:
            return -1
        
        if n <= 1:
            return 0
        
        while queue:
            current, jump = queue.popleft()

            for i in range(1, nums[current]+1):
                next_idx = current + i

                if next_idx == n - 1:
                    return jump + 1
                
                if next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append((next_idx, jump + 1))
        return -1
                    
        