class Solution:
    def finalString(self, s: str) -> str:
        # Two Pointers
        result = [] # creating a list
        for char in s:
            if char == 'i': # if character is i
            # using two pointers approach on result[] list that we created
                left = 0
                right = len(result)-1
                while left < right:
                    result[left], result[right] = result[right], result[left]
                    left += 1
                    right -= 1
            else:
                result.append(char) # if character is not i then add it in list result
        return "".join(result)
        # join() convert from list to string