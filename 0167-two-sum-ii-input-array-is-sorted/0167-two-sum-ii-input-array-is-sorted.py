class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers, concept like binary search is used
        L, R = 0, len(numbers) - 1 # L = 0 and R = length of numbers - 1
        
        while L < R:
            cur_sum = numbers[L] + numbers[R]
            if cur_sum == target:
                return [L + 1, R + 1] # returning index
            elif cur_sum < target:
                L += 1
            else:
                R -= 1
        
        return [-1, -1] # fallback statement, returns something if ans is not found, otherwise error