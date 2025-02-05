class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        left = right = ''
        
        for i in range(len(s) - 1):
            left = s[: i + 1]
            right = s[i + 1:]
            left_count = left.count('0')
            right_count = right.count('1')
            max_score = max(max_score, (left_count + right_count))
        
        return max_score