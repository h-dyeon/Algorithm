
###############################################22.04.17
N=int(input())
arr=[list(map(int,input().split(' '))) for _ in range(N)]
answer=max([max(row) for row in arr])


def dfs(cnt,arr):
    global answer
    if cnt==5:
        answer=max(answer,max([max(row) for row in arr]))
        return

    # up
    narr=[[0]*N for _ in range(N)]
    status=False
    for c in range(N):
        i,j,val=0,0,0
        while j!=N:
            if arr[j][c]==0:
                j+=1
                continue
            if arr[j][c]!=val:
                narr[i][c]=arr[j][c]
                val=arr[j][c]
                i+=1
            elif arr[j][c]==val:
                narr[i-1][c]=arr[j][c]*2
                val=0
            j+=1
        if i!=j and i!=0:
            status=True
    if status:
        dfs(cnt+1, narr)

    # down
    narr=[[0]*N for _ in range(N)]
    status=False
    for c in range(N):
        i,j,val=N-1,N-1,0
        while j!=-1:
            if arr[j][c]==0:
                j-=1
                continue
            if arr[j][c]!=val:
                narr[i][c]=arr[j][c]
                val=arr[j][c]
                i-=1
            elif arr[j][c]==val:
                narr[i+1][c]=arr[j][c]*2
                val=0
            j-=1
        if i!=j and i!=N-1:
            status=True
    if status:
        dfs(cnt+1, narr)

    # right
    narr=[[0]*N for _ in range(N)]
    status=False
    for r in range(N):
        i,j,val=N-1,N-1,0
        while j!=-1:
            if arr[r][j]==0:
                j-=1
                continue
            if arr[r][j]!=val:
                narr[r][i]=arr[r][j]
                val=arr[r][j]
                i-=1
            elif arr[r][j]==val:
                narr[r][i+1]=arr[r][j]*2
                val=0
            j-=1
        if i!=j and i!=N-1:
            status=True
    if status:
        dfs(cnt+1, narr)
    
    #right
    narr=[[0]*N for _ in range(N)]
    status=False
    for r in range(N):
        i,j,val=0,0,0
        while j!=N:
            if arr[r][j]==0:
                j+=1
                continue
            if arr[r][j]!=val:
                narr[r][i]=arr[r][j]
                val=arr[r][j]
                i+=1
            elif arr[r][j]==val:
                narr[r][i-1]=arr[r][j]*2
                val=0
            j+=1
        if i!=j and i!=0:
            status=True
    if status:
        dfs(cnt+1, narr)


dfs(0,arr)
print(answer)
















###############################################
# import sys
# from pprint import pprint

# # N=int(input())
# # arr=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]
# # print(arr)
# N=3
# arr=[[256, 256, 128], [32, 16, 128], [128, 128, 128]]

# # N=4
# # arr=[[8,0,2,8],[4,0,2,2],[4,0,0,0],[16,0,0,0]]

# # N=3
# # arr=[[2, 2, 2], [4, 4, 4], [8, 8, 8]]

# def move(matrix,direction):
#     newMatrix=[[0]*N for _ in range(N)]
#     if direction==0: # up 
#         for c in range(N):
#             status=-1
#             tmpIdx=0
#             for r in range(N):
#                 if matrix[r][c]==0: continue
#                 if status==-1:
#                     newMatrix[tmpIdx][c]+=matrix[r][c]
#                     status=matrix[r][c]
#                 else:
#                     if status==matrix[r][c]:
#                         newMatrix[tmpIdx][c]+=matrix[r][c]
#                         tmpIdx+=1
#                         status=-1
#                     else:
#                         tmpIdx+=1
#                         newMatrix[tmpIdx][c]+=matrix[r][c]
#                         status=matrix[r][c]
#     if direction==1: # down
#         for c in range(N):
#             status=-1
#             tmpIdx=N-1 # start position
#             for r in range(N-1,-1,-1):
#                 if matrix[r][c]==0: continue
#                 if status==-1:
#                     newMatrix[tmpIdx][c]+=matrix[r][c]
#                     status=matrix[r][c]
#                 else:
#                     if status==matrix[r][c]:
#                         newMatrix[tmpIdx][c]+=matrix[r][c]
#                         tmpIdx-=1
#                         status=-1
#                     else:
#                         tmpIdx-=1
#                         newMatrix[tmpIdx][c]+=matrix[r][c]
#                         status=matrix[r][c]
#     elif direction==2: # ->
#         for r in range(N):
#             status=-1
#             tmpIdx=0
#             for c in range(N):
#                 if matrix[r][c]==0: continue
#                 if status==-1:
#                     newMatrix[r][tmpIdx]+=matrix[r][c]
#                     status=matrix[r][c]
#                 else:
#                     if status==matrix[r][c]:
#                         newMatrix[r][tmpIdx]+=matrix[r][c]
#                         tmpIdx+=1
#                         status=-1
#                     else:
#                         tmpIdx+=1
#                         newMatrix[r][tmpIdx]+=matrix[r][c]
#                         status=matrix[r][c]
#     elif direction==3: # -> & <-
#         for r in range(N):
#             status=-1
#             tmpIdx=N-1 # start position
#             for c in range(N-1,-1,-1):
#                 if matrix[r][c]==0: continue
#                 if status==-1:
#                     newMatrix[r][tmpIdx]+=matrix[r][c]
#                     status=matrix[r][c]
#                 else:
#                     if status==matrix[r][c]:
#                         newMatrix[r][tmpIdx]+=matrix[r][c]
#                         tmpIdx-=1
#                         status=-1
#                     else:
#                         tmpIdx-=1
#                         newMatrix[r][tmpIdx]+=matrix[r][c]
#                         status=matrix[r][c]
#     maxx=0
#     change=False
#     for i in range(N):
#         for j in range(N):
#             if newMatrix[i][j]!=matrix[i][j]:
#                 change=True
#             maxx=max(maxx,newMatrix[i][j])
#     return newMatrix, change,maxx

# def dfs(matrix,cnt,nowmax):
#     if cnt>=5:
#         return nowmax
#     answer=nowmax
#     for k in range(4):
#         newmatrix,change,maxx=move(matrix,k)
#         # print(change,maxx,cnt,"-----------",k)
#         # print(*newmatrix, sep='\n')
#         if change:
#             answer=max(answer,dfs(newmatrix,cnt+1,maxx))
#     return answer

# nowmax=0
# for i in range(N):
#     for j in range(N):
#         nowmax=max(nowmax,arr[i][j])
# print(dfs(arr,0,nowmax))