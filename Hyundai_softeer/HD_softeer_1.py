# 차세대 지능형 교통시스템

from sys import stdin
import sys
from collections import deque

N,T = map(int, stdin.readline().strip().split(' ')) 

mapinfo = [list(list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)) for _ in range(N)]
visited=[[0]*N for _ in range(N)]

dr=[0,0,-1,0,1]
dc=[0,1,0,-1,0]

direc=[[1,[1,2,4]],
        [2,[1,2,3]],
        [3,[3,2,4]],
        [4,[1,3,4]],
        [1,[1,2]],
        [2,[2,3]],
        [3,[3,4]],
        [4,[4,1]],
        [1,[4,1]],
        [2,[1,2]],
        [3,[2,3]],
        [4,[3,4]]]


queue=deque([(0,0,0,mapinfo[0][0][0])]) # T, r, c, signal
visited[0][0]=1
count=1
while queue:
    t,r,c,signal=queue.popleft()
    newdirec=direc[signal-1][1] # 0 index
    for i in newdirec:
        newR=r+dr[i]
        newC=c+dc[i]

        if 0<=newR<N and 0<=newC<N :
            newsignal=mapinfo[newR][newC][(t+1)%4]
            newinputdirec=direc[newsignal-1][0]
            if i == newinputdirec and visited[newR][newC]!=1:
                if t+1!=T:
                    queue.append((t+1,newR,newC,newsignal))
                visited[newR][newC]=1
                count+=1

#print(visited)
print(count)



