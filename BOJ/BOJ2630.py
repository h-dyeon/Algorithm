import sys
# N=8
# matrix=[[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]
# N=8
# matrix=[[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1]]
# N=4
# matrix=[[1,1,1,1],[1,1,1,1],[0,0,0,1],[0,0,0,1]]

def quadTree(r, c, size):
    if size==1:
        color[matrix[r][c]]+=1
    else :
        tmp=0
        for i in range(size):
            tmp+=sum(matrix[r+i][c:c+size])
        if tmp/(size*size) == 1:
            color[1]+=1
        elif tmp/(size*size) ==0:
            color[0]+=1
        else :
            half=int(size/2)
            quadTree(r,c,half)
            quadTree(r,c+half,half)
            quadTree(r+half,c,half)
            quadTree(r+half,c+half,half)
        

N=int(sys.stdin.readline().strip())
matrix=[list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N)]
color=[0, 0] #white, blue
quadTree(0,0,N)
print(color[0])
print(color[1])
