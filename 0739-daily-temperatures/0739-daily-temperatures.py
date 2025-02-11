class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = temperatures
        s = [] # creating empty stack
        r = [0] * len(T) # creating array of size of temperature containing 0 at every
        # index and will be updated accordingly

        for i in range (len(T)):
            while s and T[i] > T[s[-1]]: # 74( top of stack) > 73 
                index = s.pop() 
                r[index] = i - index
            s.append(i)
        
        return r