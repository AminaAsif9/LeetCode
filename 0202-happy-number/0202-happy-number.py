class Solution:
    def isHappy(self, n: int) -> bool:
        current_number = n
        number = 0 # store the sum of the squares of the digits
        numbers = {} # dictionary used to track numbers we’ve seen before.
        
        while True:
            #This loop will keep running until we either reach 1 (happy number) 
            #or detect a cycle (not a happy number).

            for i in str(current_number): #Convert current_number to a string so we can iterate over its digits.
                number += int(i) ** 2
            if number == 1:
                return True
            if number in numbers: #If number was seen before in numbers, we have a cycle, meaning n is not a happy number.
                return False
            numbers[number] = 0 # Store number in the dictionary to track it.
            current_number = number 
            number = 0
#O(logn)