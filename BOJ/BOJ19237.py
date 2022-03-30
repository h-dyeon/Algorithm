from collections import deque
N,M,k=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]

sharkdirec=list(map(int,input().split(' ')))

direc=[]*M
for _ in range(M):
    tmp=[list(map(int,input().split(' '))) for _ in range(4)]
    direc.append(tmp)

# print(arr)
# print(direc)

# N,M,k=5,4,4
# arr=[[0, 0, 0, 0, 3], [0, 2, 0, 0, 0], [1, 0, 0, 0, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# direc=[[[2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 2, 1], [4, 3, 1, 2]], [[2, 4, 3, 1], [2, 1, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]], [[4, 3, 2, 1], [1, 4, 3, 2], [1, 3, 2, 4], [3, 2, 1, 4]], [[3, 4, 1, 2], [3, 2, 4, 1], [1, 4, 2, 3], [1, 4, 2, 3]]]
# sharkdirec=[4,4,3,1]

dr=[0,-1,1,0,0]
dc=[0,0,0,-1,1]

sharklive=[1]*M
sharkposition=[[0,0] for _ in range(M)]
sharksmell=[deque([]) for _ in range(M)]
for i in range(N):
    for j in range(N):
        if arr[i][j]!=0:
            s=arr[i][j] # 1 index
            sharkposition[s-1][0]=i
            sharkposition[s-1][1]=j
            sharksmell[s-1].append((i,j))


def update(s,check):
    r,c=sharkposition[s]
    nowdirec=sharkdirec[s] #1 index
    directions=direc[s][nowdirec-1]

    for i in directions:
        nr,nc=r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc]==check:
            if narr[nr][nc]!=check:
                if (sharkposition[narr[nr][nc]-1][0]==nr and
                    sharkposition[narr[nr][nc]-1][1]==nc): # there is real shark
                    sharklive[s]=-1*(k-len(sharksmell[s])-1) # die
                    sharkposition[s][0]=-1
                    sharkposition[s][1]=-1
                    return True
            # just other shark smell or no shark
            narr[nr][nc]=s+1 #move shark
            sharkposition[s][0]=nr
            sharkposition[s][1]=nc
            sharkdirec[s]=i
            sharksmell[s].append((nr,nc))
            if len(sharksmell[s])>k: # delete smell
                tr,tc=sharksmell[s].popleft()
                if narr[tr][tc]==s+1 and (tr!=nr or tc!=nc):
                    narr[tr][tc]=0
            return True
    return False


answer=-1
for t in range(1000):
    if sum(sharklive)==1:
        answer=t
        break

    narr=[row[:] for row in arr]

    for s in range(M):
        if sharklive[s]<0:
            sharklive[s]+=1
            continue
        if sharklive[s]==0 :
            if len(sharksmell[s])>0:
                tr,tc=sharksmell[s].popleft()
                if narr[tr][tc]==s+1:
                    narr[tr][tc]=0
            continue

        ismoved=False
        # no shark no smell
        check=0
        if not ismoved:
            ismoved=update(s,0)  
        # my smell
        if not ismoved:
            ismoved=update(s,s+1)
        # cannot move.........?
        if not ismoved:
            print("funcked.....")
    arr=narr

print(answer)



