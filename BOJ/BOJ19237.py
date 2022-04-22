################################################22.04.22
from collections import deque

if __name__ == '__main__':
    direc=[(-1,0),(1,0),(0,-1),(0,1)]
    N,M,K=map(int,input().split(' '))
    arr=[list(map(int,input().split(' '))) for _ in range(N)]
    shark_direc = list(map(int, input().split(' ')))
    tmp=[[list(map(int,input().split(' '))) for _ in range(4)] for _ in range(M)]
    shark_pos=[deque([(-1,-1) for _ in range(K-1)]) for _ in range(M+1)] # shark 1~M
    for i in range(N):
        for j in range(N):
            if arr[i][j]!=0:
                shark_pos[arr[i][j]].append((i,j))
    shark_direc=[-1]+[shark_direc[i]-1 for i in range(M)]  # shark 1~M
    tmp=[[[tmp[i][j][k]-1 for k in range(4)] for j in range(4)] for i in range(M)]
    shark_prio=[[]]
    for i in range(M):
        shark_prio.append(tmp[i])


    answer=-1
    for time_ in range(0,1001):
        status=True
        for i in range(2,M+1):
            if shark_direc[i]!=-1:
                status=False
                break
        if status or M==1:
            answer=time_
            break

        # move shark
        tmp=[r[:] for r in arr] # look tmp, modify arr
        for shark in range(1,M+1):
            if shark_direc[shark]==-1: # dead
                if len(shark_pos[shark])>0: # check smell
                    r,c=shark_pos[shark].popleft()
                    if 0<=r<N and 0<=c<N and tmp[r][c]==shark:
                        arr[r][c]=0
                        for cr,cc in shark_pos[shark]:
                            if cr==r and cc==c:
                                arr[r][c]=shark
                continue

            # shark is not dead.
            r, c = shark_pos[shark][-1]
            d=shark_direc[shark]

            nr,nc,nd=-1,-1,-1
            status = False
            for d_ in shark_prio[shark][d]:
                a,b=r+direc[d_][0],c+direc[d_][1]
                if 0<=a<N and 0<=b<N and tmp[a][b]==0: # no shark
                    nr,nc,nd=a,b,d_
                    status=True
                    break
            if status==False:
                for d_ in shark_prio[shark][d]:
                    a,b=r+direc[d_][0],c+direc[d_][1]
                    if 0<=a<N and 0<=b<N and tmp[a][b]==shark:  # my smell
                        nr,nc,nd=a,b,d_
                        break

            if nr==-1:
                print("----------이거는 방향 못찾을꺼대비-------------")

            # delete smell
            dr, dc = shark_pos[shark].popleft()
            if 0 <= dr < N and 0 <= dc < N and tmp[dr][dc] == shark:
                arr[dr][dc] = 0
                for cr, cc in shark_pos[shark]:
                    if cr == dr and cc == dc:
                        arr[dr][dc] = shark

            if arr[nr][nc]==0 or arr[nr][nc]==shark:
                shark_pos[shark].append((nr,nc))
                shark_direc[shark]=nd
                arr[nr][nc]=shark
            elif arr[nr][nc]>shark:
                weakShark=arr[nr][nc]
                shark_pos[weakShark].pop()
                shark_direc[weakShark]=-1

                shark_pos[shark].append((nr, nc))
                shark_direc[shark] = nd
                arr[nr][nc] = shark
            else: #arr[nr][nc]<shark:
                shark_direc[shark] = -1


    print(answer)



################################################
# from collections import deque
# N,M,K=map(int,input().split(' '))
# numshark=M
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# smells=[deque([(-1,-1) for _ in range(K-1)]) for _ in range(M+1)] # shark is 1 index
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]!=0:
#             smells[arr[i][j]].append((i,j))
# nowdirec=[0]+list(map(int,input().split(' ')))
# sharkdirec=[[] for _ in range(M+1)]
# for i in range(M):
#     tmp=[list(map(int,input().split(' '))) for _ in range(4)]
#     sharkdirec[i+1]=tmp

# print(smells)
# print(nowdirec)
# print(sharkdirec)
# print(arr)

# # N,M,K=5,4,4
# # numshark=M
# # smells=[deque([(-1, -1), (-1, -1), (-1, -1)]), deque([(-1, -1), (-1, -1), (-1, -1), (2, 0)]), deque([(-1, -1), (-1, -1), (-1, -1), (1, 1)]), deque([(-1, -1), (-1, -1), (-1, -1), (0, 4)]), deque([(-1, -1), (-1, -1), (-1, -1), (2, 4)])]
# # nowdirec=[0, 4, 4, 3, 1]
# # sharkdirec=[[], [[2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 2, 1], [4, 3, 1, 2]], [[2, 4, 3, 1], [2, 1, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]], [[4, 3, 2, 1], [1, 4, 3, 2], [1, 3, 2, 4], [3, 2, 1, 4]], [[3, 4, 1, 2], [3, 2, 4, 1], [1, 4, 2, 3], [1, 4, 2, 3]]]
# # arr=[[0, 0, 0, 0, 3], [0, 2, 0, 0, 0], [1, 0, 0, 0, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# direc=[(0,1),(-1,0),(1,0),(0,-1),(0,1)]


# answer=-1
# for t in range(1000):
#     if numshark==1:
#         answer=t
#         break
    
