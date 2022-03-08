import sys
from collections import deque 

M,N=map(int,sys.stdin.readline().strip().split(' '))
matrix=[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

# N,M=3,3
# matrix=[[0, 1, 1], [1, 1, 1], [1, 1, 0]]
answer=[[1e9 for _ in range(M)] for _ in range(N)]

dr=[1,0,-1,0]
dc=[0,1,0,-1]

answer[0][0]=0
dq=deque([(0,0)])#row,col
while dq:
    r,c=dq.popleft()
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<N and 0<=nc<M and answer[nr][nc]>answer[r][c]+matrix[nr][nc]:
            answer[nr][nc]=answer[r][c]+matrix[nr][nc]
            dq.append([nr,nc])

print(answer[N-1][M-1])





# import sys
# from collections import deque 

# M,N=map(int,sys.stdin.readline().strip().split(' '))
# matrix=[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

# # N,M=3,3
# # matrix=[[0, 1, 1], [1, 1, 1], [1, 1, 0]]
# answer=[[1e9 for _ in range(M)] for _ in range(N)]

# dr=[1,0,-1,0]
# dc=[0,1,0,-1]

# answer[0][0]=0
# dq=deque([(0,0,0)])#row,col, num
# while dq:
#     r,c,n=dq.popleft()
#     for i in range(4):
#         nr=r+dr[i]
#         nc=c+dc[i]
#         if 0<=nr<N and 0<=nc<M and answer[nr][nc]>n+matrix[nr][nc]:
#             answer[nr][nc]=n+matrix[nr][nc]
#             dq.append([nr,nc,answer[nr][nc]])

# print(answer[N-1][M-1])


