
#####################################################22.04.15
N=int(input())
arr=[[0]*(N+6) for _ in range(N+6)]
for i in range(N):
    tmp=list(map(int,input().split(' ')))
    arr[i+3][3:3+N]=tmp
print(arr)

direc=[(0,-1),(1,0),(0,1),(-1,0)]

rate=[[(-2,0,2),(-1,-1,10),(-1,0,7),(-1,1,1),
        (0,-2,5),(1,-1,10),(1,0,7),(1,1,1),
        (2,0,2)],
        [(-1,-1,1),(-1,1,1),
        (0,-2,2),(0,-1,7),(0,1,7),(0,2,2),
        (1,-1,10),(1,1,10),
        (2,0,5)],
        [(-2,0,2),
        (-1,1,10),(-1,0,7),(-1,-1,1),
        (0,2,5),
        (1,1,10),(1,0,7),(1,-1,1),
        (2,0,2)],
        [(1,-1,1),(1,1,1),
        (0,-2,2),(0,-1,7),(0,1,7),(0,2,2),
        (-1,-1,10),(-1,1,10),
        (-2,0,5)]]

# N=10

# r,c=5,5
# for i in range(4):
#     arr=[[0]*(N+6) for _ in range(N+6)]
#     for a,b,d in rate[i]:
#         arr[r+a][c+b]=d
    
#     print("d")





def blow(r,c,d):
    y=arr[r][c]
    tmp=0
    for dr,dc,dy in rate[d]:
        arr[r+dr][c+dc]+=int(y*dy/100)
        tmp+=int(y*dy/100)
    if d==0:
        arr[r][c-1]+=arr[r][c]-tmp
    elif d==1:
        arr[r+1][c]+=arr[r][c]-tmp
    elif d==2:
        arr[r][c+1]+=arr[r][c]-tmp
    elif d==3:
        arr[r-1][c]+=arr[r][c]-tmp
    arr[r][c]=0

    return


# tornado
visited=[[False]*N for _ in range(N)]
r,c=int((N-1)/2),int((N-1)/2)
d=0
visited[r][c]=True
while r!=0 or c!=0:
    r,c=r+direc[d][0],c+direc[d][1]
    if arr[r+3][c+3]>0:
        blow(r+3,c+3,d)
    visited[r][c]=True
    if visited[r+direc[(d+1)%4][0]][c+direc[(d+1)%4][1]]==False:
        d=(d+1)%4

# sand
answer=0
answer+=(sum(arr[0])+sum(arr[1])+sum(arr[2]))
answer+=(sum(arr[N+3])+sum(arr[N+4])+sum(arr[N+5]))
for i in range(3,N+3):
    for j in [0,1,2,N+3,N+4,N+5]:
        answer+=arr[i][j]
print(answer)




#####################################################3
# N=int(input())
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# print(arr)


# # N=5
# # arr=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 10, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# # N=5
# # arr=[[100, 200, 300, 400, 200], [300, 243, 432, 334, 555], [999, 111, 0, 999, 333], [888, 777, 222, 333, 900], [100, 200, 300, 400, 500]]

# dr=[0,1,0,-1] #left,down,right,up
# dc=[-1,0,1,0]

# # x+(dr,dc)
# move=[[(-2,-1,2),  (-1,-2,10),(-1,-1,7),(-1,0,1),  
#         (0,-3,5), 
#         (1,-2,10),(1,-1,7),(1,0,1),  (2,-1,2)],
        
#         [(0,-1,1),(0,1,1),
#         (1,-2,2),(1,-1,7),(1,1,7),(1,2,2),
#         (2,-1,10),(2,1,10),
#         (3,0,5)],

#         [(-2,1,2),
#         (-1,0,1),(-1,1,7),(-1,2,10),
#         (0,3,5),
#         (1,0,1),(1,1,7),(1,2,10),
#         (2,1,2)],
        
#         [(-3,0,5),
#         (-2,-1,10),(-2,1,10),
#         (-1,-2,2),(-1,-1,7),(-1,1,7),(-1,2,2),
#         (0,-1,1),(0,1,1)]
#         ]

# moveAlpha=[(0,-2),(2,0),(0,2),(-2,0)]

# # N=10
# # a,b=5,5
# # for k in range(4):
# #     arr=[[0]*N for _ in range(N)]
# #     for r,c,v in move[k]:
# #         arr[a+r][b+c]=v

# #     for i in range(N):
# #         print(arr[i])



# visited=[[0]*N for _ in range(N)]
# r,c=int(N/2),int(N/2) #tornado
# visited[r][c]=1
# direc=0

# answer=0
# while (r!=0 or c!=0):
#     nr,nc=r+dr[direc],c+dc[direc]
#     # print(r,c,"=>",nr,nc)

#     y=arr[nr][nc] # sand
#     arr[nr][nc]=0 # all sand moved
#     notmovesand=y
#     for ddr,ddc,percent in move[direc]:
#         if r+ddr<0 or r+ddr>=N or c+ddc<0 or c+ddc>=N:
#             answer+=int(y*percent/100)
#             notmovesand-=int(y*percent/100)
#             continue
#         arr[r+ddr][c+ddc]+=int(y*percent/100)
#         notmovesand-=int(y*percent/100)
    
#     # position alpha
#     ar,ac=r+moveAlpha[direc][0], c+moveAlpha[direc][1]
#     if 0<=ar<N and 0<=ac<N:
#         arr[ar][ac]+=notmovesand
#     else:
#         answer+=notmovesand


#     if visited[nr+dr[(direc+1)%4]][nc+dc[(direc+1)%4]]==0:
#         direc=(direc+1)%4
#     r,c=nr,nc
#     visited[r][c]=1

# print(answer)
# # print(idx,ne)