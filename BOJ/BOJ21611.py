N,M=map(int,input().split(' '))
arr=[[0] for _ in range(N+1)]
arr[0]=[0]*(N+1)
for i in range(1,N+1):
    arr[i]=[0]+list(map(int,input().split(' ')))
magic=[list(map(int,input().split(' '))) for _ in range(M)]

def makeidxmap():
    global arr
    idxmap=[[0]*(N+1) for _ in range(N+1)]
    tmp=[0 for _ in range(N*N)]
    dr=[0,1,0,-1]
    dc=[-1,0,1,0]
    d=0
    i=0
    r,c=int((N+1)/2),int((N+1)/2)
    idxmap[r][c]=-1
    while r!=1 or c!=1:
        i+=1
        r,c=r+dr[d],c+dc[d]
        idxmap[r][c]=i
        tmp[i]=arr[r][c]
        if idxmap[r+dr[(d+1)%4]][c+dc[(d+1)%4]]==0:
            d=(d+1)%4
    return idxmap,tmp

idxmap,arr=makeidxmap()
dr=[0,-1,1,0,0]
dc=[0,0,0,-1,1]
answer=[0,0,0,0]
sr,sc=int((N+1)/2),int((N+1)/2)
for m in range(M):

    # delete bizz
    d,s=magic[m]
    for k in range(s,-0,-1):
        nr,nc=sr+k*dr[d],sc+k*dc[d]
        tmp=idxmap[nr][nc]
        del arr[tmp]
    
    # boom!
    status=True
    while status:
        status=False
        i=len(arr)-1
        while i>3:
            if arr[i]==arr[i-1]==arr[i-2]==arr[i-3]:
                start=i-3
                for j in range(i-3,1,-1):
                    if arr[j]==arr[j-1]:
                        start=j-1
                    else:
                        break
                answer[arr[i]]+=(i+1-start)
                status=True
                del arr[start:i+1]            
                i=start-1
            else:
                i-=1

    
    #check no bizz
    if len(arr)<=1 or arr.count(0)==len(arr):
        break
    
    # change bizz
    tmp=[0]*(N*N)
    i,j,cnt=1,2,1
    idx=1
    len_=len(arr)
    while True:
        if j==len(arr):
            if idx==N*N: 
                break
            tmp[idx]=cnt
            if idx+1==N*N: 
                break
            tmp[idx+1]=arr[i]
            break
        if arr[i]!=arr[j]:
            if idx==N*N: 
                break
            tmp[idx]=cnt
            if idx+1==N*N: 
                break
            tmp[idx+1]=arr[i]
            idx+=2
            i,j,cnt=j,j+1,1
        else:
            cnt+=1
            j+=1
    arr=tmp

print(answer[1]*1 + answer[2]*2+answer[3]*3)    