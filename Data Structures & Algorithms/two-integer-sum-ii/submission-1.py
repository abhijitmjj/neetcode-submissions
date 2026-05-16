class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            curr_sum = numbers[L] + numbers[R]

            if curr_sum == target:
                return [L+1, R+1]
            if curr_sum > target:
                R -= 1
            else:
                L += 1
        
            
        