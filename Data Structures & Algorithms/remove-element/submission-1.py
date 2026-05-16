from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of 'val' from the given list in-place and returns the new length.
        
        This solution uses the two-pointer technique:
        - 'L' (Left Pointer): Tracks the position where the next valid element should be placed.
        - 'R' (Right Pointer): Iterates through the list, checking for non-'val' elements.

        The algorithm ensures that each non-'val' element gets moved to the left without unnecessary swaps,
        maintaining an optimal O(n) time complexity and O(1) space complexity.
        """
        L = 0  # Position where the next valid element should be placed

        for R in range(len(nums)):  # Iterate over the list with the Right Pointer
            if nums[R] != val:  # When we find a non-'val' element
                nums[L] = nums[R]  # Move the valid element to its correct position
                L += 1  # Advance the Left Pointer

        return L  # The new length of the modified array
