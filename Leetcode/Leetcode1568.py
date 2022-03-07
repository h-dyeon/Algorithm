from collections import deque
grid =[[0,0,0],[0,1,0],[0,0,0]]

def checkDisconnected():
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    numIsland=0
    visited=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1 and visited[i][j]!=1:
                numIsland+=1
                # one island
                dq=deque([(i,j)])
                visited[i][j]=1
                while dq:
                    r,c=dq.popleft()
                    for k in range(4):
                        nr=r+dr[k]
                        nc=c+dc[k]
                        if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1 and visited[nr][nc]!=1:
                            dq.append([nr,nc])
                            visited[nr][nc]=1
    return numIsland


total=sum([i for a in grid for i in a])
if total<=1:
    print(total)

if checkDisconnected()>1: print(0)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==1:
            grid[i][j]=0
            if checkDisconnected()>1: print(1)
            grid[i][j]=1
print(2)