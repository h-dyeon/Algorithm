import sys
from collections import deque


N, M, K=map(int, sys.stdin.readline().strip().split(' '))

INF=9999999
visited=[[INF]*M for _ in range(N)]
dr=[0,-1,0,1]
dc=[1,0,-1,0]

matrix = [list(sys.stdin.readline().strip()) for _ in range(N)]
x1, y1, x2, y2=map(int, sys.stdin.readline().strip().split(' '))
x1-=1; y1-=1; x2-=1; y2-=1

queue=deque([(x1,y1)])
visited[x1][y1]=0
while queue:
    r,c=queue.popleft()
    for i in range(4):
        for j in range(1,K+1):
            newR=r+j*dr[i]
            newC=c+j*dc[i]
            if 0>newR or newR>=N or 0>newC or newC>=M:
                break
            if matrix[newR][newC]=='#':
                break

            if visited[newR][newC] < visited[r][c]+1:
                break
            else:
                visited[newR][newC]=visited[r][c]+1
                queue.append((newR,newC))
            # if visited[newR][newC] == INF:
            #     visited[newR][newC]=visited[r][c]+1
            #     queue.append((newR,newC))
            # elif visited[newR][newC] == visited[r][c]+1:
            #     continue
            # elif visited[newR][newC] > visited[r][c]+1:
            #     continue
            # else:
            #     break
if visited[x2][y2]==INF:
    print(-1)
else:
    print(visited[x2][y2])

