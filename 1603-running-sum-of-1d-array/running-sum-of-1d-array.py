class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i - 1]        
        # return nums
        a = 0
        array = []
        for i in nums:
            a = a + i
            array.append(a)

        return array


#T: O(n)
#S: O(n)