import sys
import copy

def rotate(mat,r,c,s):
    tmp=copy.deepcopy(mat)
    for i in range(1,s+1):
        lt=tmp[r-i][c-i]
        rb=tmp[r+i][c+i]
        for j in range(-1*i,i):
            tmp[r+j][c-i]=tmp[r+j+1][c-i]
            tmp[r+j*(-1)][c+i]=tmp[r+j*(-1)-1][c+i]
        for j in range(-1*i,i):
            tmp[r+i][c+j]=tmp[r+i][c+j+1]
            tmp[r-i][c+j*(-1)]=tmp[r-i][c+j*(-1)-1]
        tmp[r-i][c-i+1]=lt
        tmp[r+i][c+i-1]=rb
    return tmp

def calc(mat):
    answer=1000000
    for i in range(N):
        answer=min(answer,sum(mat[i]))
    return answer

def dfs(mat,visited):
    ans=999999999
    for i in range(K):
        if visited & (1<<i) == 0:
            tmp=rotate(mat,rot[i][0]-1,rot[i][1]-1,rot[i][2])
            visited|=(1<<i)
            if visited !=(2<<K-1)-1:
                h=dfs(tmp,visited)
                ans=min(ans,h)
            else:
                return calc(tmp)
            visited &=(0<<i)
    return ans

N,M,K=map(int,sys.stdin.readline().strip().split(' '))
matrix=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]
rot=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(K)]

print(dfs(matrix,0))