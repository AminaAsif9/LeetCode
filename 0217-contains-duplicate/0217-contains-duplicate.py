class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) != len(nums):
            return True
        else:
            return False

        # Shortcut of this
        # return True if len(set(nums)) != len(nums) else False

# 2nd approach
        # arr = []
        # for i in nums:
        #     if i not in arr:
        #         arr.append(i)
        #     else:
        #         return True
        # return False