from collections import deque
import sys
def hello():
    V,E=map(int,sys.stdin.readline().strip().split(" "))
    matrix={i:[] for i in range(V)}    
    for j in range(E):
        x,y=map(int,sys.stdin.readline().strip().split(" "))
        matrix[x-1].append(y-1)
        matrix[y-1].append(x-1)

    dq=deque([0])
    visited=[100 if len(matrix[i])==0 else 0 for i in range(V)] # 0: not visit, 1&-1=> check, 100:not linked
    for j in range(0,len(visited)):
        if visited[j]==0:
            dq.append(j)
            visited[j]=1
            break
        
    while dq:
        n=dq.popleft()
        for j in matrix[n]:
            if visited[j]==visited[n]:
                return False
            elif visited[j]==0:
                visited[j]=-1*visited[n]
                dq.append(j)
        if not dq:
            for j in range(0,len(visited)):
                if visited[j]==0:
                    dq.append(j)
                    visited[j]=1
                    break
    return True

K=int(input())
for K in range(0,K):
    if hello(): print("YES")
    else: print("NO")
    

