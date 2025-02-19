# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n  

        while low < high:
            mid = low + (high - low) // 2  
            if isBadVersion(mid):
                high = mid  # The first bad version could be mid or before.
            else:
                low = mid + 1 # The first bad version must be after mid.
        return low # At the end, low will be the first bad version.