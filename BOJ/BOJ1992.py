# 20220209 again!

import sys
N=int(input())
arr=[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

def dq(sr,sc,l):
    tmp=0
    for i in range(l):
        tmp+=sum(arr[sr+i][sc:sc+l])
    if tmp==0: return "0"
    elif tmp==l*l: return "1"
    else:
        return ("("+dq(sr,sc,int(l/2))+
                    dq(sr,sc+int(l/2),int(l/2))+
                    dq(sr+int(l/2),sc,int(l/2))+
                    dq(sr+int(l/2),sc+int(l/2),int(l/2))+
                    ")")

print(dq(0,0,N))

















# import sys
# # N=8
# # matrix=[[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1]]
# # N=4
# # matrix=[[1,1,1,1],[1,1,1,1],[0,0,0,1],[0,0,0,1]]

# def quadTree(r, c, size):
#     if size==1:
#         return str(matrix[r][c])
    
#     tmp=0
#     for i in range(size):
#         tmp+=sum(matrix[r+i][c:c+size])
    
#     if tmp/(size*size) == 1:
#         return str(1)
#     elif tmp/(size*size) ==0:
#         return str(0)
#     else :
#         half=int(size/2)
#         return ("(" + quadTree(r,c,half) + 
#                     quadTree(r,c+half,half) + 
#                     quadTree(r+half,c,half) + 
#                     quadTree(r+half,c+half,half) + ")" )

# N=int(sys.stdin.readline().strip())
# matrix=[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
# print(quadTree(0,0,N))
