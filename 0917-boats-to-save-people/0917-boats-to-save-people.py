class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ''' We have people 1,2 (it is their weight) and limit 3, means 
        we need only 1 boat here, since 1+2 = 3 and 3 is limit.
        Similarly in 2 example, limit is 3 means boat weight should not 
        increase 3. So we have boat1 containing 2, boat2 having 2 and 1 (means 2+1=3)
        so limit is reached. and boat3 having 2.
        '''
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats