########## 22.04.06 ############
arr=[[0]*4 for _ in range(4)]
fishes=[[0]*3 for _ in range(17)]
for i in range(4):
    tmp=list(map(int,input().split(' ')))
    for j in range(4):
        f,d=tmp[2*j],tmp[2*j+1]
        arr[i][j]=f
        fishes[f]=[i,j,d]

print(arr)
print(fishes)

# arr=[[7, 2, 15, 9], [3, 1, 14, 10], [6, 13, 4, 11], [16, 8, 5, 12]]
# fishes=[[0, 0, 0], [1, 1, 8], [0, 1, 3], [1, 0, 1], [2, 2, 3], [3, 2, 2], [2, 0, 1], [0, 0, 6], [3, 1, 7], [0, 3, 8], [1, 3, 1], [2, 3, 4], [3, 3, 2], [2, 1, 6], [1, 2, 7], [0, 2, 6], [3, 0, 1]]
answer=0
dr=[-1,-1,-1,0,1,1,1,0,-1]
dc=[1,0,-1,-1,-1,0,1,1,1]


def dfs(sum,matrix,nfish):
    global answer

    # move fish
    for f in range(1,17):
        r,c,d=nfish[f]
        if d==-1:
            continue
        for k in range(0,8):
            nr,nc=r+dr[(d+k)%8],c+dc[(d+k)%8]
            if 0<=nr<4 and 0<=nc<4 and matrix[nr][nc]!=-1: #not shark
                if matrix[nr][nc]!=0: # is fish
                    afterf=matrix[nr][nc]

                    nfish[afterf]=[r,c,nfish[afterf][2]]
                    nfish[f]=[nr,nc,(d+k)%8]

                    matrix[nr][nc]=f
                    matrix[r][c]=afterf
                else: #blank
                    nfish[f]=[nr,nc,(d+k)%8]
                    matrix[r][c]=0
                    matrix[nr][nc]=f
                break
    # move shark
    status=True
    for k in range(1,4):
        r,c,d=nfish[0]
        nr,nc=r+k*dr[d],c+k*dc[d]
        if 0<=nr<4 and 0<=nc<4 and matrix[nr][nc]>0: # is fish
            status=False
            fidx=matrix[nr][nc]

            nmatrix=[row[:] for row in matrix]
            nnfish=[row[:] for row in nfish]

            nmatrix[r][c]=0
            nmatrix[nr][nc]=-1

            nnfish[0]=nnfish[fidx]#move shark
            nnfish[fidx]=[-1,-1,-1]
            dfs(sum+fidx,nmatrix,nnfish)
    if status:
        answer=max(answer,sum)
    return






firstFish=arr[0][0]
fishes[0]=fishes[firstFish] # shark eat fish
fishes[firstFish]=[-1,-1,-1]
arr[0][0]=-1 #shark
matrix=[row[:] for row in arr]
nfish=[row[:] for row in fishes]
dfs(firstFish,matrix,nfish)
print(answer)









############ 21.09~~?##############
# import sys
# import copy
# # x는 행
# # y는 열
# # 공간은 4*4

# # 번호 1~16
# # 물고기는 모두 다른 번호

# dr=[-1,-1,0,1,1,1,0,-1] # 1 indexing
# dc=[0,-1,-1,-1,0,1,1,1]


# # number=[[7, 2, 15, 9], [3, 1, 14, 10], [6, 13, 4, 11], [16, 8, 5, 12]]
# # # direc=[[6, 3, 6, 8], [1, 8, 7, 1], [1, 6, 3, 4], [1, 7, 2, 2]]
# # direc=[[5, 2, 5, 7], [0, 7, 6, 0], [0, 5, 2, 3], [0, 6, 1, 1]]

# def findpos(val,number):
#     for i in range(4):
#         for j in range(4):
#             if number[i][j]==val:
#                 return i,j
#     return -1,-1

  
# def func(number,direc,shark_r,shark_c):
#     # shark
    
#     nowshark=number[shark_r][shark_c]
#     answer=nowshark
#     number[shark_r][shark_c]=shark

#     # fish
#     for i in range(1,17):
#         r,c=findpos(i,number)
#         if r==-1:
#             continue
#         d=direc[r][c]
#         for j in range(8):
#             newr=r+dr[(d+j)%8]
#             newc=c+dc[(d+j)%8]
#             if 0<=newr<4 and 0<=newc<4 and blankfish<=number[newr][newc]<=16:
#                 if 1<=number[newr][newc]<=16:
#                     number[r][c]=number[newr][newc]
#                     direc[r][c]=direc[newr][newc]
#                 else:
#                     number[r][c]=blankfish
#                     direc[r][c]=-1
#                 number[newr][newc]=i
#                 direc[newr][newc]=(d+j)%8
#                 break
#     #shark
#     sr,sc=findpos(shark,number)
#     sd=direc[sr][sc]
#     for i in range(4):
#         newsr=sr+(i+1)*dr[sd]
#         newsc=sc+(i+1)*dc[sd]
#         if not(0<=newsr<4 and 0<=newsc<4):
#             break
#         elif 0<=newsr<4 and 0<=newsc<4 and 1<=number[newsr][newsc]<=16:
#             newnumber=copy.deepcopy(number)
#             newnumber[sr][sc]=blankfish
#             newdirec=copy.deepcopy(direc)
#             hey=func(newnumber,newdirec,newsr,newsc)
#             answer=max(answer,nowshark+hey)
#     return answer

# number=[[0] *4 for _ in range(4)]
# direc=[[0] *4 for _ in range(4)]
# for i in range(4):
#     tmp=list(map(int, sys.stdin.readline().strip().split(' ')))
#     for j in range(4):
#         number[i][j]=tmp[j*2]
#         direc[i][j]=tmp[j*2+1]-1

# # number=[[12, 14, 4, 6], [15, 11, 3, 7], [10, 8, 16, 1], [5, 2, 13, 9]]
# # direc=[[5, 4, 4, 6], [0, 6, 6, 4], [2, 2, 5, 0], [7, 6, 5, 1]]


# blankfish=0
# shark=100
# a=func(number,direc, 0,0)
# print(a)