import sys


N,M=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]
print(arr)

# N,M=4,6
# arr=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 6, 0], [0, 0, 0, 0, 0, 0]]
dr=[1,0,-1,0]
dc=[0,1,0,-1]
answer=100000000000 #min

#find cctv
cctv=[]
for i in range(N):
    for j in range(M):
        if 0<arr[i][j]<6:
            cctv.append((i,j,arr[i][j]))

def going(copyarr,direc,r,c):
    for k in range(1,1000):
        nr=r+k*dr[direc]
        nc=c+k*dc[direc]
        if 0<=nr<N and 0<=nc<M and copyarr[nr][nc]!=6:
            copyarr[nr][nc]=99
        else:
            break
    return copyarr


def check(copyarr,idx):
    global answer
    tmp=sum([copyarr[i].count(0) for i in range(N)])
    if tmp==0 or len(cctv)==idx:  
        answer=min(answer,tmp)
        return

    r,c,t=cctv[idx]
    
    if t==1:
        for d in range(4):
            narr=[r[:] for r in copyarr]
            check(going(narr,d,r,c),idx+1)
    elif t==2:
        for i in range(2):
            narr=[r[:] for r in copyarr]
            going(narr,i,r,c)
            going(narr,i+2,r,c)
            check(narr,idx+1)
    elif t==3:
        for i in range(4):
            narr=[r[:] for r in copyarr]
            going(narr,i,r,c)
            going(narr,(i+1)%4,r,c)
            check(narr,idx+1)
    elif t==4:
        for i in range(4):
            narr=[r[:] for r in copyarr]
            going(narr,i,r,c)
            going(narr,(i+1)%4,r,c)
            going(narr,(i+2)%4,r,c)
            check(narr,idx+1)
    elif t==5:
        narr=[r[:] for r in copyarr]
        for d in range(4):
            going(narr,d,r,c)
        check(narr,idx+1)

copyarr=[r[:] for r in arr]
check(copyarr,0)
print(answer)
