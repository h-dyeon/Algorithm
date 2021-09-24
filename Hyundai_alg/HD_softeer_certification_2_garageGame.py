import sys
from collections import deque


def func(mat,cnt):
    print("now mat=",mat)
    dr=[1,0,-1,0]
    dc=[0,1,0,-1]
    visited=[0]*N # bitmask N<=15
    answer=0
    for r in range(N):
        for c in range(N):
            if (visited[r] & (1<<(c)))==0: 
                nowanswer=1
                rectRow=[r,r]
                rectCol=[c,c]
                forNewMat=[0]*N # bitmask N<=15

                #find same colors
                nowcolor=mat[r][c]
                dq=deque([[r,c]])
                visited[r] |= (1<<c)
                forNewMat[r] |= (1<<c)
                while dq:
                    rr,cc=dq.popleft()
                    for k in range(4):
                        newR=rr+dr[k]
                        newC=cc+dc[k]
                        if 0<=newR<N and 0<=newC<N and mat[newR][newC]==nowcolor and (visited[newR] & (1<<(newC)))==0:
                            visited[newR] |= (1<<newC)
                            forNewMat[newR] |= (1<<newC)
                            dq.append([newR,newC])
                            nowanswer+=1
                            rectRow[0]=min(rectRow[0], newR)
                            rectRow[1]=max(rectRow[1],newR)
                            rectCol[0]=min(rectCol[0],newC)
                            rectCol[1]=max(rectCol[1],newC)
                print("\tvisited",visited,"\tforNewMat",forNewMat)

                #calculate answer
                square=(rectRow[1]+1-rectRow[0])*(rectCol[1]-rectCol[0]+1)
                print("\tnowcolor=",nowcolor,"\tcnt=",cnt,"\tnowanswer=",nowanswer,"\tsqure=",square,"\tsum=",nowanswer+square)
                if cnt==0:
                    answer=max(answer,nowanswer+square)
                else:
                    #reset matrix
                    newmat=[[] for _ in range(N)]
                    for i in range(N):
                        for j in range(N):
                            if (forNewMat[i] & (1<<j))==0:
                                newmat[i].append(mat[i][j])
                        newmat[i]+=mat[i][N:]
                    #print(newmat)
                    answer=max(answer,nowanswer+square+func(newmat,cnt-1))
    print("cnt=",cnt,"\tanswer=",answer)              
    return answer
                


N=int(sys.stdin.readline().strip())
matrix=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(3*N)]
# N=3
# matrix=[[8, 5, 1], [9, 6, 1], [10, 7, 1], [11, 1, 3], [12, 1, 3], [13, 1, 3], [1, 2, 2], [1, 2, 2], [1, 2, 2]]
newmatrix=[]
#b=list(zip(*matrix))[0]
for j in range(N):
    newmatrix.append(list(reversed([i[j] for i in matrix])))



s=func(newmatrix,2)
print(s)