############################################22.04.19
N,K=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]
# red=set([])
# blue=set([])
# for i in range(N):
#     tmp=list(map(int,input().split(' ')))
#     for j in range(N):
#         if tmp[i][j]==1:
#             red.add((i,j))
#         if tmp[j][j]==2:
#             blue.add((i,j)) 
now_horse={(i,j):[] for j in range(N) for i in range(N)}

tmp=[list(map(int,input().split(' '))) for _ in range(K)]
horse_pos=[[0,0] for _ in range(K+1)]
horse_d=[0 for _ in range(K+1)]
for i in range(K):
    r,c,d=tmp[i]
    horse_pos[i+1]=[r-1,c-1]
    horse_d[i+1]=d-1
    now_horse[(r-1,c-1)].append(i+1)

direc=[(0,1),(0,-1),(-1,0),(1,0)]

def solve():
    for time_ in range(1,1001):
        for h in range(1,K+1):
            r,c=horse_pos[h]
            d=horse_d[h]
            nr,nc=r+direc[d][0],c+direc[d][1]
            #print(h,":",r,c,d,"(",direc[d],")=>",nr,nc,"-",arr[nr][nc])
            status=True
            if 0>nr or N<=nr or 0>nc or N<=nc or arr[nr][nc]==2: #out or blue
                nd=d
                if d==0: nd=1
                elif d==1: nd=0
                elif d==2: nd=3
                elif d==3: nd=2
                nr,nc=r+direc[nd][0],c+direc[nd][1]
                horse_d[h]=nd
                status=False
                if 0<=nr<N and 0<=nc<N and arr[nr][nc]!=2:
                    status=True
            if status: # red or white
                if arr[nr][nc]==0: #white
                    for i in range(len(now_horse[(r,c)])):
                        if now_horse[(r,c)][i]==h:
                            now_horse[(nr,nc)]+=now_horse[(r,c)][i:]
                            for h_ in now_horse[(r,c)][i:]: # move position
                                horse_pos[h_]=[nr,nc]
                            now_horse[(r,c)]=now_horse[(r,c)][0:i]
                            break                            
                elif arr[nr][nc]==1: #red
                    for i in range(len(now_horse[(r,c)])):
                        if now_horse[(r,c)][i]==h:
                            tmp=now_horse[(r,c)][i:]
                            tmp=list(reversed(tmp))
                            for h_ in tmp:
                                horse_pos[h_]=[nr,nc]
                            now_horse[(nr,nc)]+=tmp
                            now_horse[(r,c)]=now_horse[(r,c)][0:i]
                            break
                horse_pos[h]=[nr,nc]
                if len(now_horse[(nr,nc)])>=4:
                    return time_
    
    return -1

print(solve())
    












############################################3
# # N,K=map(int,input().split(' '))
# # arr=[list(map(int,input().split(' '))) for _ in range(N)]
# # cordi=[[0,0] for _ in range(K)]
# # chess={}
# # for k in range(K):
# #     r,c,d=map(int,input().split(' '))
# #     cordi[k]=[r-1,c-1,d-1]
# #     chess.setdefault((r-1,c-1),[]).append(k)
# direc=[[0,1],[0,-1],[-1,0],[1,0]] #[r,c]
# N=4
# chess={(i,j):[] for i in range(N) for j in range(N)}

# # print(arr)
# # print(cordi)
# # print(chess)

# # N,K=4,4
# # arr=[[0, 0, 2, 0], [0, 0, 1, 0], [0, 0, 1, 2], [0, 2, 0, 0]]
# # cordi=[[1, 0, 0], [2, 1, 2], [1, 1, 0], [3, 0, 1]]
# # chess={(1, 0): [0], (2, 1): [1], (1, 1): [2], (3, 0): [3]}

# N,K=6,10
# arr=[[0, 1, 2, 0, 1, 1], [1, 2, 0, 1, 1, 0], [2, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 2], [2, 0, 1, 2, 0, 1], [0, 2, 1, 0, 2, 1]]
# cordi=[[0, 0, 0], [1, 1, 1], [2, 2, 3], [3, 3, 0], [4, 4, 2], [5, 5, 1], [0, 5, 2], [5, 0, 1], [1, 3, 2], [3, 1, 0]]
# chess={(0, 0): [0], (1, 1): [1], (2, 2): [2], (3, 3): [3], (4, 4): [4], (5, 5): [5], (0, 5): [6], (5, 0): [7], (1, 3): [8], (3, 1): [9]}

# def move_red(r,c,nr,nc,k):
#     idx=chess[(r,c)].index(k)
#     for i in range(len(chess[(r,c)])-1,idx-1,-1):
#         tmp=chess[(r,c)].pop(i)
#         cordi[tmp][0]=nr
#         cordi[tmp][1]=nc
#         chess.setdefault((nr,nc),[]).append(tmp)
#     return

# def move_white(r,c,nr,nc,k):
#     idx=chess[(r,c)].index(k)
#     while len(chess[(r,c)]) > idx:
#         tmp=chess[(r,c)].pop(idx)
#         cordi[tmp][0]=nr
#         cordi[tmp][1]=nc
#         chess.setdefault((nr,nc),[]).append(tmp)
#     return

# def solve():
#     for t in range(1,1001):
#         for k in range(K):
#             r,c,d=cordi[k]
#             nr,nc=r+direc[d][0],c+direc[d][1]
#             if 0<=nr<N and 0<=nc<N and arr[nr][nc]!=2: #not blue
#                 if arr[nr][nc]==0: #white
#                     move_white(r,c,nr,nc,k)
#                 elif arr[nr][nc]==1: #red
#                     move_red(r,c,nr,nc,k)
#                 if len(chess[(nr,nc)])>=4:
#                     return t
#             else:
#                 if d==0: d=1
#                 elif d==1: d=0
#                 elif d==2: d=3
#                 elif d==3: d=2
#                 nr,nc=r+direc[d][0],c+direc[d][1]
#                 cordi[k][2]=d
#                 if 0<=nr<N and 0<=nc<N and arr[nr][nc]!=2: #not blue
#                     if arr[nr][nc]==0: #white
#                         move_white(r,c,nr,nc,k)
#                     elif arr[nr][nc]==1: #red
#                         move_red(r,c,nr,nc,k)
#                     if len(chess[(nr,nc)])>=4:
#                         return t
#                 else: #not move, just change direction
#                     cordi[k][2]=d
#     return -1
# print(solve())





# # a={}
# # a.setdefault((3,2),[]).append((1,2))
# # a.setdefault((3,2),[]).append((1,3))
# # a.setdefault((3,2),[]).append((1,4))

# # a.setdefault((1,1),[]).append(a[(3,2)].pop(1))
# # a.setdefault((1,1),[]).append(a[(3,2)].pop(1))

