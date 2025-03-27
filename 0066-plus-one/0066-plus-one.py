class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits # If all digits were 9, the loop will finish without returning, meaning all digits are now 0.

# In this case, the function prepends 1 to the list and returns it.