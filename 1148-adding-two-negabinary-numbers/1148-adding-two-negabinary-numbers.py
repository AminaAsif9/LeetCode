class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Helper function to convert a negabinary number to decimal
        def to_decimal(arr):
            decimal_value = 0
            length = len(arr)  # Get the length of the array
            
            for i in range(length):
                bit = arr[i]  # Get the bit at position i
                decimal_value += bit * (-2) ** (length - 1 - i)  # Compute the weighted sum
            return decimal_value
        
        # Helper function to convert decimal to negabinary
        def to_negabinary(n):
            if n == 0:
                return [0]
            negabinary = []
            while n != 0:
                rem = n % -2
                n = n // -2
                if rem < 0:
                    rem += 2
                    n += 1
                negabinary.append(rem)
            return negabinary[::-1]
        
        # Convert both arr1 and arr2 to decimal
        num1 = to_decimal(arr1)
        num2 = to_decimal(arr2)
        
        # Add the two numbers in decimal
        total = num1 + num2
        
        # Convert the result back to negabinary (base -2)
        return to_negabinary(total)