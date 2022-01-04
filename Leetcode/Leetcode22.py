#20220104

from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
        else:
            answer=[]
            dq=deque([["(",1,1]]) #mstr, check, leftBrace
            
            while len(dq)!=0:
                mstr,check,leftBrace=dq.popleft()
                                
                if check==0 and leftBrace==n:
                      answer.append(mstr)
                      continue
                if leftBrace>n:
                      continue
                
                if leftBrace<n:
                      dq.append([mstr+"(",check+1,leftBrace+1])
                if check>0:
                      dq.append([mstr+")",check-1,leftBrace])
            return answer