class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Step 1: Initialize product and sum
        product = 1
        total_sum = 0
        
        # Step 2: Process each digit of the number
        while n > 0:
            digit = n % 10  # Get the last digit
            product *= digit  # Update the product
            total_sum += digit  # Update the sum
            n //= 10  # Remove the last digit from the number
        
        # Step 3: Subtract sum from product
        return product - total_sum
