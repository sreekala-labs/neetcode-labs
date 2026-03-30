import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_only=re.sub(r'[^A-Za-z0-9]','',s).lower()
        i=0
        j=len(alphanumeric_only)-1
        while i<=j:
            if alphanumeric_only[i]!=alphanumeric_only[j]:
                return False
            i=i+1
            j=j-1
        return True