from collections import deque
grid = [[40,10],[30,20]]
k = 1

R=len(grid)
C=len(grid[0])
newgrid=[[0]*C for _ in range(R)]

for i in range(int(min(R,C)/2)):
    dq=deque([])

    for j in range(i,R-i):
        dq.append(grid[j][i])
    for j in range(i+1,C-i):
        dq.append(grid[R-1-i][j])
    for j in range(R-1-i-1,i-1,-1):
        dq.append(grid[j][C-1-i])
    for j in range(C-1-i-1,i,-1):
        dq.append(grid[i][j])
    
    dq.rotate(k)

    for j in range(i,R-i):
        newgrid[j][i]=dq.popleft()
    for j in range(i+1,C-i):
        newgrid[R-1-i][j]=dq.popleft()
    for j in range(R-1-i-1,i-1,-1):
        newgrid[j][C-1-i]=dq.popleft()
    for j in range(C-1-i-1,i,-1):
        newgrid[i][j]=dq.popleft()

print(newgrid)