class Solution:
    # def reverseString(self, s: List[str]) -> None:
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
    #     # s.reverse()
    #     # other method

    #     l = 0
    #     r = len(s) -1
    #     while l < r:
    #         s[l] , s[r] = s[r] , s[l] # Swapping
    #         l += 1
    #         r -= 1

    # Time: O(n)
    # Space: O(1)

    # With Recursion
    def helper(self, s, left, right) -> None:
        if left > right: # Base case to stop recursion
            return
        s[left], s[right] = s[right], s[left] # swap
        return self.helper(s, left+1, right-1)


    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        return self.helper(s, left, right)