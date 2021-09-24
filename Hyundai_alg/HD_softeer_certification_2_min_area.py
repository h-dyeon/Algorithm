import sys
from collections import deque

# N, K = map(int,sys.stdin.readline().strip().split(' '))
# matrix=[]

# N=5
# K=3
#matrix=[[3, 7, 1], [5, 8, 1], [6, 5, 2], [7, 1, 3], [9, 3, 3]]

N=5
K=2
matrix=[[-4, -2, 1], [-5, -3, 1], [5, -4, 2], [4, -5, 2], [3, -8, 2]]

x_m=[[0]*2001 for i in range(K)]
y_m=[[0]*2001 for i in range(K)]

for i in range(N):
    # x,y,k=map(int,sys.stdin.readline().strip().split(' '))
    # matrix.append([x,y,k])
    x=matrix[i][0]
    y=matrix[i][1]
    k=matrix[i][2]
    x_m[k-1][x+1000]=1
    y_m[k-1][y+1000]=1
print(matrix)

minv=5000000
for i in range (N):
    for j in range(i,N):
        xs=[matrix[i][0]+1000,matrix[j][0]+1000]
        ys=[matrix[i][1]+1000,matrix[j][1]+1000]
        xs.sort()
        ys.sort()
        print("i=",i,matrix[i],"j=",j,matrix[j], "=====",xs,ys)
        status=1
        for m in range(K):
            print("\t",x_m[m][xs[0]:xs[1]+1],y_m[m][ys[0]:ys[1]+1])
            if sum(x_m[m][xs[0]:xs[1]+1])==0 and sum(y_m[m][ys[0]:ys[1]+1])==0:
                status=0
                break
        if status==1:
            minv=min(minv, (xs[1]-xs[0])*(ys[1]-ys[0]))

print(minv)

