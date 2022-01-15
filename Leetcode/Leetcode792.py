from collections import deque
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        setS=set(s)
        table={i:deque() for i in setS}
        for w in words:
            if w[0] in table.keys():
                table[w[0]].append(w)

        answer=0
        for nows in s:
            for i in range(len(table[nows])):
                tmp=table[nows].popleft()
                if len(tmp)==1:
                    answer+=1
                elif tmp[1] in table.keys():
                    table[tmp[1]].append(tmp[1:])
        return answer
