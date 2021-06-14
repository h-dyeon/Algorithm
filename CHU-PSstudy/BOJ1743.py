from sys import stdin
import sys

N,M,K = map(int, stdin.readline().strip().split(' ')) #row, coulmn, submerged cell
mapinfo = [list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(K)]

dr=[0,-1,0,1]
dc=[1,0,-1,0]

maxx=0
while mapinfo:
    now=mapinfo.pop()
    value=1
    queue=[now]
    while queue:
        tmp=queue.pop()
        for i in range(4):
            newR=tmp[0]+dr[i]
            newC=tmp[1]+dc[i]
            if [newR,newC] in mapinfo:
                mapinfo.remove([newR,newC])
                queue.append([newR,newC])
                value+=1
    maxx=max(maxx,value)

print(maxx)
