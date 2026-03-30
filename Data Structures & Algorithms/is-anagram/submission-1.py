import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Check for length.
        if len(s)!=len(t):
            return False

        map={}
        for c in s:
            if c in map:
                map[c]+=1
            else:
                map[c]=1

        for c in t:
            if c in map:
                map[c]-=1

        return True if all(value==0 for value in map.values()) else False