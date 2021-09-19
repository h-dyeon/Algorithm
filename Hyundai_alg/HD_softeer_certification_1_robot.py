import sys
from collections import deque

H,W = map(int,sys.stdin.readline().strip().split(' '))
matrix=[list(sys.stdin.readline().strip()) for _ in range(H)]

# H=9
# W=14
# matrix=[['.', '.', '.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'], ['.', '#', '#', '#', '#', '#', '.', '.', '.', '#', '#', '#', '.', '.'], ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.'], ['.', '#', '.', '#', '#', '#', '#', '#', '.', '.', '.', '#', '#', '#'], ['.', '#', '.', '#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#'], ['.', '#', '#', '#', '.', '#', '#', '#', '.', '.', '.', '.', '.', '#'], ['.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '#'], ['.', '.', '.', '.', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#']] 

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

                
R,C=start_dq.popleft()

first_dir=-1
for k in range(4):
    if 0<=R+dr[k]<H and 0<=C+dc[k]<W and matrix[R+dr[k]][C+dc[k]]=='#':
        first_dir=k
        break

mstr=''
dq=deque([[first_dir,R,C]]) #now direction, row, col
while dq:
    d,r,c=dq.popleft()
    # print(d,r,c)
    if 0<=r+dr[d]<H and 0<=c+dc[d]<W and matrix[r+dr[d]][c+dc[d]]=='#':
        matrix[r+dr[d]][c+dc[d]]=1
        matrix[r+2*dr[d]][c+2*dc[d]]=1
        mstr+='A'
        dq.append([d,r+2*dr[d],c+2*dc[d]])
    elif 0<=r+dr[(d+1)%4]<H and 0<=c+dc[(d+1)%4]<W and matrix[r+dr[(d+1)%4]][c+dc[(d+1)%4]]=='#':
        mstr+='L'
        dq.append([(d+1)%4,r,c])
    elif 0<=r+dr[(d-1)%4]<H and 0<=c+dc[(d-1)%4]<W and matrix[r+dr[(d-1)%4]][c+dc[(d-1)%4]]=='#':
        mstr+='R'
        dq.append([(d-1)%4,r,c])

print(R+1,C+1)
print(dir_to_char[first_dir])
print(mstr)



###############################################
###############################################
# # 로봇이 지나간 경로 (not solved)
# dfs 관련 코드

# from sys import stdin
# import sys
# from collections import deque

# INF=99999999
# H,W = map(int, stdin.readline().strip().split(' ')) 
# mapinfo = [list(sys.stdin.readline().strip()) for _ in range(H)]
# needtogo=0
# for i in range(H):
#     for j in range(W):
#         if mapinfo[i][j]=='#':
#             needtogo+=1

# command=[1,-1,0] #L,R,A
# dr=[0,1,0,-1]
# dc=[-1,0,1,0]


# answer=(-1,-1,-1,'')
# answercount=INF

# def dfs(r, c,direc,strr,visited,count):
#     if count==needtogo:
#         return 
#     # left
#     ll=(direc+1)%4
#     if visited[r][c][ll]!=1:
#         visited[r][c][ll]=1
#         dfs(r,c,ll,strr+'L',visited,count)        
#     # right
#     rr=(direc+3)%4
#     if visited[r][c][rr]!=1:
#         visited[r][c][rr]=1
#         dfs(r,c,rr,strr+'R',visited,count)
#     # go straight
#     newR=[r+dr[direc],r+dr[direc]*2]
#     newC=[c+dc[direc],c+dc[direc]*2]
#     status=1
#     for i in range(2):
#         if 0>newR[i] or newR[i]>=H or 0>newC[i] or newC[i]>=W :
#             status=0
#             break
#         if sum(visited[newR[i]][newC[i]])!=4:
#             status=0
#             break
#     if status==1:
#         visited[newR[0]][newC[0]]=[1,1,1,1]
#         visited[newR[1]][newC[1]]=[1,1,1,1]
#         dfs(newR[1],newC[1],direc,strr+'A',visited,count+2)



# for i in range(H):
#     for j in range(W):
#         print(i,j)
#         for k in range(3):
#             visited=[[[0]*W for _ in range(H)] for _ in range(4)] # r,c,4 direction
#             visited[R][C][k]=1
#             dfs(i,j,k,'',visited)

            
#         if answercount>len(tmpanswer):
#             answer=(R,C,direc,tmpanswer)
#             answercount=len(tmpanswer)

# printdirec=['<','v','>','^']