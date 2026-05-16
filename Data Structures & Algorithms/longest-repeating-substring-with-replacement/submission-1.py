from collections import deque, Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        window = deque()
        c = Counter()
        maxf = 0
        res = 0
        for R, ch in enumerate(s):
            window.append(ch)
            c[ch] += 1
            maxf = max(maxf, c[ch])
            
            while len(window) - maxf > k:
                left_char = window.popleft()  # Get the character being removed
                c[left_char] -= 1             # Decrement count of that character
                # Note: we don't update maxf here (optimization explained above)
            res = max(res, len(window))
        return res