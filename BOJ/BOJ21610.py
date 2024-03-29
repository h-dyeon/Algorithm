####################################################22.04.17
N,M=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]
move=[list(map(int,input().split(' '))) for _ in range(M)]

cloud=set([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])

direc=[(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

for i in range(M):
    tmpcloud=set()
    d,s=move[i]
    for r,c in cloud:
        nr,nc=(r+direc[d-1][0]*s)%N,(c+direc[d-1][1]*s)%N
        arr[nr][nc]+=1
        tmpcloud.add((nr,nc))

    narr=[row[:] for row in arr]
    for r,c in tmpcloud:
        cnt=0
        if r+1<N:
            if c+1<N and narr[r+1][c+1]>0: cnt+=1
            if c-1>=0 and narr[r+1][c-1]>0: cnt+=1
        if r-1>=0:
            if c+1<N and narr[r-1][c+1]>0: cnt+=1
            if c-1>=0 and narr[r-1][c-1]>0: cnt+=1
        arr[r][c]+=cnt

    cloud=set()
    for i in range(N):
        for j in range(N):
            if arr[i][j]>1 and (i,j) not in tmpcloud:
                cloud.add((i,j))
                arr[i][j]-=2

    #cloud=tmpcloud

print(sum([sum(r) for r in arr]))







###############################################################3
# N,M=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# move=[list(map(int,input().split(' '))) for _ in range(M)]
# # print(arr)
# # print(move)
# # N,M=5,4
# # arr=[[0, 0, 1, 0, 2], [2, 3, 2, 1, 0], [4, 3, 2, 9, 0], [1, 0, 2, 9, 0], [8, 8, 2, 1, 0]]
# # move=[[1, 3], [3, 4], [8, 1], [4, 8]]



# dr=[0,-1,-1,-1,0,1,1,1]
# dc=[-1,-1,0,1,1,1,0,-1]

# cloud={(N-1,0),(N-1,1),(N-2,0),(N-2,1)}

# for m in range(M):
#     direc=move[m][0]-1
#     s=move[m][1]

#     # step 1&2 move cloud and rain
#     for r,c in cloud:
#         nr,nc=(r+s*dr[direc])%N,(c+s*dc[direc])%N
#         arr[nr][nc]+=1
#         # arr[a][b]+=1
    
#     # step 4
#     for r,c in cloud:
#         nr,nc=(r+s*dr[direc])%N,(c+s*dc[direc])%N
#         cnt=0
#         for i in range(4):
#             nnr,nnc=nr+dr[i*2+1],nc+dc[i*2+1]
#             if 0<=nnr<N and 0<=nnc<N and arr[nnr][nnc]>0:
#                 cnt+=1
#         arr[nr][nc]+=cnt
    
#     # step 5
#     newcloud=set()
#     for r in range(N):
#         for c in range(N):
#             if arr[r][c]>=2:
#                 beforeR=(r+s*dr[(direc+4)%8])%N
#                 beforeC=(c+s*dc[(direc+4)%8])%N
#                 if (beforeR,beforeC) not in cloud:
#                     newcloud.add((r,c))
#                     arr[r][c]-=2
#     cloud=newcloud

# answer=sum([sum(row) for row in arr])
# print(answer)


