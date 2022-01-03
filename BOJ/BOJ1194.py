from sys import stdin
import sys
from collections import deque

dr=[1,-1,0,0]
dc=[0,0,+1,-1]
INF=9999999999
minValue=INF


def BFS(start_r,start_c):
    cnt=[[[0]*64 for _ in range(M)] for _ in range(N)]
    cnt[start_r][start_c][0]=1 # step count
    dq=deque([[start_r,start_c,0]]) # row, col, key

    while len(dq)!=0: 
        r,c,keys=dq.popleft()
        #print(r,c,maze[r][c],bin(keys))
        if maze[r][c]=='1':
            print(cnt[r][c][keys]-1)
            return

        for i in range(4):
            R=r+dr[i]
            C=c+dc[i]
            if 0<=R<N and 0<=C<M:
                char=maze[R][C]
                if char=='#' or cnt[R][C][keys]!=0:
                    continue
                
                char_bit=ord(char)
                if char.islower(): # lower alphabet
                    newkeys = keys | (1<<(char_bit-97))
                    if cnt[R][C][newkeys]==0:
                        cnt[R][C][newkeys]=cnt[r][c][keys]+1
                        dq.append([R,C,newkeys])

                elif char.isupper(): # upper alphabet
                    if (keys & (1<<(char_bit-65))) != 0 :
                        cnt[R][C][keys]=cnt[r][c][keys]+1
                        dq.append([R,C,keys])
                else :
                    cnt[R][C][keys]=cnt[r][c][keys]+1
                    dq.append([R,C,keys])

    print(-1)

###################################### 
N, M = list(map(int, stdin.readline().strip().split(' ')))
start=[0,0]
maze=[]
for i in range(0,N):
    line=stdin.readline().strip()
    maze.append(line)
    if line.find('0') != -1:
        start=[i,line.find('0')]

BFS(start[0],start[1]) 
