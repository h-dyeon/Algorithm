import sys


N=int(sys.stdin.readline().strip())
matrix=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]

visited=[[[0]*3 for _ in range(N)] for _ in range(N)]

visited[0][1][0]=1
for i in range(N):
    for j in range(N):
        if i!=N-1 and matrix[i+1][j]!=1:
            visited[i+1][j][1]+=visited[i][j][1]
            visited[i+1][j][1]+=visited[i][j][2]
        if j!=N-1 and matrix[i][j+1]!=1:
            visited[i][j+1][0]+=visited[i][j][0]
            visited[i][j+1][0]+=visited[i][j][2]
        if j!=N-1 and i!=N-1 and \
            matrix[i][j+1]!=1 and \
            matrix[i+1][j]!=1 and \
                matrix[i+1][j+1]!=1:
            visited[i+1][j+1][2]+=visited[i][j][0]
            visited[i+1][j+1][2]+=visited[i][j][1]
            visited[i+1][j+1][2]+=visited[i][j][2]

print(visited[N-1][N-1][0]+visited[N-1][N-1][1]+visited[N-1][N-1][2])
        