from collections import deque
N,M,feul=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]
r,c=map(int,input().split(' '))
r-=1
c-=1
person=[list(map(int,input().split(' '))) for _ in range(M)] #1 index

oklist=[0]*len(person)

def calcdistmap(R,C):
    visited=[[-1 if arr[i][j]==1 else 1e9+1 for j in range(N)] for i in range(N)]
    visited[R][C]=0
    dq=deque([(R,C)])
    while dq:
        r,c=dq.popleft()
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==(1e9+1):
                visited[nr][nc]=visited[r][c]+1
                dq.append((nr,nc))
    
    return visited

for _ in range(M):
    distmap=calcdistmap(r,c)

    # pick person
    d=1e9
    p,pr,pc=-1,1e9,1e9
    for i in range(len(person)):
        if oklist[i]==1: # already moved
            continue
        a,b=person[i][0]-1,person[i][1]-1
        if distmap[a][b]<d:
            d=distmap[a][b]
            p,pr,pc=i,a,b
        elif distmap[a][b]==d and (a<pr or (a==pr and b<pc)):
            p,pr,pc=i,a,b
    if p==-1:
        break
    
    # go to person
    feul-=d
    r,c=pr,pc

    # move to target position
    distmap=calcdistmap(r,c)
    tr,tc=person[p][2]-1,person[p][3]-1
    d=distmap[tr][tc]
    if feul>=d:
        feul+=d
        r,c=tr,tc
        oklist[p]=1
    else:
        break

if sum(oklist)!=len(person) or feul<0:
    print(-1)
else:
    print(feul)