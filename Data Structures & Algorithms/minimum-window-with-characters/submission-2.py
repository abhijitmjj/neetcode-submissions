from collections import Counter, deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        l = 0
        best = (float('inf'), 0 , 0)
        window = deque()
        for r, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            window.append(c)

            while missing == 0:
                if (r - l + 1) < best[0]:
                    best = (r - l + 1, l, r)
                left_c = window.popleft()
                need[left_c] += 1
                if need[left_c] > 0:
                    missing += 1
                l += 1
        return s[best[1]: best[2] + 1] if best[0] != float('inf') else ""