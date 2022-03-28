# 22.03.28 new
from collections import deque

dr=[0,-1,0,1]
dc=[1,0,-1,0]
N=int(input())
info=[list(map(int,input().split(' '))) for _ in range(N)]
print(info)
# N=3
# info=[[3, 3, 0, 1], [4, 2, 1, 3], [4, 2, 2, 1]]

arr=[[0]*101 for _ in range(101)]



def checkSquare():
    answer=0
    for r in range(100):
        for c in range(100):
            if arr[r][c]+arr[r][c+1]+arr[r+1][c]+arr[r+1][c+1]==4:
                answer+=1
    return answer

def drawCurve(dq,g):
    if g==0:
        for i in range(len(dq)):
            r,c=dq[i]
            arr[r][c]=1
        return
    pr,pc=dq[-1] #point
    start=len(dq)-1
    for i in range(start-1,-1,-1):
        r,c=dq[i]
        nr=(c-pc)+pr
        nc=-1*(r-pr)+pc
        dq.append((nr,nc))
    drawCurve(dq,g-1)


for i in range(len(info)):
    c,r,d,g=info[i][0],info[i][1],info[i][2],info[i][3]
    nc,nr=c+dc[d],r+dr[d]
    drawCurve(deque([(r,c),(nr,nc)]),g)
print(checkSquare())




















# import sys
# from collections import deque

# dx=[1,0,-1,0]
# dy=[0,-1,0,1]
# points={i:set([]) for i in range(101)}

# def savecurves(x,y,d,g):
#     dq=deque([[x,y]])
#     dq.append([x+dx[d],y+dy[d]])
#     for i in range(g):
#         px,py=dq[len(dq)-1]
#         for j in range(len(dq)-2,-1,-1):
#             tx,ty=dq[j]
#             dq.append([-(ty-py)+px,tx-px+py])
#         #     print("t=(",tx,",",ty,") new=(",-(ty-py)+px,",",tx-px+py,")")
#         # print("===================")
#     while dq:
#         x,y=dq.popleft()
#         if 0<=x<=100 and 0<=y<=100:
#             points[x].add(y)

# N=int(sys.stdin.readline().strip())
# for _ in range(N):
#     x,y,d,g=map(int,sys.stdin.readline().strip().split(' '))
#     savecurves(x,y,d,g)

# answer=0
# for i in range(100):
#     for j in range(100):
#         if points[i] and (j in points[i]):
#             if points[i+1] and (j in points[i+1]) \
#                 and points[i] and (j+1 in points[i]) \
#                 and points[i+1] and (j+1 in points[i+1]):
#                     answer+=1
# print(answer)
