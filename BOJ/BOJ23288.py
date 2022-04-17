################################################22.04.18

from collections import deque

N,M,K=map(int,input().split(' '))

arr=[list(map(int,input().split(' '))) for _ in range(N)]

R,C,D=0,0,0
direc=[(0,1),(1,0),(0,-1),(-1,0)]

dice=[1,2,3,4,5,6] # A idx = dice[5]

def mrotate(d):
    global dice
    tmp=[0,0,0,0,0,0]
    if d==0:
        tmp=[dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif d==2:
        tmp=[dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif d==1:
        tmp=[dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    elif d==3:
        tmp=[dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]  
    dice=tmp
    return

def bfs():
    tmp=arr[R][C]
    visited=[[0 if arr[i][j]==tmp else 1 for j in range(M)] for i in range(N)]
    dq=deque([(R,C)])
    visited[R][C]=1
    cnt=1
    while dq:
        r,c=dq.popleft()
        for dr,dc in direc:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0:
                dq.append((nr,nc))
                visited[nr][nc]=1
                cnt+=1
    return cnt*tmp
        


score=0
for _ in range(K):
    nr,nc=R+direc[D][0],C+direc[D][1]
    if 0>nr or 0>nc or N<=nr or M<=nc:
        D=(D+2)%4
        nr,nc=R+direc[D][0],C+direc[D][1]  
    R,C=nr,nc          
    mrotate(D)
    
    score+=bfs()
    
    if dice[5] > arr[R][C]:
        D=(D+1)%4
    elif dice[5] < arr[R][C]:
        D=(D-1+4)%4
print(score)
















################################################33
# from collections import deque
# N,M,K=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]

# horizon=[1,3,6,4]
# vertical=[1,5,6,2]
# d=0
# r,c=0,0
# dr=[0,1,0,-1]
# dc=[1,0,-1,0]


# answer=0
# for _ in range(K):
#     # step 1 
#     if r+dr[d]<0 or r+dr[d]>=N or c+dc[d]<0 or c+dc[d]>=M:
#         d=(d+2)%4
    
#     r,c=r+dr[d],c+dc[d]
#     if d==0: #right
#         horizon=horizon[-1:]+horizon[:-1]
#         vertical[0]=horizon[0]
#         vertical[2]=horizon[2]
#     elif d==1: #down
#         vertical=vertical[-1:]+vertical[:-1]
#         horizon[0]=vertical[0]
#         horizon[2]=vertical[2]
#     elif d==2: #left
#         horizon=horizon[1:]+horizon[:1]
#         vertical[0]=horizon[0]
#         vertical[2]=horizon[2]  
#     elif d==3: #up
#         vertical=vertical[1:]+vertical[:1]
#         horizon[0]=vertical[0]
#         horizon[2]=vertical[2]


#     #step 2
#     num=arr[r][c]
#     cnt=1
#     visit=[[0]*M for _ in range(N)]
#     visit[r][c]=1
#     dq=deque([(r,c)])
#     while dq:
#         rr,cc=dq.popleft()
#         for ddr,ddc in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nr,nc=rr+ddr,cc+ddc
#             if 0<=nr<N and 0<=nc<M and visit[nr][nc]==0 and arr[nr][nc]==num:
#                 cnt+=1
#                 dq.append((nr,nc))
#                 visit[nr][nc]=1
#     answer+=(arr[r][c]*cnt)

#     # step 3
#     if horizon[2] > arr[r][c]:
#         d=(d+1)%4
#     elif horizon[2] < arr[r][c]:
#         d=(d-1+4)%4

# print(answer)





# # from collections import deque
# # N,M,K=map(int,input().split(' '))
# # arr=[list(map(int,input().split(' '))) for _ in range(N)]

# # horizon=[1,3,6,4]
# # vertical=[1,5,6,2]
# # d=0
# # r,c=0,0
# # dr=[0,1,0,-1]
# # dc=[1,0,-1,0]

# # def rotate(direc):
# #     global horizon
# #     global vertical
# #     if direc==0: #right
# #         horizon=horizon[-1:]+horizon[:-1]
# #         vertical[0]=horizon[0]
# #         vertical[2]=horizon[2]
# #     elif direc==1: #down
# #         vertical=vertical[-1:]+vertical[:-1]
# #         horizon[0]=vertical[0]
# #         horizon[2]=vertical[2]
# #     elif direc==2: #left
# #         horizon=horizon[1:]+horizon[:1]
# #         vertical[0]=horizon[0]
# #         vertical[2]=horizon[2]  
# #     elif direc==3: #up
# #         vertical=vertical[1:]+vertical[:1]
# #         horizon[0]=vertical[0]
# #         horizon[2]=vertical[2]
# #     return

# # def bfs(num):
# #     cnt=1
# #     visit=[[0]*M for _ in range(N)]
# #     visit[r][c]=1
# #     dq=deque([(r,c)])
# #     while dq:
# #         rr,cc=dq.popleft()
# #         for ddr,ddc in [(1,0),(-1,0),(0,1),(0,-1)]:
# #             nr,nc=rr+ddr,cc+ddc
# #             if 0<=nr<N and 0<=nc<M and visit[nr][nc]==0 and arr[nr][nc]==num:
# #                 cnt+=1
# #                 dq.append((nr,nc))
# #                 visit[nr][nc]=1
# #     return cnt


# # answer=0
# # for _ in range(K):
# #     # step 1 
# #     if r+dr[d]<0 or r+dr[d]>=N or c+dc[d]<0 or c+dc[d]>=M:
# #         d=(d+2)%4
# #     rotate(d)
# #     r,c=r+dr[d],c+dc[d]

# #     #step 2
# #     n=bfs(arr[r][c])
# #     answer+=(arr[r][c]*n)

# #     # step 3
# #     if horizon[2] > arr[r][c]:
# #         d=(d+1)%4
# #     elif horizon[2] < arr[r][c]:
# #         d=(d-1+4)%4

# # print(answer)

