from collections import deque
M,S=map(int,input().split(' '))
arr=[[deque([]) for _ in range(4)] for _ in range(4)]
for _ in range(M):
    x,y,d=map(int,input().split(' '))
    arr[x-1][y-1].appendleft(d)
X,Y=map(int,input().split(' ')) #shark
X-=1
Y-=1
print(arr)
# M,S=5,3
# arr=[[deque([]), deque([]), deque([5]), deque([])], [deque([6]), deque([]), deque([]), deque([2])], [deque([]), deque([]), deque([]), deque([4])], [deque([]), deque([]), deque([5]), deque([])]]
# X,Y=3,1

dr=[1,0,-1,-1,-1,0,1,1,1]
dc=[-1,-1,-1,0,1,1,1,0,-1]
sdr=[0,-1,0,1,0]
sdc=[1,0,-1,0,1]
smells=[[[0 for _ in range(4)] for _ in range(4)] for _ in range(3)]
smellIdx=0 # you have to set in smells[smellIdx], delete smells[smellIdx-2]

def getSharkmove(tmp):
    mstr=[1e9,1e9,1e9]
    maxsum=0
    visit=[[len(tmp[i][j]) for j in range(4)] for i in range(4)]

    for a in range(1,5):
        nr,nc=X+sdr[a],Y+sdc[a]
        if nr<0 or nc<0 or nr>=4 or nc>=4:
            continue
        a_=visit[nr][nc]
        nfish=visit[nr][nc]
        visit[nr][nc]=0

        for b in range(1,5):
            nnr,nnc=nr+sdr[b],nc+sdc[b]
            if nnr<0 or nnc<0 or nnr>=4 or nnc>=4:
                continue
            b_=visit[nnr][nnc]
            nnfish=visit[nnr][nnc]+nfish
            visit[nnr][nnc]=0

            for c in range(1,5):
                nnnr,nnnc=nnr+sdr[c],nnc+sdc[c]
                if nnnr<0 or nnnc<0 or nnnr>=4 or nnnc>=4:
                    continue
                nnnfish=visit[nnnr][nnnc]+nnfish
                if maxsum<nnnfish:
                    mstr=[a,b,c]
                    maxsum=nnnfish
                elif maxsum==nnnfish:
                    if a<=mstr[0]:
                        if b<=mstr[1]:
                            if c<=mstr[2]:
                                mstr=[a,b,c]
            visit[nnr][nnc]=b_
        visit[nr][nc]=a_
    return mstr

for _ in range(S):
    # step 1
    tmp=[[deque([]) for _ in range(4)] for _ in range(4)]

    # move fish
    for i in range(4):
        for j in range(4):
            for d in arr[i][j]:
                status=True
                for k in range(8):
                    nr,nc=i+dr[(d-k+8)%8], j+dc[(d-k+8)%8]
                    if (0<=nr<4 and 0<=nc<4 and 
                        (nr!=X or nc!=Y) and
                        smells[(smellIdx-1+3)%3][nr][nc]==0 and
                        smells[(smellIdx-2+3)%3][nr][nc]==0):
                        tmp[nr][nc].appendleft((d-k+8)%8)
                        status=False
                        break
                if status:
                    tmp[i][j].appendleft(d)
    # move shark
    direc=getSharkmove(tmp)
    for d in direc:
        nr,nc=X+sdr[d],Y+sdc[d]
        if len(tmp[nr][nc])>0:
            tmp[nr][nc].clear()
            smells[smellIdx][nr][nc]=1
        X,Y=nr,nc

    # delete smell
    smells[(smellIdx-2+3)%3]=[[0]*4 for _ in range(4)]
    smellIdx=(smellIdx+1)%3

    # complete duplicate magic
    for i in range(4):
        for j in range(4):
            for d in tmp[i][j]:
                arr[i][j].append(d)

answer=[len(arr[i][j]) for i in range(4) for j in range(4)]
print(sum(answer))

