from collections import deque

R,C,K=map(int,input().split(' '))
onepoong=[]
testpos=[]
for i in range(R):
    t=list(map(int,input().split(' ')))
    for j in range(C):
        if 0<t[j]<5:
            tmp=-1
            if t[j]==1: tmp=0 #right
            elif t[j]==2: tmp=2 #left
            elif t[j]==3: tmp=1 # up
            elif t[j]==4: tmp=3 #down
            onepoong.append((i,j,tmp))
        elif t[j]==5:
            testpos.append((i,j))

W=int(input())
walls={}
for _ in range(W):
    x,y,t=map(int,input().split(' '))
    if t==0:
        walls.setdefault((x-1,y-1),[]).append((x-2,y-1))
        walls.setdefault((x-2,y-1),[]).append((x-1,y-1))
    elif t==1:
        walls.setdefault((x-1,y-1),[]).append((x-1,y))
        walls.setdefault((x-1,y),[]).append((x-1,y-1))


dr=[0,-1,0,1]
dc=[1,0,-1,0]

def checkwall(r,c,nr,nc):
    if (r,c) not in walls:
        return False
    if (nr,nc) in walls[(r,c)]:
        return True
    return False

def blow(rr,cc,d):
    tmp=[[0]*C for _ in range(R)]

    nr,nc=rr+dr[d],cc+dc[d]
    tmp[nr][nc]=5
    dq=deque([(nr,nc,5)])
    while dq:
        r,c,v=dq.popleft()
        nr,nc=r+dr[d],c+dc[d]
        if 0<=nr<R and 0<=nc<C and not checkwall(r,c,nr,nc):
            tmp[nr][nc]=v-1
            if v>2:
                dq.append((nr,nc,v-1))
        
        midr,midc=r+dr[(d+1)%4],c+dc[(d+1)%4]
        nr,nc=r+dr[d]+dr[(d+1)%4],c+dc[d]+dc[(d+1)%4]
        if 0<=nr<R and 0<=nc<C and not (checkwall(r,c,midr,midc) or checkwall(midr,midc, nr,nc)):
            tmp[nr][nc]=v-1
            if v>2:
                dq.append((nr,nc,v-1))
        
        midr,midc=r+dr[(d+3)%4],c+dc[(d+3)%4]
        nr,nc=r+dr[d]+dr[(d+3)%4],c+dc[d]+dc[(d+3)%4]
        if 0<=nr<R and 0<=nc<C and not (checkwall(r,c,midr,midc) or checkwall(midr,midc, nr,nc)):
            tmp[nr][nc]=v-1
            if v>2:
                dq.append((nr,nc,v-1))
    return tmp

def adjust(arr):
    tmp=[row[:] for row in arr]
    for i in range(R):
        for j in range(C):
            if j+1<C and not checkwall(i,j,i,j+1):
                a=int(abs(arr[i][j+1]-arr[i][j])/4)
                if arr[i][j]<arr[i][j+1]:
                    tmp[i][j+1]-=a
                    tmp[i][j]+=a
                elif arr[i][j]>arr[i][j+1]:
                    tmp[i][j]-=a
                    tmp[i][j+1]+=a
            if i+1<R and not checkwall(i,j,i+1,j):
                a=int(abs(arr[i+1][j]-arr[i][j])/4)
                if arr[i][j]<arr[i+1][j]:
                    tmp[i+1][j]-=a
                    tmp[i][j]+=a
                elif arr[i][j]>arr[i+1][j]:
                    tmp[i][j]-=a
                    tmp[i+1][j]+=a
    for r in tmp:
        print(r)
    print("------------------")
    return tmp


add_onepong=[[0]*C for _ in range(R)]
for i,j,d in onepoong:
        tmp=blow(i,j,d)
        add_onepong=[[add_onepong[r][c]+tmp[r][c] for c in range(C)] for r in range(R)]

arr=[[0]*C for _ in range(R)]
answer=101
for choco in range(1,101):
    # blow
    arr=[[arr[r][c]+add_onepong[r][c] for c in range(C)] for r in range(R)] 
    
    # adjust
    a=adjust(arr)
    arr=a
    # minus
    for i in [0,R-1]:
        for j in range(C):
            if arr[i][j]>0:
                arr[i][j]-=1
    for i in [0,C-1]:
        for j in range(R):
            if arr[j][i]>0:
                arr[j][i]-=1
    if choco==50:
        print("c")
    
    # check
    status=True
    for i,j in testpos:
        if arr[i][j]<K:
            status=False
            break
    if status:
        answer=choco
        break


print(answer)   

