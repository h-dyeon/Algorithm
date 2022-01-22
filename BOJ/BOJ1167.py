import sys
from collections import deque

N=int(input())
mat={i:deque() for i in range(N)}
for i in range(N):
    tmp=list(map(int,sys.stdin.readline().strip().split(' ')))
    for j in range(1,len(tmp)-1,2):
        mat[tmp[0]-1].append([tmp[j]-1,tmp[j+1]])


print(N)
print(mat)

# N=5
# mat={0: deque([[2, 2]]), 1: deque([[3, 4]]), 2: deque([[0, 2], [3, 3]]), 3: deque([[1, 4], [2, 3], [4, 6]]), 4: deque([[3, 6]])}




def dfs(sNode):
    eNode,elen=sNode,0
    visited=[0 for _ in range(N)]
    visited[eNode]=1

    dq=deque([(sNode,0)])
    while dq:
        n,l=dq.popleft()
        for nn,ll in mat[n]:
            if visited[nn]==0:
                dq.append([nn,ll+l])
                visited[nn]=1
                if ll+l>elen :
                    elen=ll+l
                    eNode=nn


    return eNode, elen

a,b=dfs(0)
a,b=dfs(a)
print(b)


