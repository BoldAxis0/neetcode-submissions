class Solution:
    def isPalindrome(self, s: str) -> bool:

        # first format the string to only have alphanumeric 
        #characters

        st = ""
        for i in s:
            if i.isalnum():
                st+=i.lower()
        
        #now we can seamlessly check forwards and backwards
        p1=0
        p2=len(st) - 1 
        while p1<p2:
            if st[p1]==st[p2]:
                p1+=1
                p2-=1
                continue
            else:
                return False

        return True









        


        