class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ans1 = "".join(word1)                
        ans2 = "".join(word2)
        if ans1 == ans2:
            return True
        return False
#O(N)