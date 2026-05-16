class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]*len(arr)
        rightMax = -1
        for idx in range(len(arr) - 1, -1, -1):
            res[idx] = rightMax
            rightMax = max(arr[idx], rightMax)
        return res