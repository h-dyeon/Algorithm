
####################################################### 22.04.14
from collections import deque
from dis import dis

from numpy import sort
N,M,feul=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]
RR,CC=map(int,input().split(' '))
RR-=1 #taxi start position
CC-=1
person=[[0]*4 for _ in range(M)]
nowperson=M
for i in range(M):
    a,b,c,d=map(int,input().split(' '))
    person[i]=[a-1,b-1,c-1,d-1]
    arr[a-1][b-1]=2 #start
    arr[c-1][d-1]=3 #finish
direc=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs_start(i,j): #start position
    visited=[[-2 if arr[i][j]==1 else -1 for j in range(N)] for i in range(N)]
    visited[i][j]=0
    dq=deque([(i,j)])

    tmp=nowperson # count people
    if arr[i][j]==2:
        tmp=nowperson-1
    
    while dq:
        r,c=dq.popleft()
        for dr,dc in direc:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==-1:
                visited[nr][nc]=visited[r][c]+1
                dq.append((nr,nc))
                if arr[nr][nc]==2:
                    tmp-=1
                    if tmp==0:
                        return visited
    return visited

def bfs_finish(i,j,a,b): #start position, final position
    visited=[[-2 if arr[i][j]==1 else -1 for j in range(N)] for i in range(N)]
    visited[i][j]=0
    dq=deque([(i,j)])    
    while dq:
        r,c=dq.popleft()
        for dr,dc in direc:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==-1:
                visited[nr][nc]=visited[r][c]+1
                dq.append((nr,nc))
                if nr==a and nc==b:
                    return visited[nr][nc]
    return 1e9


for _ in range(M):

    tmp=bfs_start(RR,CC) #find people
    sortarr=[]
    for i in range(M):
        if person[i][0]==-1:
            continue
        r,c=person[i][0],person[i][1]
        if tmp[r][c]>=0:
            sortarr.append((tmp[r][c],r,c,i)) # distance, r,c,idx
    
    if len(sortarr)==0:
        break
    sortarr=sorted(sortarr,key=lambda x:(x[0],x[1],x[2],i))
    d,r,c,idx=sortarr[0]
    if d>feul:
        break
    feul-=d
    RR,CC=r,c


    sr,sc,fr,fc=person[idx]

    d=bfs_finish(RR,CC,fr,fc)
    if d>feul:
        break
    feul+=d
    RR,CC=fr,fc
    arr[sr][sc]=0
    arr[fr][fc]=0
    person[idx]=[-1,-1,-1,-1]
    nowperson-=1

if nowperson==0:
    print(feul)
else:
    print(-1)





















#######################################################
# from collections import deque
# N,M,feul=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# r,c=map(int,input().split(' '))
# r-=1
# c-=1
# person=[list(map(int,input().split(' '))) for _ in range(M)] #1 index

# oklist=[0]*len(person)

# def calcdistmap(R,C):
#     visited=[[-1 if arr[i][j]==1 else 1e9+1 for j in range(N)] for i in range(N)]
#     visited[R][C]=0
#     dq=deque([(R,C)])
#     while dq:
#         r,c=dq.popleft()
#         for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
#             nr,nc=r+dr,c+dc
#             if 0<=nr<N and 0<=nc<N and visited[nr][nc]==(1e9+1):
#                 visited[nr][nc]=visited[r][c]+1
#                 dq.append((nr,nc))
    
#     return visited

# for _ in range(M):
#     distmap=calcdistmap(r,c)

#     # pick person
#     d=1e9
#     p,pr,pc=-1,1e9,1e9
#     for i in range(len(person)):
#         if oklist[i]==1: # already moved
#             continue
#         a,b=person[i][0]-1,person[i][1]-1
#         if distmap[a][b]<d:
#             d=distmap[a][b]
#             p,pr,pc=i,a,b
#         elif distmap[a][b]==d and (a<pr or (a==pr and b<pc)):
#             p,pr,pc=i,a,b
#     if p==-1:
#         break
    
#     # go to person
#     feul-=d
#     r,c=pr,pc

#     # move to target position
#     distmap=calcdistmap(r,c)
#     tr,tc=person[p][2]-1,person[p][3]-1
#     d=distmap[tr][tc]
#     if feul>=d:
#         feul+=d
#         r,c=tr,tc
#         oklist[p]=1
#     else:
#         break

# if sum(oklist)!=len(person) or feul<0:
#     print(-1)
# else:
#     print(feul)