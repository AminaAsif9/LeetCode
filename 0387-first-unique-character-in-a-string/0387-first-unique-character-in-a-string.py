class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
         #{'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1} 
        for char in s:
            if char in char_count:
                char_count[char] += 1 #l = 1 at first
            else:
                char_count[char] = 1
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i  
        return -1
