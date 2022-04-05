N,M=map(int,input().split(' '))
r,c,d=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]
print(arr)

direc=[[-1,0],[0,1],[1,0],[0,-1]]
answer=0
while True:
    # step 1
    if arr[r][c]==0:
        arr[r][c]=2 #clean
        answer+=1
    
    #step 2
    status=False
    for i in range(1,5):
        nr,nc=r+direc[(d-i+4)%4][0],c+direc[(d-i+4)%4][1]
        if arr[nr][nc]==0:
            r,c=nr,nc
            d=(d-i+4)%4
            status=True
            break
    if status:
        continue
    else:
        nr,nc=r+direc[(d+2)%4][0], c+direc[(d+2)%4][1]
        if arr[nr][nc]==1:
            break
        else:
            r,c=nr,nc

print(answer)


# import sys

# # N,M=list(map(int,sys.stdin.readline().strip().split(' ')))
# # r,c,d=list(map(int,sys.stdin.readline().strip().split(' ')))
# # arr=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]
# # print(arr)

# N,M=3,3
# r,c,d=1,1,0
# arr=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]

# # N,M=11,10
# # r,c,d=7,4,0
# # arr=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# dr=[-1,0,1,0]
# dc=[0,1,0,-1]

# answer=0
# status=True
# for _ in range(10000000):
#     if status: # number 1
#         answer+=1
#         arr[r][c]=2 #clean
#         status=False # goto number2
#     else: # number2
#         isCleaned=False
#         for i in range(1,5):
#             nd=(d+4-i)%4
#             nr,nc=r+dr[nd],c+dc[nd]
#             if 0<=nr<N and 0<=nc<M and arr[nr][nc]==0:
#                 r,c,d=nr,nc,nd
#                 isCleaned=True
#                 break
#         if isCleaned:
#             status=True # goto number1
#             continue
#         elif arr[r+dr[(d+4-2)%4]][c+dc[(d+4-2)%4]]!=1: #there is blocked 
#             r=r+dr[(d+4-2)%4]
#             c=c+dc[(d+4-2)%4]
#             continue
#         else:
#             break
# print(answer)




