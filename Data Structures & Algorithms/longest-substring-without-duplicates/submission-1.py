from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = deque()
        seen = set()
        max_l = 0
        for c in s:
            
            while c in seen:
                
                seen.remove(q.popleft())
            q.append(c)
            seen.add(c)
            max_l = max(len(q), max_l)
        return max_l
            



        