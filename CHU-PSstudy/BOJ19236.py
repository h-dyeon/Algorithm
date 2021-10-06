import sys
import copy
# x는 행
# y는 열
# 공간은 4*4

# 번호 1~16
# 물고기는 모두 다른 번호

dr=[-1,-1,0,1,1,1,0,-1] # 1 indexing
dc=[0,-1,-1,-1,0,1,1,1]


# number=[[7, 2, 15, 9], [3, 1, 14, 10], [6, 13, 4, 11], [16, 8, 5, 12]]
# # direc=[[6, 3, 6, 8], [1, 8, 7, 1], [1, 6, 3, 4], [1, 7, 2, 2]]
# direc=[[5, 2, 5, 7], [0, 7, 6, 0], [0, 5, 2, 3], [0, 6, 1, 1]]

def findpos(val,number):
    for i in range(4):
        for j in range(4):
            if number[i][j]==val:
                return i,j
    return -1,-1

  
def func(number,direc,shark_r,shark_c):
    # shark
    
    nowshark=number[shark_r][shark_c]
    answer=nowshark
    number[shark_r][shark_c]=shark

    # fish
    for i in range(1,17):
        r,c=findpos(i,number)
        if r==-1:
            continue
        d=direc[r][c]
        for j in range(8):
            newr=r+dr[(d+j)%8]
            newc=c+dc[(d+j)%8]
            if 0<=newr<4 and 0<=newc<4 and blankfish<=number[newr][newc]<=16:
                if 1<=number[newr][newc]<=16:
                    number[r][c]=number[newr][newc]
                    direc[r][c]=direc[newr][newc]
                else:
                    number[r][c]=blankfish
                    direc[r][c]=-1
                number[newr][newc]=i
                direc[newr][newc]=(d+j)%8
                break
    #shark
    sr,sc=findpos(shark,number)
    sd=direc[sr][sc]
    for i in range(4):
        newsr=sr+(i+1)*dr[sd]
        newsc=sc+(i+1)*dc[sd]
        if not(0<=newsr<4 and 0<=newsc<4):
            break
        elif 0<=newsr<4 and 0<=newsc<4 and 1<=number[newsr][newsc]<=16:
            newnumber=copy.deepcopy(number)
            newnumber[sr][sc]=blankfish
            newdirec=copy.deepcopy(direc)
            hey=func(newnumber,newdirec,newsr,newsc)
            answer=max(answer,nowshark+hey)
    return answer

number=[[0] *4 for _ in range(4)]
direc=[[0] *4 for _ in range(4)]
for i in range(4):
    tmp=list(map(int, sys.stdin.readline().strip().split(' ')))
    for j in range(4):
        number[i][j]=tmp[j*2]
        direc[i][j]=tmp[j*2+1]-1

# number=[[12, 14, 4, 6], [15, 11, 3, 7], [10, 8, 16, 1], [5, 2, 13, 9]]
# direc=[[5, 4, 4, 6], [0, 6, 6, 4], [2, 2, 5, 0], [7, 6, 5, 1]]


blankfish=0
shark=100
a=func(number,direc, 0,0)
print(a)