class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path, choices):
            if not choices:
                result.append(path[:])       #Store a Copy of path
                return

            for i in range(len(choices)):
                path.append(choices[i])
                backtrack(path, choices[:i] + choices[i+1:])
                path.pop()
            
        backtrack([], nums)
        return result  