#     narr=[row[:] for row in arr]
#     for i in range(M,0,-1):
#         if nowdirec[i]==-1: # i shark is dead
#             if len(smells[i])>0:
#                 r,c=smells[i].popleft()
#                 if r!=-1 and narr[r][c]==i:
#                     narr[r][c]=0
#             continue
#         r,c=smells[i][-1]
#         nowd=nowdirec[i]
#         blankArea=[-1,-1,-1]
#         mysmell=[-1,-1,-1]
#         for nextd in sharkdirec[i][(nowd-1+4)%4]:
#             nr,nc=r+direc[nextd][0], c+direc[nextd][1]
#             if 0<=nr<N and 0<=nc<N :
#                 if arr[nr][nc]==0: # there is blank area
#                     blankArea=[nr,nc,nextd]
#                     break
#                 elif arr[nr][nc]==i and mysmell[0]==-1: # this is my smell
#                     mysmell=[nr,nc,nextd]
#                 else: # what the fuck
#                     print("d")
        
#         #move shark
#         nr,nc,nd=blankArea
#         if nr==-1:
#             nr,nc,nd=mysmell
        
#         nowdirec[i]=nd #change direction
#         smells[i].append((nr,nc)) # change position
#         if len(smells[i])>K: #too much smell
#             br,bc=smells[i].popleft()
#             if br!=-1 and narr[br][bc]==i and (br,bc) not in smells[i]:
#                 narr[br][bc]=0
#             else: # what the fuck
#                 print("d")

#         if arr[nr][nc]==0 and narr[nr][nc]==0: # there is no shark
#             narr[nr][nc]=i
#         elif arr[nr][nc]==0 and narr[nr][nc]>i: # there is stronger shark
#             weakShark=narr[nr][nc]
#             nowdirec[weakShark]=-1
#             smells[weakShark].pop()
#             narr[nr][nc]=i
#             numshark-=1
#         elif arr[nr][nc]==i: # there is my smell
#             narr[nr][nc]=i
#         else: # what the fuck
#             print("d")
#     arr=narr
        

# print(answer)





################################################

# from collections import deque
# N,M,k=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]

# sharkdirec=list(map(int,input().split(' ')))

# direc=[]*M
# for _ in range(M):
#     tmp=[list(map(int,input().split(' '))) for _ in range(4)]
#     direc.append(tmp)

# # print(arr)
# # print(direc)

# # N,M,k=5,4,4
# # arr=[[0, 0, 0, 0, 3], [0, 2, 0, 0, 0], [1, 0, 0, 0, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# # direc=[[[2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 2, 1], [4, 3, 1, 2]], [[2, 4, 3, 1], [2, 1, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]], [[4, 3, 2, 1], [1, 4, 3, 2], [1, 3, 2, 4], [3, 2, 1, 4]], [[3, 4, 1, 2], [3, 2, 4, 1], [1, 4, 2, 3], [1, 4, 2, 3]]]
# # sharkdirec=[4,4,3,1]

# dr=[0,-1,1,0,0]
# dc=[0,0,0,-1,1]

# sharklive=[1]*M
# sharkposition=[[0,0] for _ in range(M)]
# sharksmell=[deque([]) for _ in range(M)]
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]!=0:
#             s=arr[i][j] # 1 index
#             sharkposition[s-1][0]=i
#             sharkposition[s-1][1]=j
#             sharksmell[s-1].append((i,j))


# def update(s,check):
#     r,c=sharkposition[s]
#     nowdirec=sharkdirec[s] #1 index
#     directions=direc[s][nowdirec-1]

#     for i in directions:
#         nr,nc=r+dr[i],c+dc[i]
#         if 0<=nr<N and 0<=nc<N and arr[nr][nc]==check:
#             if narr[nr][nc]!=check:
#                 if (sharkposition[narr[nr][nc]-1][0]==nr and
#                     sharkposition[narr[nr][nc]-1][1]==nc): # there is real shark
#                     sharklive[s]=-1*(k-len(sharksmell[s])-1) # die
#                     sharkposition[s][0]=-1
#                     sharkposition[s][1]=-1
#                     return True
#             # just other shark smell or no shark
#             narr[nr][nc]=s+1 #move shark
#             sharkposition[s][0]=nr
#             sharkposition[s][1]=nc
#             sharkdirec[s]=i
#             sharksmell[s].append((nr,nc))
#             if len(sharksmell[s])>k: # delete smell
#                 tr,tc=sharksmell[s].popleft()
#                 if narr[tr][tc]==s+1 and (tr!=nr or tc!=nc):
#                     narr[tr][tc]=0
#             return True
#     return False


# answer=-1
# for t in range(1000):
#     if sum(sharklive)==1:
#         answer=t
#         break

#     narr=[row[:] for row in arr]

#     for s in range(M):
#         if sharklive[s]<0:
#             sharklive[s]+=1
#             continue
#         if sharklive[s]==0 :
#             if len(sharksmell[s])>0:
#                 tr,tc=sharksmell[s].popleft()
#                 if narr[tr][tc]==s+1:
#                     narr[tr][tc]=0
#             continue

#         ismoved=False
#         # no shark no smell
#         check=0
#         if not ismoved:
#             ismoved=update(s,0)  
#         # my smell
#         if not ismoved:
#             ismoved=update(s,s+1)
#         # cannot move.........?
#         if not ismoved:
#             print("funcked.....")
#     arr=narr

# print(answer)



