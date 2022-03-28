from collections import deque
N,L,R=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]

# def check():
#     for i in range(N):
#         for j in range(N):
#             if j<N-1 and abs(L<=arr[i][j]-arr[i][j+1])<=R:
#                 return True
#             if i<N-1 and abs(L<=arr[i][j]-arr[i+1][j])<=R:
#                 return True
#     return False
            
for t in range(10000000000):
    status=True
    visited=[[False]*N for _ in range(N)] #initialize
    for i in range(N):
        for j in range(N):
            if visited[i][j]==False:

                summ=arr[i][j] # if changed 1, not change 0
                visited[i][j]=True
                dq=deque([(i,j)])
                mset=set([(i,j)])
                while dq:
                    r,c=dq.popleft()
                    for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nr=r+dr
                        nc=c+dc
                        if 0<=nr<N and 0<=nc<N and visited[nr][nc]==False:
                            if L<=abs(arr[r][c]-arr[nr][nc])<=R:
                                visited[nr][nc]=True
                                mset.add((nr,nc))
                                dq.append((nr,nc))
                                summ+=arr[nr][nc]
                l=len(mset)
                for r,c in mset:
                    arr[r][c]=int(summ/l)
                if summ>arr[i][j]:
                    status=False
    if status:
        print(t)
        break