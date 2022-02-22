import sys
N,M,K=map(int,sys.stdin.readline().strip().split(' '))
matrix=[sys.stdin.readline().strip() for _ in range(N)]
word=sys.stdin.readline().strip()

dr=[0,1,0,-1]
dc=[1,0,-1,0]
dp=[[[-1 for _ in range(len(word)+1)] for _ in range(M)] for _ in range(N)]
result=0

def dfs(r,c,idx):
    if dp[r][c][idx]!=-1:
        return dp[r][c][idx]
    if idx==len(word):
        dp[r][c][idx]=1
        return 1
    dp[r][c][idx]=0;
    for i in range(4):
        for k in range(1,K+1):
            nr=r+dr[i]*k
            nc=c+dc[i]*k
            if 0<=nr<N and 0<=nc<N and matrix[nr][nc]==word[idx]:
                dp[r][c][idx]+=dfs(nr,nc,idx+1)
    return dp[r][c][idx]

for i in range(N):
    for j in range(M):
        if word[0]==matrix[i][j]:
            result+=dfs(i,j,1)

print(result)




########3 time out ##############3
# import sys
# from collections import deque

# N,M,K=map(int,sys.stdin.readline().strip().split(' '))
# matrix=[sys.stdin.readline().strip() for _ in range(N)]
# word=sys.stdin.readline().strip()

# dx=[0,1,0,-1]
# dy=[1,0,-1,0]

# dq=deque([])
# for i in range(N):
#     for j in range(M):
#         if word[0]==matrix[i][j]:
#             dq.append([i,j,1])

# answer=0
# while dq:
#     [x,y,idx]=dq.popleft()
#     for i in range(4):
#         for k in range(1,K+1):
#             nx,ny=x+dx[i]*k, y+dy[i]*k
#             if 0<=nx<N and 0<=ny<N and matrix[nx][ny]==word[idx]:
#                 if idx==len(word)-1:
#                     answer+=1
#                 else:
#                     dq.append([nx,ny,idx+1])
# print(answer)