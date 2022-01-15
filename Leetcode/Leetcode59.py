answer=[[0 for _ in range(n)] for _ in range(n)]
tmp=1
r,c,mode=0,-1,0
dr=[0,-1,0,1]
dc=[1,0,-1,0]

while tmp<=n*n:
    tr=r+dr[mode]
    tc=c+dc[mode]
    for i in range(4):
        if 0<=tr<n and 0<=tc<n and answer[tr][tc]==0:
            r,c=tr,tc
            answer[r][c]=tmp
            tmp+=1
            break
        else:
            mode=(mode+1)%4
            tr=r+dr[mode]
            tc=c+dc[mode]
print(answer)