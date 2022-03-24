import sys
from pprint import pprint

# N=int(input())
# arr=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]
# print(arr)
N=3
arr=[[256, 256, 128], [32, 16, 128], [128, 128, 128]]

# N=4
# arr=[[8,0,2,8],[4,0,2,2],[4,0,0,0],[16,0,0,0]]

# N=3
# arr=[[2, 2, 2], [4, 4, 4], [8, 8, 8]]

def move(matrix,direction):
    newMatrix=[[0]*N for _ in range(N)]
    if direction==0: # up 
        for c in range(N):
            status=-1
            tmpIdx=0
            for r in range(N):
                if matrix[r][c]==0: continue
                if status==-1:
                    newMatrix[tmpIdx][c]+=matrix[r][c]
                    status=matrix[r][c]
                else:
                    if status==matrix[r][c]:
                        newMatrix[tmpIdx][c]+=matrix[r][c]
                        tmpIdx+=1
                        status=-1
                    else:
                        tmpIdx+=1
                        newMatrix[tmpIdx][c]+=matrix[r][c]
                        status=matrix[r][c]
    if direction==1: # down
        for c in range(N):
            status=-1
            tmpIdx=N-1 # start position
            for r in range(N-1,-1,-1):
                if matrix[r][c]==0: continue
                if status==-1:
                    newMatrix[tmpIdx][c]+=matrix[r][c]
                    status=matrix[r][c]
                else:
                    if status==matrix[r][c]:
                        newMatrix[tmpIdx][c]+=matrix[r][c]
                        tmpIdx-=1
                        status=-1
                    else:
                        tmpIdx-=1
                        newMatrix[tmpIdx][c]+=matrix[r][c]
                        status=matrix[r][c]
    elif direction==2: # ->
        for r in range(N):
            status=-1
            tmpIdx=0
            for c in range(N):
                if matrix[r][c]==0: continue
                if status==-1:
                    newMatrix[r][tmpIdx]+=matrix[r][c]
                    status=matrix[r][c]
                else:
                    if status==matrix[r][c]:
                        newMatrix[r][tmpIdx]+=matrix[r][c]
                        tmpIdx+=1
                        status=-1
                    else:
                        tmpIdx+=1
                        newMatrix[r][tmpIdx]+=matrix[r][c]
                        status=matrix[r][c]
    elif direction==3: # -> & <-
        for r in range(N):
            status=-1
            tmpIdx=N-1 # start position
            for c in range(N-1,-1,-1):
                if matrix[r][c]==0: continue
                if status==-1:
                    newMatrix[r][tmpIdx]+=matrix[r][c]
                    status=matrix[r][c]
                else:
                    if status==matrix[r][c]:
                        newMatrix[r][tmpIdx]+=matrix[r][c]
                        tmpIdx-=1
                        status=-1
                    else:
                        tmpIdx-=1
                        newMatrix[r][tmpIdx]+=matrix[r][c]
                        status=matrix[r][c]
    maxx=0
    change=False
    for i in range(N):
        for j in range(N):
            if newMatrix[i][j]!=matrix[i][j]:
                change=True
            maxx=max(maxx,newMatrix[i][j])
    return newMatrix, change,maxx

def dfs(matrix,cnt,nowmax):
    if cnt>=5:
        return nowmax
    answer=nowmax
    for k in range(4):
        newmatrix,change,maxx=move(matrix,k)
        # print(change,maxx,cnt,"-----------",k)
        # print(*newmatrix, sep='\n')
        if change:
            answer=max(answer,dfs(newmatrix,cnt+1,maxx))
    return answer

nowmax=0
for i in range(N):
    for j in range(N):
        nowmax=max(nowmax,arr[i][j])
print(dfs(arr,0,nowmax))