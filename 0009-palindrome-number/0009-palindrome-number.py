class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  
            return False  # Negative numbers and numbers ending in 0 (except 0) can't be palindromes
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10  # Reduce the original number

        return x == reversed_half or x == reversed_half // 10  # Handles even and odd-length numbers
