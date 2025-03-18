class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a list to store the minimum number of coins for each amount
        # amount + 1 represent an "impossible" or "infinity" value
        min_coins = [amount + 1] * (amount + 1)
        # Base case: 0 coins are needed to make up amount 0
        min_coins[0] = 0

        # Iterate through all amounts from 1 to the target amount
        for i in range(1, amount + 1):
            # Try each coin to see if it can contribute to the current amount
            for c in coins:
                # Check if the coin is not larger than the current amount
                if i - c >= 0:
                    # Update the minimum number of coins for the current amount
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])
         
        # Return the result for the target amount
        if min_coins[-1] == amount + 1:
            return -1  # No valid solution
        else:
            return min_coins[-1]  # Return the minimum number of coins