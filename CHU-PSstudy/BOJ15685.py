import sys
from collections import deque

dx=[1,0,-1,0]
dy=[0,-1,0,1]
points={i:set([]) for i in range(101)}

def savecurves(x,y,d,g):
    dq=deque([[x,y]])
    dq.append([x+dx[d],y+dy[d]])
    for i in range(g):
        px,py=dq[len(dq)-1]
        for j in range(len(dq)-2,-1,-1):
            tx,ty=dq[j]
            dq.append([-(ty-py)+px,tx-px+py])
        #     print("t=(",tx,",",ty,") new=(",-(ty-py)+px,",",tx-px+py,")")
        # print("===================")
    while dq:
        x,y=dq.popleft()
        if 0<=x<=100 and 0<=y<=100:
            points[x].add(y)

N=int(sys.stdin.readline().strip())
for _ in range(N):
    x,y,d,g=map(int,sys.stdin.readline().strip().split(' '))
    savecurves(x,y,d,g)

answer=0
for i in range(100):
    for j in range(100):
        if points[i] and (j in points[i]):
            if points[i+1] and (j in points[i+1]) \
                and points[i] and (j+1 in points[i]) \
                and points[i+1] and (j+1 in points[i+1]):
                    answer+=1
print(answer)
