import sys
from collections import deque

dr=[-1,-1,0,1,1,1,0,-1]
dc=[0,1,1,1,0,-1,-1,-1]


N,M,K=map(int, sys.stdin.readline().strip().split(' '))
matrix=[list([deque([]),0,0,-2,0] for _ in range(N)) for _ in range(N)]
# deque, sum of m, sum of s, check d, fireball Count




















# import sys
# from collections import deque

# dr=[-1,-1,0,1,1,1,0,-1]
# dc=[0,1,1,1,0,-1,-1,-1]


# N,M,K=map(int, sys.stdin.readline().strip().split(' '))
# matrix=[list([deque([]),0,0,-2,0] for _ in range(N)) for _ in range(N)]
# # deque, sum of m, sum of s, check d, fireball Count

# for _ in range(M):
#     r,c,m,s,d=map(int, sys.stdin.readline().strip().split(' '))
#     matrix[r-1][c-1][0].append([m,s,d])

# for _ in range(K):
#     # move fireball
#     for i in range(N):
#         for j in range(N):
#             while matrix[i][j][0]:
#                 m,s,d=matrix[i][j][0].popleft()
#                 newr=i+dr[d]*s
#                 newc=j+dc[d]*s
#                 matrix[newr%N][newc%N][1]+=m # m
#                 matrix[newr%N][newc%N][2]+=s # s
#                 if matrix[newr%N][newc%N][3]==-2:  # direction
#                     matrix[newr%N][newc%N][3]=d
#                 elif matrix[newr%N][newc%N][3]%2 != d%2 :
#                     matrix[newr%N][newc%N][3]=-1
#                 matrix[newr%N][newc%N][4]+=1 # count
#     #merge fireball
#     for i in range(N):
#         for j in range(N):
#             if matrix[i][j][4]>=1:
#                 m=matrix[i][j][1]
#                 s=matrix[i][j][2]
#                 d=matrix[i][j][3]
#                 cnt=matrix[i][j][4]
#                 matrix[i][j]=[deque([]),0,0,-2,0]
#                 if cnt==1:
#                     matrix[i][j][0].append([m,s,d])
#                 else:
#                     if m>=5:
#                         for k in range(4):
#                             matrix[i][j][0].append([int(m/5),int(s/cnt),2*k+d%2])


# answer=0
# for i in range(N):
#     for j in range(N):
#         for k in range(len(matrix[i][j][0])):
#             answer+=matrix[i][j][0][k][0]

# print(answer)


            