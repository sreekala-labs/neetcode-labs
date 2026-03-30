class Solution:
    def isValid(self, s: str) -> bool:
        resultStack=[]
        dict={
            '}':'{',
            ']':'[',
            ')':'('
        }

        for c in s:
            if c in dict:
                if resultStack and resultStack[-1]==dict[c]:
                    resultStack.pop()
                else:
                    return False
            else:
                resultStack.append(c)

        return True if not resultStack else False