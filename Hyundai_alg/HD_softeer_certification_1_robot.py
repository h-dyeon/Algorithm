import sys
from collections import deque
# L left 90 rotation
# R right 90 rotation
# A go straight 2

# not double visit

# H,W = map(int,sys.stdin.readline().strip().split(' '))
# matrix=[list(sys.stdin.readline().strip()) for _ in range(H)]

H=9
W=14
matrix=[['.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'], ['.', '#', '#', '#', '#', '#', '.', '.', '.', '#', '#', '#', '.', '.'], ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.'], ['.', '#', '.', '#', '#', '#', '#', '#', '.', '.', '.', '#', '#', '#'], ['.', '#', '.', '#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#'], ['.', '#', '#', '#', '.', '#', '#', '#', '.', '.', '.', '.', '.', '#'], ['.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '#'], ['.', '.', '.', '.', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#']] 

command=[1,-1,0] #L,R,A
dr=[0,1,0,-1]
dc=[-1,0,1,0]

dir_to_char=['<','v','>','^'] # E,N,W,S

start_dq=deque()
for i in range(H):
    for j in range(W):
        if matrix[i][j]=='#':
            for k in range(4):
                if 0<=i+dr[k]<H and 0<=j+dc[k]<W and matrix[i+dr[k]][j+dc[k]]=='#' \
                    and 0<=i+2*dr[k]<H and 0<=j+2*dc[k]<W and matrix[i+2*dr[k]][j+2*dc[k]]=='#' :
                    if (not(0<=i+dr[(k+1)%4]<H and 0<=j+dc[(k+1)%4]<W) or matrix[i+dr[(k+1)%4]][j+dc[(k+1)%4]]=='.') \
                        and (not(0<=i+dr[(k+2)%4]<H and 0<=j+dc[(k+2)%4]<W) or matrix[i+dr[(k+2)%4]][j+dc[(k+2)%4]]=='.') \
                        and (not(0<=i+dr[(k+3)%4]<H and 0<=j+dc[(k+3)%4]<W) or matrix[i+dr[(k+3)%4]][j+dc[(k+3)%4]]=='.') :
                        start_dq.append([i,j])

                
r,c=start_dq.popleft()

first_dir=-1
for k in range(4):
    if 0<=r+dr[k]<H and 0<=c+dc[k]<W and matrix[r+dr[k]][c+dc[k]]=='#':
        first_dir=k
        break


mstr=''
visited=[[0]*W]*H
visited[r][c]=1
dq=deque([first_dir,r,c]) #now direction, row, col
while True:

    for k in range(4):
        if 0<=r+dr[k+]<H and 0<=c+dc[k]<W and matrix[r+dr[k]][c+dc[k]]=='#':
            mstr+=


print(r+1,c+1)
print(dir_to_char[first_dir])
