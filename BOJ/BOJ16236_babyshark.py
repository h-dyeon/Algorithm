#################220412
from collections import deque
N=int(input())
arr=[list(map(int,input().split(' '))) for _ in range(N)]
print(arr)
R,C=0,0 #shark
sharkBody=2
eatfish=0
numfish=0
for i in range(N):
    for j in range(N):
        if arr[i][j]==9:
            R,C=i,j
        elif 1<=arr[i][j]<=6:
            numfish+=1
direc=[(1,0),(-1,0),(0,1),(0,-1)]


time=0
while True:
    if numfish==0:
        print(time)
        break
    
    mindist=1e9
    whatfish=[]
    visited=[[-1]*N for _ in range(N)]
    visited[R][C]=0
    dq=deque([(R,C)])
    while dq:
        r,c=dq.popleft()
        for dr,dc in direc:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==-1 and arr[nr][nc]<=sharkBody:
                if 1<=arr[nr][nc]<sharkBody:
                    mindist=min(mindist,visited[r][c]+1)
                    whatfish.append((visited[r][c]+1,nr,nc))
                visited[nr][nc]=visited[r][c]+1
                if mindist>visited[r][c]+1:
                    dq.append((nr,nc))
    if len(whatfish)==0:
        print(time)
        break
    whatfish=sorted(whatfish,key=lambda x:[x[0],x[1],x[2]])
    d,x,y=whatfish[0]
    arr[R][C]=0
    R,C=x,y
    arr[x][y]=0
    numfish-=1
    eatfish+=1
    time+=visited[x][y]
    if sharkBody==eatfish:
        eatfish=0
        sharkBody+=1
    






#######################################

# from collections import deque

# N=int(input())
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# print(arr)

# # N=4
# # arr=[[4, 3, 2, 1], [0, 0, 0, 0], [0, 0, 9, 0], [1, 2, 3, 4]]

# def findshark():
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j]==9:
#                 return i,j
# sharkX,sharkY=findshark()
# fishX,fishY=1e9,1e9

# mtime=0
# shark=2
# numFish=0
# nowdist=0
# # eatlist=deque([]) #pos_x,pos_y, distance # position of fishes
# visited=[[False]*N for _ in range(N)]
# visited[sharkX][sharkY]=True
# dq=deque([(sharkX,sharkY,0)]) #pos_x,pos_y, distance


# while dq:
#     r,c,d=dq.popleft()
#     if d>nowdist:
#         if fishX==1e9 and fishY==1e9:
#             nowdist=d
#         # if len(eatlist)==0:
#         #     nowdist=d
#         else:
#             # update distance
#             mtime+=d
#             nowdist=0
            
#             # update position
#             arr[sharkX][sharkY]=0
#             sharkX,sharkY=fishX,fishY
#             # sharkX,sharkY=1e9,1e9
#             # for x,y,d in eatlist:
#             #     if (sharkX>x) or (sharkX==x and sharkY>y):
#             #         sharkX,sharkY=x,y
#             arr[sharkX][sharkY]=9
            
#             # update size of shark
#             numFish+=1
#             if shark==numFish:
#                 shark+=1
#                 numFish=0

#             # initialize
#             fishX,fishY=1e9,1e9
#             # eatlist=deque([])
#             visited=[[False]*N for _ in range(N)]
#             visited[sharkX][sharkY]=True
#             dq=deque([(sharkX,sharkY,0)])    
#             # print("----------------")
#             continue     
    
#     for dr,dc in [(-1,0),(0,-1),(0,1),(1,0)]:
#         nr,nc=r+dr,c+dc
#         if 0<=nr<N and 0<=nc<N and arr[nr][nc]<=shark and visited[nr][nc]==False:
#             if 0<arr[nr][nc]<shark:
#                 if (fishX>nr) or (fishX==nr and fishY>nc):
#                     fishX,fishY=nr,nc
#                 # eatlist.append((nr,nc,d+1))
#             # print(nr,nc,d+1)
#             visited[nr][nc]=True    
#             dq.append((nr,nc,d+1))
# print(mtime)