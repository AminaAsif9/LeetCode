class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from typing import List
        # Store result
        triplets = []
        
        # Sort the list
        nums.sort()
        
        for i in range(len(nums) - 2):
            
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize two pointers
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    # Add to result
                    triplets.append([nums[i], nums[j], nums[k]])
                    
                    # Skip duplicate elements
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    # Move both pointers
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:  # total > 0
                    k -= 1
        
        return triplets
