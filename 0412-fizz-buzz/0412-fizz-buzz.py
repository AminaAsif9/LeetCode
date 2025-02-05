class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []  # Create a list to store the result
        
        for i in range(1, n + 1):  # Loop from 1 to n inclusive
            if i % 3 == 0 and i % 5 == 0:  # Divisible by both 3 and 5
                answer.append("FizzBuzz")
            elif i % 3 == 0:  
                answer.append("Fizz")
            elif i % 5 == 0:  
                answer.append("Buzz")
            else:  # Not divisible by 3 or 5
                answer.append(str(i))
        
        return answer  # Return the resulting list
