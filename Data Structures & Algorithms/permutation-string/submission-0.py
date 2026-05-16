from collections import Counter, deque
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        res = []
        lookup = Counter(s1)
        deficit = len(s1)
        window = deque()
        win_count = Counter()
        for _, c in enumerate(s2):

            window.append(c)
            if lookup[c] > 0:
                deficit -= 1
            lookup[c] -= 1 

            if len(window) > len(s1):
                left_char = window.popleft()
                if lookup[left_char] >= 0:
                    deficit += 1
                # exit
                lookup[left_char] += 1
            if len(window) == len(s1) and deficit == 0:
                return True
        return False

            
        