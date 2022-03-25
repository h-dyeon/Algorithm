import sys
import copy
from collections import deque

# N,M=list(map(int,sys.stdin.readline().strip().split(' ')))
# arr=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]
# print(arr)
N=4
M=6
arr=[[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]
dr=[1,0,-1,0]
dc=[0,1,0,-1]

def checkvirus(a,b,c):
    narr=copy.deepcopy(arr)
    # narr[int(a/M)][a%M]=1
    # narr[int(b/M)][b%M]=1
    # narr[int(c/M)][c%M]=1
    narr[a[0]][a[1]]=1
    narr[b[0]][b[1]]=1
    narr[c[0]][c[1]]=1

    visited=[[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if narr[i][j]==2 and visited[i][j]==False:
                dq=deque([(i,j)])
                visited[i][j]=True
                while dq:
                    x,y=dq.popleft()
                    for k in range(4):
                        nx=x+dr[k]
                        ny=y+dc[k]
                        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False and narr[nx][ny]==0:
                            narr[nx][ny]=2
                            visited[nx][ny]=True
                            dq.append((nx,ny))
    
    return sum([narr[row].count(0) for row in range(N)])
    # ans=0
    # for i in range(N):
    #     for j in range(M):
    #         if narr[i][j]==0:
    #             ans+=1
    # return ans


answer=0
case=[(i, j) for i in range(N) for j in range(M) if arr[i][j]==0]
for i in range(len(case)-2):
    for j in range(i+1, len(case)-1):
        for k in range(j+1, len(case)):
            A, B, C = case[i], case[j], case[k]
            answer=max(answer,checkvirus(A,B,C))
print(answer)

# answer=0
# for i in range(N*M-2):
#     ir,ic=int(i/M),i%M
#     if arr[ir][ic]!=0: continue
#     for j in range(i+1,N*M-1):
#         jr,jc=int(j/M),j%M
#         if arr[jr][jc]!=0: continue
#         for k in range(j+1,N*M):
#             kr,kc=int(k/M),k%M
#             if arr[kr][kc]!=0: continue
#             answer=max(answer,checkvirus(i,j,k))
# print(answer)

            