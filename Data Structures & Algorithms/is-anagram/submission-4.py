class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS={}
        countT={}


        for c in s:
            countS[c]=1+countS.get(c,0)
        
        for f in t:
            countT[f]=1+countT.get(f,0)

        return countS==countT