import sys
from collections import deque

N,T=map(int, sys.stdin.readline().strip().split(' '))
ITSsignals=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N*N)]

# N=3
# T=3
# ITSsignals=[[2, 6, 12, 9], [7, 1, 11, 6], [6, 3, 5, 11], [1, 1, 12, 9], [3, 11, 8, 2], [1, 7, 11, 9], [4, 6, 2, 3], [2, 4, 2, 4], [6, 9, 2, 6]]

go_=[[1,0],[0,-1],[-1,0],[0,1]] # E,N,W,S

signal={1:[0,[1,0,3]],
        2:[1,[0,1,2]],
        3:[2,[1,2,3]],
        4:[3,[2,3,0]],
        5:[0,[0,1]],
        6:[1,[1,2]],
        7:[2,[2,3]],
        8:[3,[3,0]],
        9:[0,[0,3]],
        10:[1,[1,0]],
        11:[2,[2,1]],
        12:[3,[3,2]]}

dq=deque([(1,0,1,1)]) # input direction, T, r, c
visited = {(1-1)*N+1} # value= (row-1)*N+col
while dq:
    inputdir,t,r,c=dq.popleft()
    nowpos_signals=ITSsignals[(r-1)*N+c-1]
    now_S=signal[nowpos_signals[t%4]]
    if now_S[0]==inputdir:
        for i in now_S[1]:
            newC=c+go_[i][0]
            newR=r+go_[i][1]
            if 0<newR<=N and 0<newC<=N and ((newR-1)*N+newC) not in visited:
                visited.add((newR-1)*N+newC)
                if T>t+1:
                    dq.append([i,t+1,newR,newC])
print(len(visited))





############before############
# #차세대 지능형 교통시스템

# from sys import stdin
# import sys
# from collections import deque

# N,T = map(int, stdin.readline().strip().split(' ')) 

# mapinfo = [list(list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)) for _ in range(N)]
# visited=[[0]*N for _ in range(N)]

# dr=[0,0,-1,0,1]
# dc=[0,1,0,-1,0]

# direc=[[1,[1,2,4]],
#         [2,[1,2,3]],
#         [3,[3,2,4]],
#         [4,[1,3,4]],
#         [1,[1,2]],
#         [2,[2,3]],
#         [3,[3,4]],
#         [4,[4,1]],
#         [1,[4,1]],
#         [2,[1,2]],
#         [3,[2,3]],
#         [4,[3,4]]]


# queue=deque([(0,0,0,mapinfo[0][0][0])]) # T, r, c, signal
# visited[0][0]=1
# count=1
# while queue:
#     t,r,c,signal=queue.popleft()
#     newdirec=direc[signal-1][1] # 0 index
#     for i in newdirec:
#         newR=r+dr[i]
#         newC=c+dc[i]

#         if 0<=newR<N and 0<=newC<N :
#             newsignal=mapinfo[newR][newC][(t+1)%4]
#             newinputdirec=direc[newsignal-1][0]
#             if i == newinputdirec and visited[newR][newC]!=1:
#                 if t+1!=T:
#                     queue.append((t+1,newR,newC,newsignal))
#                 visited[newR][newC]=1
#                 count+=1

# #print(visited)
# print(count)



