class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = [0]*26
        t_arr = [0]*26
        for c in s:
            s_arr[ord(c)-ord('a')] += 1
        for c in t:
            t_arr[ord(c)-ord('a')] += 1
        return tuple(s_arr) == tuple(t_arr)
        