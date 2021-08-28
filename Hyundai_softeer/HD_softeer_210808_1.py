import sys
from collections import deque

N=int(sys.stdin.readline().strip())
origin=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(3*N)]

#transpose
matrix=[[0]*3*N for _ in range(N)]
for i in range(N*3):
    for j in range(N):
        matrix[j][i] = origin[3*N-i-1][j]

# print(origin)
# print(matrix)

# N=3
# origin=[[8, 5, 1], [9, 6, 1], [10, 7, 1], [11, 1, 3], [12, 1, 3], [13, 1, 3], [1, 2, 2], [1, 2, 2], [1, 2, 2]]
# matrix=[[1, 1, 1, 13, 12, 11, 10, 9, 8], 
#         [2, 2, 2, 1, 1, 1, 7, 6, 5], 
#         [2, 2, 2, 3, 3, 3, 1,1, 1]]
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def findSameCar(r,c,nowPos):
    colorNum= matrix[r][nowPos[r][c]]
    dCar=deque([[r,c]])
    dq=deque([[r,c]])
    rmax=r;rmin=r;cmax=c;cmin=c;
    while len(dq)!=0:
        tr,tc=dq.popleft()
        for i in range(4):
            newR=tr+dr[i]
            newC=tc+dc[i]
            if 0<=newR<N and 0<=newC<N and matrix[newR][nowPos[newR][newC]]==colorNum and [newR,newC] not in dCar:
                rmax=max(rmax,newR)
                rmin=min(rmin,newR)
                cmax=max(cmax,newC)
                cmin=min(cmin,newC)
                dq.append([newR,newC])
                dCar.append([newR,newC])
    return len(dCar),dCar, (rmax-rmin+1)*(cmax-cmin+1)

def makeNewMatrix(dCar,beforeM):
    newM=[deque(beforeM[i]) for i in range(N)]
    tmp=[max(beforeM[i])+1 for i in range(N)]
    while len(dCar)!=0:
        r,c=dCar.popleft()
        newM[r].remove(beforeM[r][c])
        newM[r].append(tmp[r])
        tmp[r]+=1
    return newM



def findanswer(turn,nowPos):
    if turn==0:
        return 0
    answer=0
    visit=[[0]*N]*N
    for i in range(N):
        for j in range(N):
            if visit[i][j]==0:
                dcarsize,deletcarlist,rectsize=findSameCar(i,j,nowPos) # position, color
                newPos=makeNewMatrix(deletcarlist,nowPos)
                answer=max(answer,dcarsize+rectsize+findanswer(turn-1,newPos))
                for r,c in deletcarlist:
                    visit[r][c]=1
    return answer

tmp=[list(range(N))]*N
print(findanswer(3,tmp))
