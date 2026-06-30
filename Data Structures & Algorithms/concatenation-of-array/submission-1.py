class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cpy = [0]*len(nums)*2
        for idx, elem in enumerate(nums):
            cpy[idx] = elem; cpy[len(nums) + idx] = elem
        return cpy
