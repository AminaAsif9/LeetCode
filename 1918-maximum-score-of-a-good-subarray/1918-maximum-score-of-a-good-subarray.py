class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        '''- Multiply min val with len each time
        - like, first we start from 7 (index 3 as given k=3 so we start from there)
        
        - In ex 1, we have to start at index 3 and more to its both sides left n right,
        - 7 x 1 = 7 (7 is val and 1 is length)
        then we have 7 and 4 as we move to one forward, and we r checking min val, so
        that is 4 and length is now 2 so,
        - 4 x 2 = 8
        right, now again move one next and we have, 7, 4, 5, but min is still 4 and len is 3 now
        - 4 x 3 = 12 (which is score btw, we are finding score)
        then array is end, so we move to other direction to 7, that is to left side
        here we have 3 and total we have 7, 4, 5, 3 and min is 3 with len 4,
        - 3 x 4 = 12
        and so on like,
        - 3 x 5 = 15
        - 1 x 6 = 6 
        and that's it, so here max score is 15 that we needed '''

 # Initialize two pointers at index k
        l = r = k
        
        # Start with the score being just the value at index k
        res = nums[k]
        # Current minimum value in the window
        cur_min = nums[k]

        # Expand the window as long as we're not at both edges of the array
        while l > 0 or r < len(nums) - 1:
            # Get the next left and right values if possible, otherwise 0
            left = nums[l - 1] if l > 0 else 0
            right = nums[r + 1] if r < len(nums) - 1 else 0

            # Expand towards the side with the larger value to keep cur_min higher
            if left > right:
                l -= 1                     # Move left pointer
                cur_min = min(cur_min, left)  # Update current min
            else:
                r += 1                     # Move right pointer
                cur_min = min(cur_min, right) # Update current min

            # Calculate score for current window and update result
            res = max(res, cur_min * (r - l + 1))

        # Return the maximum score found
        return res
