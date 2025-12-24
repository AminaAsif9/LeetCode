class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        def solve(i , total_sum, arr):
            if total_sum > target:
                return 
            if total_sum == target:
                if arr not in result:
                    result.append(arr[:])
                return 
            if i >= n:
                return 
            arr.append(candidates[i])
            #  take the current element
            solve(i, total_sum + candidates[i], arr)
            arr.pop()
            # skip the current elemnt
            solve(i + 1, total_sum, arr)
        solve(0, 0, [])
        return result

        # other method

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []

#         def make_combination(idx, comb, total):
#             if total == target:
#                 res.append(comb[:])
#                 return
            
#             if total > target or idx >= len(candidates):
#                 return
            
#             comb.append(candidates[idx])
#             make_combination(idx, comb, total + candidates[idx])
#             comb.pop()
#             make_combination(idx+1, comb, total)

#             return res

#         return make_combination(0, [], 0)