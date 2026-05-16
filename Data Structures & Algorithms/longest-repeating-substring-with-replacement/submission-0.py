from collections import deque, Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L=0
        window = deque()
        c = Counter()
        maxf = 0
        res = 0
        for R, ch in enumerate(s):
            window.append(ch)
            c[ch] += 1
            maxf = max(maxf, c[ch])
            while len(window) - maxf > k:
                elem = window.popleft()
                c[elem] -= 1
                
            res = max(res, len(window))
        return res




        