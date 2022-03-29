R,C,T=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(R)]

top,bottom=0,0
for i in range(R):
    if arr[i][0]==-1:
        top=i
        bottom=i+1
        break


for _ in range(T):

    ##### spread() #####
    narr=[row[:] for row in arr]
    for r in range(R):
        for c in range(C):
            if arr[r][c]<=0:
                continue
            ### check direction ###
            cnt=0
            tmp=int(arr[r][c]/5)
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<R and 0<=nc<C and arr[nr][nc]!=-1:
                    cnt+=1
                    narr[nr][nc]+=tmp
            ### add dust ###
            narr[r][c]-=tmp*cnt
    arr=[row[:] for row in narr]



    # clean()
    #top
    for i in range(top-1,-1,-1):
        arr[i+1][0]=arr[i][0]
    for i in range(1,C):
        arr[0][i-1]=arr[0][i]
    for i in range(1,top+1):
        arr[i-1][C-1]=arr[i][C-1]
    for i in range(C-2,-1,-1):
        arr[top][i+1]=arr[top][i]
    arr[top][0]=-1 #clean!
    arr[top][1]=0 #clean!

    # bottom
    for i in range(bottom+1,R):
        arr[i-1][0]=arr[i][0]
    for i in range(1,C):
        arr[R-1][i-1]=arr[R-1][i]
    for i in range(R-2,bottom-1,-1):
        arr[i+1][C-1]=arr[i][C-1]
    for i in range(C-2,-1,-1):
        arr[bottom][i+1]=arr[bottom][i]
    arr[bottom][0]=-1 #clean!
    arr[bottom][1]=0 #clean!


answer=sum([sum(row) for row in arr])
print(answer+2)