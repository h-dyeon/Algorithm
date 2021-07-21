# 로봇이 지나간 경로 (not solved)

from sys import stdin
import sys
from collections import deque

INF=99999999
H,W = map(int, stdin.readline().strip().split(' ')) 
mapinfo = [list(sys.stdin.readline().strip()) for _ in range(H)]
needtogo=0
for i in range(H):
    for j in range(W):
        if mapinfo[i][j]=='#':
            needtogo+=1

command=[1,-1,0] #L,R,A
dr=[0,1,0,-1]
dc=[-1,0,1,0]


answer=(-1,-1,-1,'')
answercount=INF

def dfs(r, c,direc,strr,visited,count):
    if count==needtogo:
        return 
    # left
    ll=(direc+1)%4
    if visited[r][c][ll]!=1:
        visited[r][c][ll]=1
        dfs(r,c,ll,strr+'L',visited,count)        
    # right
    rr=(direc+3)%4
    if visited[r][c][rr]!=1:
        visited[r][c][rr]=1
        dfs(r,c,rr,strr+'R',visited,count)
    # go straight
    newR=[r+dr[direc],r+dr[direc]*2]
    newC=[c+dc[direc],c+dc[direc]*2]
    status=1
    for i in range(2):
        if 0>newR[i] or newR[i]>=H or 0>newC[i] or newC[i]>=W :
            status=0
            break
        if sum(visited[newR[i]][newC[i]])!=4:
            status=0
            break
    if status==1:
        visited[newR[0]][newC[0]]=[1,1,1,1]
        visited[newR[1]][newC[1]]=[1,1,1,1]
        dfs(newR[1],newC[1],direc,strr+'A',visited,count+2)



for i in range(H):
    for j in range(W):
        print(i,j)
        for k in range(3):
            visited=[[[0]*W for _ in range(H)] for _ in range(4)] # r,c,4 direction
            visited[R][C][k]=1
            dfs(i,j,k,'',visited)

            
        if answercount>len(tmpanswer):
            answer=(R,C,direc,tmpanswer)
            answercount=len(tmpanswer)

printdirec=['<','v','>','^']