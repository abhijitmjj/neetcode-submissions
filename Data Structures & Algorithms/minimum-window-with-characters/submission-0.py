from collections import deque, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        deficit = len(t)
        lookup = Counter(t)
        best_len = (float('inf'), -1, -1)
        window = deque()

        for r, ch in enumerate(s):
            window.append((r, ch))
            if lookup[ch] > 0:
                deficit -= 1
            # char entering
            lookup[ch] -= 1

            while deficit == 0:
                if len(window) < best_len[0]:
                    best_len = len(window), window[0][0], window[-1][0]
                left_idx, left_char = window.popleft()
                    
                if lookup[left_char] >= 0:
                    deficit += 1
                lookup[left_char] += 1
                    # char exiting
                    
        return s[best_len[1]:best_len[2]+1] if best_len[0] != float('inf') else ""


        