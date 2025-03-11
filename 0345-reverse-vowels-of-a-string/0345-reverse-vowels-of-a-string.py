class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set("aeiouAEIOU")
        l =0
        r =len(s)-1
        arr = list(s)
        while l<r:
            if arr[l] not in vowel:
                l+=1
            elif arr[r] not in vowel:
                r-=1
            else:
                arr[l],arr[r] = arr[r],arr[l]

                l+=1
                r-=1
        res ="".join(arr)
        return res