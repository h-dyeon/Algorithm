from collections import deque
N,Q=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(2**N)]
Llist=list(map(int,input().split(' ')))

# N,Q=3,1
# arr=[[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6,7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]
# Llist=[1]

# N,Q=3,5
# arr=[[1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]]
# Llist=[1,2,0,3,2]
wholesize=2**N

def mrotate(L):
    global arr
    global wholesize
    if L==0:
        return
    
    partsize=2**L
    narr=[[0]*wholesize for _ in range(wholesize)]
    for i in range(0,wholesize,partsize):
        for j in range(0,wholesize,partsize):
            r,c=i,j
            for size in range(int(partsize/2)):
                nr,nc=r+size,c+size
                npartsize=partsize-size*2
                for k in range(npartsize-1):
                    narr[nr+k][nc+npartsize-1]=arr[nr][nc+k]
                    narr[nr+npartsize-1][nc+npartsize-1-k]=arr[nr+k][nc+npartsize-1]
                    narr[nr+npartsize-1-k][nc]=arr[nr+npartsize-1][nc+npartsize-1-k]
                    narr[nr][nc+k]=arr[nr+npartsize-1-k][nc]
    arr=narr
    return

def minusIce():
    global arr
    # global wholesize
    narr=[row[:] for row in arr]
    for r in range(wholesize):
        for c in range(wholesize):
            cnt=0
            if r+1<wholesize and arr[r+1][c]>0:
                cnt+=1
            if r-1>=0 and arr[r-1][c]>0:
                cnt+=1
            if c+1<wholesize and arr[r][c+1]>0:
                cnt+=1
            if c-1>=0 and arr[r][c-1]>0:
                cnt+=1
            
            if cnt<3:
                narr[r][c]=max(narr[r][c]-1,0)
    arr=narr
    return

def findbig(summ):
    if summ==0:
        return 0
    answer=1
    visited=[[0]*wholesize for _ in range(wholesize)]
    for r in range(wholesize):
        for c in range(wholesize):
            status=False
            if c<wholesize-1 and arr[r][c]*arr[r][c+1]!=0: # connected
                status=True
            if r<wholesize-1 and arr[r][c]*arr[r+1][c]!=0: # connected
                status=True

            if status==False: continue

            dq=deque([(r,c)])
            visited[r][c]=1
            cnt=1
            while dq:
                rr,cc=dq.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc=rr+dr,cc+dc
                    if 0<=nr<wholesize and 0<=nc<wholesize and arr[nr][nc]>0 and visited[nr][nc]==0:
                        visited[nr][nc]=1
                        dq.append((nr,nc))
                        cnt+=1
            answer=max(answer,cnt)           
    return answer


for L in Llist:
    mrotate(L)
    minusIce()


summ=sum([sum(row) for row in arr])
print(summ)
print(findbig(summ))
