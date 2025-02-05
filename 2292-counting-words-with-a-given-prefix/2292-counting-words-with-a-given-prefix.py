class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans=0
        for i in words: #O(n)
            if pref== i[0:len(pref)]:# slicing has complexity of O(n) but n is already assigned so we consider O(m) where m is length of pref
                ans+=1
        return ans



        #opened a code a little for better understanding
        # ans=0
        # for i in words:#O(n) ,n=length of words
        # sli=i[0:len(pref)] #O(m), m=length of pref
        # if pref== sli: #O(m), m=length of pref already defined
        #         ans+=1
        # return ans
#total = (O(n*(m+m)))=O(2mn)=O(mn)