class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
      
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums





















  # ans=nums+nums
        # return ans
        
        #or
        #return nums*2


        #alternate method
        # ans=[]
        # for i in range(2):#O(2)
        #     for j in nums:#O(n), n is number of elements in nums
        #         ans.append(j)
        # return ans