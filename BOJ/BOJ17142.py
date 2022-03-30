# from collections import deque

# N,M=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# print(arr)

# virus=[]
# viruscnt=0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]==2:
#             virus.append((i,j))
#             viruscnt+=1


# def bfs(rr,cc):
#     diffuselist={}
#     visit=[[True if arr[r][c]!=0 else False for c in range(N)] for r in range(N)]
#     dq=deque([(rr,cc,0)])    
#     while dq:
#         r,c,t=dq.popleft()
#         for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nr,nc=r+dr,c+dc
#             if 0<=nr<N and 0<=nc<N and visit[nr][nc]==False and arr[nr][nc]!=1:
#                 visit[nr][nc]=True
#                 dq.append((nr,nc,t+1))
#                 if t+1 in diffuselist:
#                     diffuselist[t+1].append((nr,nc))
#                 else:
#                      diffuselist[t+1]=[(nr,nc)]
#     return diffuselist

# virusdiffuse=[{} for _ in range(viruscnt)]
# for i in range(viruscnt):
#     r,c=virus[i]
#     virusdiffuse[i]=bfs(r,c)


# answer=1e9
# mset=[0]*(1<<(viruscnt+1))

# def calcTime(bits):
#     global answer
#     visit=[[True if arr[r][c]!=0 else False for c in range(N)] for r in range(N)]
    
#     for t in range(1,100000):
#         if answer<t:
#             return
#         if sum([visit[i].count(False) for i in range(N)])==0:
#             answer=min(answer,t-1)
#             return
#         change=False
#         for v in range(viruscnt):
#             if bits & (1<<v)>0:
#                 if t in virusdiffuse[v]:
#                     for a,b in virusdiffuse[v][t]:
#                         if visit[a][b]==False:
#                             change=True
#                         visit[a][b]=True
#         if change==False:
#             return

   

# def dfs(bits,cnt):
#     global mset
#     if cnt==0:
#         # print(bin(bits),cnt)
#         calcTime(bits)
#     else:
#         for i in range(viruscnt):
#             if bits&(1<<i)>0:
#                 continue
#             status=bits|(1<<i)
#             if mset[status]==1:
#                 continue
#             mset[status]=1
#             dfs(status,cnt-1)


# dfs(1<<viruscnt,M)
# print(-1 if answer==1e9 else answer)


from collections import deque

N,M=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]
print(arr)

# N,M=7,3
# arr=[[2, 0, 2, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0], [2, 1, 0, 0, 0, 0, 2], [1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [2, 1, 0, 0, 2, 0, 2]]
# arr=[[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 2]]
virus=[]
viruscnt=0
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            virus.append((i,j))
            viruscnt+=1
answer=1e9
mset=[0]*(1<<(viruscnt+1))


def bfs(bits):
    global answer
    visit=[[-1 if arr[r][c]!=1 else 0 for c in range(N)] for r in range(N)]
    notvitalvirus=set()
    dq=deque([])    
    for i in range(viruscnt):
        a,b=virus[i]
        if bits&(1<<i)>0:
            dq.append((a,b))
            visit[a][b]=0
        else:
            notvitalvirus.add((a,b))

    cnt=0
    while dq:
        r,c=dq.popleft()
        t=visit[r][c]
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and arr[nr][nc]!=1 and visit[nr][nc]<0 :
                if arr[nr][nc]==2 and (nr,nc) in notvitalvirus:
                    notvitalvirus.remove((nr,nc))
                else:
                    cnt=t+1
                        
                visit[nr][nc]=t+1
                dq.append((nr,nc))
    if sum([visit[i].count(-1) for i in range(N)])==0:
        answer=min(answer,cnt)
        return 
   

def dfs(bits,cnt):
    global mset
    if cnt==0:
        # print(bin(bits),cnt)
        bfs(bits)
    else:
        for i in range(viruscnt):
            if bits&(1<<i)>0:
                continue
            status=bits|(1<<i)
            if mset[status]==1:
                continue
            mset[status]=1
            dfs(status,cnt-1)


dfs(1<<viruscnt,M)
print(-1 if answer==1e9 else answer)