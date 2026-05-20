class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 1. Square each number using a list comprehension
        nums = [x**2 for x in nums]
        
        # 2. Sort the squared numbers in-place
        nums.sort()
        
        # 3. Explicitly return the modified list
        return nums