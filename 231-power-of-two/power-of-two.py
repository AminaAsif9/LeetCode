class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # solving with recursion
        if n <= 0: # base case, if 2 power is 0 or negative number then we have to stop, because that is not power of 2
            return False

        if n == 1: 
            return True

        if n%2 != 0: # if odd numbers
            return False

        return self.isPowerOfTwo(n//2) # recursive call