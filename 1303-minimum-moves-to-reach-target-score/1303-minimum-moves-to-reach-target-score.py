class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1 and maxDoubles > 0:
            # If target is odd, we cannot halve it, so we increment by 1
            if target % 2 == 1:
                target -= 1
            else:
                # We can still use a double operation
                target //= 2
                maxDoubles -= 1
            moves += 1
        
        # If maxDoubles is exhausted, we just need to increment the rest
        moves += target - 1  # Because we need to reach 1

        return moves
