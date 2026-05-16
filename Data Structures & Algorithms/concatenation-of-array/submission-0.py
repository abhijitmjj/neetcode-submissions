class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        arr = [0]*2*N
        for idx, elem in enumerate(nums):
            arr[idx] = elem
            arr[N+idx] = elem
        return arr
        