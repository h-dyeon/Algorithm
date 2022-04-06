
##################################################22.04.06

N,M=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]

cctv=[]
for i in range(N):
    for j in range(M):
        if 1<=arr[i][j]<=5:
            cctv.append((i,j))

dr=[0,1,0,-1]
dc=[1,0,-1,0]
cctvDirec=[[],[[0],[1],[2],[3]],
        [[0,2],[1,3]],
        [[0,1],[1,2],[2,3],[3,0]],
        [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
        [[0,1,2,3]]]
answer=sum([r.count(0) for r in arr])

def check(matrix,d,r,c):
    while True:
        nr,nc=r+dr[d],c+dc[d]
        if 0>nr or 0>nc or N<=nr or M<=nc or matrix[nr][nc]==6:
            break
        matrix[nr][nc]=-1
        r,c=nr,nc
    return


def dfs(cnt,narr):
    global answer
    if cnt==len(cctv):
        answer=min(answer,sum([r.count(0) for r in narr]))
        return
    
    r,c=cctv[cnt]
    ttype=arr[r][c]
    directions=cctvDirec[ttype]
    for a in directions:
        matrix=[row[:] for row in narr]
        for b in a:
            check(matrix,b,r,c)
        dfs(cnt+1,matrix)

dfs(0,arr)
print(answer)





##################################################3
# import sys


# N,M=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# print(arr)

# # N,M=4,6
# # arr=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 6, 0], [0, 0, 0, 0, 0, 0]]
# dr=[1,0,-1,0]
# dc=[0,1,0,-1]
# answer=100000000000 #min

# #find cctv
# cctv=[]
# for i in range(N):
#     for j in range(M):
#         if 0<arr[i][j]<6:
#             cctv.append((i,j,arr[i][j]))

# def going(copyarr,direc,r,c):
#     for k in range(1,1000):
#         nr=r+k*dr[direc]
#         nc=c+k*dc[direc]
#         if 0<=nr<N and 0<=nc<M and copyarr[nr][nc]!=6:
#             copyarr[nr][nc]=99
#         else:
#             break
#     return copyarr


# def check(copyarr,idx):
#     global answer
#     tmp=sum([copyarr[i].count(0) for i in range(N)])
#     if tmp==0 or len(cctv)==idx:  
#         answer=min(answer,tmp)
#         return

#     r,c,t=cctv[idx]
    
#     if t==1:
#         for d in range(4):
#             narr=[r[:] for r in copyarr]
#             check(going(narr,d,r,c),idx+1)
#     elif t==2:
#         for i in range(2):
#             narr=[r[:] for r in copyarr]
#             going(narr,i,r,c)
#             going(narr,i+2,r,c)
#             check(narr,idx+1)
#     elif t==3:
#         for i in range(4):
#             narr=[r[:] for r in copyarr]
#             going(narr,i,r,c)
#             going(narr,(i+1)%4,r,c)
#             check(narr,idx+1)
#     elif t==4:
#         for i in range(4):
#             narr=[r[:] for r in copyarr]
#             going(narr,i,r,c)
#             going(narr,(i+1)%4,r,c)
#             going(narr,(i+2)%4,r,c)
#             check(narr,idx+1)
#     elif t==5:
#         narr=[r[:] for r in copyarr]
#         for d in range(4):
#             going(narr,d,r,c)
#         check(narr,idx+1)

# copyarr=[r[:] for r in arr]
# check(copyarr,0)
# print(answer)