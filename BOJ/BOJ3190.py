import sys
from collections import deque

N=int(input())
arr=[[0]*(N+2) for _ in range(N+2)]
K=int(input())
for k in range(K):
    r,c=list(map(int,sys.stdin.readline().strip().split(' ')))
    arr[r][c]=1
L=int(input())
times={}
for l in range(L):
    r,c=sys.stdin.readline().strip().split(' ')
    times[int(r)]=c

dr=[0,1,0,-1]
dc=[1,0,-1,0]
k=0

r,c=1,1
mset=set([(1,1)])
dq=deque([(1,1)]) #snake

for t in range(1, 1000000000000):
    nr,nc=r+dr[k],c+dc[k]
    if t in times:
        if times[t]=='L':
            k=(k+4-1)%4
        elif times[t]=='D':
            k=(k+1)%4
    if (nr<=0 or N+1<=nr or nc<=0 or N+1<=nc): # block
        print(t)
        break
    if (nr,nc) in mset: # my body
        print(t)
        break
    
    # memo snake body
    dq.append((nr,nc))
    mset.add((nr,nc))
    r,c=nr,nc
    if arr[nr][nc]!=1: #not apple
        lastR,lastC=dq.popleft()
        mset.remove((lastR,lastC))
    arr[nr][nc]=0 # eat apple