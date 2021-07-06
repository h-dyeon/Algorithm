from collections import deque
matrix=[[9,9,4],[6,6,8],[2,1,1]]
m=len(matrix)
n=len(matrix[0])
dr=[0,-1,0,1]
dc=[1,0,-1,0]

aa=0
for i in range(m):
    for j in range(n):
        
        #BFS
        answer=1
        dq=deque([[i,j]]) # row, col, length
        visited=[[0]*n for _ in range(m)]
        visited[i][j]=1 # step count

        while len(dq)!=0:
            r,c=dq.popleft()
            for k in range(4):
                newR=r+dr[k]
                newC=c+dc[k]
                if 0<=newR<m and 0<=newC<n:
                    if matrix[newR][newC]>matrix[r][c] and visited[newR][newC]<visited[r][c]+1:
                        if [newR,newC] not in dq:
                            dq.append([newR,newC])
                        visited[newR][newC]=visited[r][c]+1
                        answer=max(answer,visited[r][c]+1)
                        
        aa=max(aa,answer)
print(aa)
#return aa # leetcode
