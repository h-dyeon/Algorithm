from collections import deque

N,L,R=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]

direc=[(1,0),(-1,0),(0,1),(0,-1)]


for days in range(2002):
    ismoved=False

    visited=[[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j]==1: continue

            status=False
            if j+1<N and L<=abs(arr[i][j]-arr[i][j+1])<=R:
                status=True
            if i+1<N and L<=abs(arr[i][j]-arr[i+1][j])<=R:
                status=True
            
            #find union
            if status:
                ismoved=True
                cnt=1
                ssum=arr[i][j]
                visited[i][j]=1
                dq=deque([(i,j)])

                mset=set([(i,j)])

                # record=[[0]*N for _ in range(N)]
                # record[i][j]=1
                while dq:
                    r,c=dq.popleft()
                    for dr,dc in direc:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and L<=abs(arr[nr][nc]-arr[r][c])<=R:
                            visited[nr][nc]=1
                            cnt+=1
                            ssum+=arr[nr][nc]
                            dq.append((nr,nc))
                            mset.add((nr,nc))
                            # record[nr][nc]=1
                
                a=int(ssum/cnt)
                for r,c in mset:
                    arr[r][c]=a

                # for r in range(N):
                #     for c in range(N):
                #         if record[r][c]==1:
                #             arr[r][c]=a


    if ismoved==False:
        print(days)
        break

