import sys
from collections import deque

# N,M,x,y,K=list(map(int,sys.stdin.readline().strip().split(' ')))
# arr=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]
# order=list(map(int,sys.stdin.readline().strip().split(' ')))
# print(arr)
# print(order)
 
N,M,x,y,K=3,3,0,0,16
arr=[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
order=[4, 4, 1, 1, 3, 3, 2, 2, 4, 4, 1, 1, 3, 3, 2, 2]

w=deque([0,0,0,0])
h=deque([0,0,0,0])
dx=[0,0,0,-1,1] #row, 1 index
dy=[0,1,-1,0,0] #col, 1 index

def mrotate(oo):
    if oo==4:
        h.rotate(1)
        w[0]=h[0]
        w[2]=h[2]
    elif oo==3:
        h.rotate(-1)
        w[0]=h[0]
        w[2]=h[2]
    elif oo==1:
        w.rotate(1)
        h[0]=w[0]
        h[2]=w[2]
    elif oo==2:
        w.rotate(-1)
        h[0]=w[0]
        h[2]=w[2]
    return


for o in order:
    nx=x+dx[o]
    ny=y+dy[o]
    if 0<=nx<N and 0<=ny<M:
        mrotate(o)
        if arr[nx][ny]==0:
            arr[nx][ny]=w[2] #bottom of dice
        else:
            w[2]=arr[nx][ny] #arr to dice
            h[2]=arr[nx][ny]   
            arr[nx][ny]=0 
        print(o,"---",w[0],w,h,nx,ny)
        x,y=nx,ny


