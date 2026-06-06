class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #lets count the number of letters in s
        #and the letters in t
        #if a.values contains any non zero value, return false
        #else gravy
        
        if len(s)!=len(t):
            return False

        a={}

        for i in range(len(s)):
            if s[i] in a:
                a[s[i]] +=1
            else:
                a[s[i]]=1
            
            if t[i] in a:
                a[t[i]]-=1
            else:
                a[t[i]]=-1
        
        if any(a.values()):
            return False
        
        return True

