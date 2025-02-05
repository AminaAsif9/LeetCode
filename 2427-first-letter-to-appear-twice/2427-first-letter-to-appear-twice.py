class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        empty_set = set() #set stores value only once, no duplicates, abc
        for i in s:
            if i in empty_set: #at first set is empty so false
                return i #returns first letter that is already in set before so ans is "c" 

            empty_set.add(i) #it adds "a" there


     