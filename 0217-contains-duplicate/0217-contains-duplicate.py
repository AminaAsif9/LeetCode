class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) != len(nums) else False

# 2nd approach
# arr = []
#         for i in nums:
#             if i not in arr:
#                 arr.append(i)
#             else:
#                 return True
#         return False