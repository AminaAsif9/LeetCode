class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
        return result