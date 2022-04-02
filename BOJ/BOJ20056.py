# # https://www.acmicpc.net/source/35255994
# import sys
# input = sys.stdin.readline
# N,M,K = map(int,input().split())

# def process(N,M,K):
#     fireballs = [list(map(int, input().split())) for _ in range(M)]
#     fireballs = list(map(lambda x: [x[0]-1,x[1]-1,*x[2:]],fireballs))
#     dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

#     for _ in range(K):
#         poses = {}
#         for r,c,m,s,d in fireballs:
#             nr,nc = (r+(dir[d][0]*s))%N,(c+(dir[d][1]*s))%N
#             poses.setdefault((nr,nc),[]).append([m,s,d])

#         temp = []
#         for (r,c), vals in poses.items():
#             if len(vals) == 1:
#                 temp.append([r,c,*vals[0]])
#                 continue
#             nm, ns, nd = 0,0,[]
#             for m,s,d in vals:
#                 nm += m
#                 ns += s
#                 nd.append(d%2)
#             nm = nm // 5
#             if nm == 0:
#                 continue
#             ns = ns // len(vals)
#             nd = [0,2,4,6] if all(d == nd[0] for d in nd) else [1,3,5,7]
#             for d in nd:
#                 temp.append([r,c,nm,ns,d])

#         fireballs = temp

#     return sum(map(lambda x: x[2] ,fireballs))

# print(process(N,M,K))

# ############## my code #################3
import sys
from collections import deque

dr=[-1,-1,0,1,1,1,0,-1]
dc=[0,1,1,1,0,-1,-1,-1]
fires={}

N,M,K=map(int, input().split(' '))
for _ in range(M):
    r,c,m,s,d=map(int, input().split(' '))
    fires[(r-1,c-1)]=deque([(m,s,d)])

for _ in range(K):
    # step 1
    nfires={}
    for r,c in fires.keys():
        dq=fires[(r,c)]
        for i in range(len(dq)):
            m,s,d=dq[i]
            print(m,s,d)
            nr=(r+s*dr[d]+1000*N)%N
            nc=(c+s*dc[d]+1000*N)%N
            if (nr,nc) in nfires:
                nfires[(nr,nc)].append((m,s,d))
            else:
                nfires[(nr,nc)]=deque([(m,s,d)])
    fires=nfires

    # #step 2
    nfires={}
    for r,c in fires.keys():
        dq=fires[(r,c)]
        if len(dq)==1:
            if (r,c) in nfires:
                nfires[(r,c)].append(dq[0])
            else:
                nfires[(r,c)]=dq
        else:
            sumS=0
            sumM=0
            direc=[0,0] # 짝,홀
            for i in range(len(dq)):
                m,s,d=dq[i]
                sumS+=s
                sumM+=m
                direc[d%2]+=1
            
            sumM=int(sumM/5)
            sumS=int(sumS/len(dq))
            newD=0 if direc[0]==len(dq) or direc[1]==len(dq) else 1

            if sumM==0: # disappear
                continue
            
            if (r,c) not in nfires:
                nfires[(r,c)]=deque([])
            for j in range(4):
                nfires[(r,c)].append((sumM,sumS,2*j+newD))
    fires=nfires


answer=0
for r,c in fires.keys():
    dq=fires[(r,c)]
    for i in range(len(dq)):
        answer+=dq[i][0]
print(answer)























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


            