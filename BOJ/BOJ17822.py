from collections import deque
# N,M,T=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# rot=[list(map(int,input().split(' '))) for _ in range(T)]

# print(arr)
# print(rot)

# N,M,T=4,4,4
# arr=[[1, 1, 2, 3], [5, 2, 4, 2], [3, 1, 3, 5], [2, 1, 3, 2]]
# rot=[[2, 0, 1],[3,1,3],[2,0,2],[3,1,1]]

N,M,T=4,6,3
arr=[[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9]]    
rot=[[2, 1, 4], [3, 0, 1], [2, 1, 2]]

# arr=[[1,2,3],[4,5,6]]
# hello=arr[0][-1:]+arr[0][:-1] # 양수 반시계, 음수 시계
# print(hello)
# arr[0]=hello
# print(arr)

for t in range(T):
    x,d,k=rot[t]
    for i in range(x-1,N,x):
        tmp=-1*k if d==0 else k 
        arr[i]=arr[i][tmp:]+arr[i][:tmp]
    print(arr)
    status=False
    visited=[[0 for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr[r][c]==0 or visited[r][c]==1:
                continue
            if (arr[r][c]==arr[r][(c+1)%M] or
                arr[r][c]==arr[r][(c-1+M)%M] or
                (r+1<N and arr[r][c]==arr[r+1][c]) or
                (r-1>0 and arr[r][c]==arr[r-1][c])):
                dq=deque([(r,c)])
                visited[r][c]=1
                status=True
                while dq:
                    rr,cc=dq.popleft()
                    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr,nc=rr+dr,(cc+dc+M)%M
                        if nr<0 or nr>=N: continue
                        if arr[r][c]==arr[nr][nc] and visited[nr][nc]==0:
                            dq.append((nr,nc))
                            visited[nr][nc]=1
                            arr[nr][nc]=0
                arr[r][c]=0
    if status==False:
        totalsum=sum([sum(row) for row in arr])
        cnt=N*M-sum([row.count(0) for row in arr])
        avg=totalsum/cnt
        for r in range(N):
            for c in range(M):
                if arr[r][c]==0: continue
                if arr[r][c]>avg:
                    arr[r][c]-=1
                elif arr[r][c]<avg:
                    arr[r][c]+=1








summ=sum([sum(row) for row in arr])
print(summ)