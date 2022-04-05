# N,K=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# cordi=[[0,0] for _ in range(K)]
# chess={}
# for k in range(K):
#     r,c,d=map(int,input().split(' '))
#     cordi[k]=[r-1,c-1,d-1]
#     chess.setdefault((r-1,c-1),[]).append(k)
direc=[[0,1],[0,-1],[-1,0],[1,0]] #[r,c]
N=4
chess={(i,j):[] for i in range(N) for j in range(N)}

# print(arr)
# print(cordi)
# print(chess)

# N,K=4,4
# arr=[[0, 0, 2, 0], [0, 0, 1, 0], [0, 0, 1, 2], [0, 2, 0, 0]]
# cordi=[[1, 0, 0], [2, 1, 2], [1, 1, 0], [3, 0, 1]]
# chess={(1, 0): [0], (2, 1): [1], (1, 1): [2], (3, 0): [3]}

N,K=6,10
arr=[[0, 1, 2, 0, 1, 1], [1, 2, 0, 1, 1, 0], [2, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 2], [2, 0, 1, 2, 0, 1], [0, 2, 1, 0, 2, 1]]
cordi=[[0, 0, 0], [1, 1, 1], [2, 2, 3], [3, 3, 0], [4, 4, 2], [5, 5, 1], [0, 5, 2], [5, 0, 1], [1, 3, 2], [3, 1, 0]]
chess={(0, 0): [0], (1, 1): [1], (2, 2): [2], (3, 3): [3], (4, 4): [4], (5, 5): [5], (0, 5): [6], (5, 0): [7], (1, 3): [8], (3, 1): [9]}

def move_red(r,c,nr,nc,k):
    idx=chess[(r,c)].index(k)
    for i in range(len(chess[(r,c)])-1,idx-1,-1):
        tmp=chess[(r,c)].pop(i)
        cordi[tmp][0]=nr
        cordi[tmp][1]=nc
        chess.setdefault((nr,nc),[]).append(tmp)
    return

def move_white(r,c,nr,nc,k):
    idx=chess[(r,c)].index(k)
    while len(chess[(r,c)]) > idx:
        tmp=chess[(r,c)].pop(idx)
        cordi[tmp][0]=nr
        cordi[tmp][1]=nc
        chess.setdefault((nr,nc),[]).append(tmp)
    return

def solve():
    for t in range(1,1001):
        for k in range(K):
            r,c,d=cordi[k]
            nr,nc=r+direc[d][0],c+direc[d][1]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc]!=2: #not blue
                if arr[nr][nc]==0: #white
                    move_white(r,c,nr,nc,k)
                elif arr[nr][nc]==1: #red
                    move_red(r,c,nr,nc,k)
                if len(chess[(nr,nc)])>=4:
                    return t
            else:
                if d==0: d=1
                elif d==1: d=0
                elif d==2: d=3
                elif d==3: d=2
                nr,nc=r+direc[d][0],c+direc[d][1]
                cordi[k][2]=d
                if 0<=nr<N and 0<=nc<N and arr[nr][nc]!=2: #not blue
                    if arr[nr][nc]==0: #white
                        move_white(r,c,nr,nc,k)
                    elif arr[nr][nc]==1: #red
                        move_red(r,c,nr,nc,k)
                    if len(chess[(nr,nc)])>=4:
                        return t
                else: #not move, just change direction
                    cordi[k][2]=d
    return -1
print(solve())





# a={}
# a.setdefault((3,2),[]).append((1,2))
# a.setdefault((3,2),[]).append((1,3))
# a.setdefault((3,2),[]).append((1,4))

# a.setdefault((1,1),[]).append(a[(3,2)].pop(1))
# a.setdefault((1,1),[]).append(a[(3,2)].pop(1))

