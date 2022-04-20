

######################################### 22.04.20

def makeindex():
    bizz=[]
    tmp=[[-2]*N for _ in range(N)]
    direc=[(0,-1),(1,0),(0,1),(-1,0)]

    r,c,d=int((N+1)/2)-1,int((N+1)/2)-1,0
    tmp[r][c]=-1
    val=-1

    while r!=0 or c!=0:
        r,c=r+direc[d][0],c+direc[d][1]
        val+=1
        tmp[r][c]=val
        bizz.append(arr[r][c])
        if tmp[r+direc[(d+1)%4][0]][c+direc[(d+1)%4][1]]==-2:
            d=(d+1)%4
    return tmp,bizz




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N, M = map(int, input().split(' '))
    arr=[list(map(int,input().split(' '))) for _ in range(N)]
    magic = [list(map(int, input().split(' '))) for _ in range(M)]

    indexmap,bizz=makeindex()
    direc = [(0, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
    answer=[0,0,0,0] #boom!
    center_r,center_c=int((N+1)/2)-1,int((N+1)/2)-1

    for d,s in magic:
        # delete
        for s_ in range(s,0,-1):
            nr,nc=center_r+direc[d][0]*s_, center_c+direc[d][1]*s_
            num=indexmap[nr][nc]
            del bizz[num]

        # boom
        status=True
        while status:
            status=False
            last=len(bizz)
            i=last
            while i>0:
                i-=1
                if bizz[i]==bizz[i-1]:
                    start=i-1
                    for j in range(i-1,-1,-1):
                        if bizz[i]!=bizz[j]:
                            break
                        start=j
                    if i+1-start>=4:
                        answer[bizz[i]]+=(i+1-start)
                        bizz=bizz[:start]+bizz[i+1:]
                        i=start
                        status=True
        # group
        tmp=[0 for _ in range(N*N-1)]
        idx=0
        len_=len(bizz)
        i=0
        while i<len_:
            cnt=1
            for j in range(1,len_-i):
                if bizz[i]!=bizz[i+j]:
                    break
                cnt+=1

            tmp[idx]=cnt
            tmp[idx+1]=bizz[i]
            i=i+cnt
            idx+=2
            if idx>=N*N-1:
                break

        bizz=tmp

    tmp=0
    for i in range(1,4):
        tmp+=i*answer[i]
    print(tmp)




# N,M=map(int,input().split(' '))
# arr=[[0] for _ in range(N+1)]
# arr[0]=[0]*(N+1)
# for i in range(1,N+1):
#     arr[i]=[0]+list(map(int,input().split(' ')))
# magic=[list(map(int,input().split(' '))) for _ in range(M)]

# def makeidxmap():
#     global arr
#     idxmap=[[0]*(N+1) for _ in range(N+1)]
#     tmp=[0 for _ in range(N*N)]
#     dr=[0,1,0,-1]
#     dc=[-1,0,1,0]
#     d=0
#     i=0
#     r,c=int((N+1)/2),int((N+1)/2)
#     idxmap[r][c]=-1
#     while r!=1 or c!=1:
#         i+=1
#         r,c=r+dr[d],c+dc[d]
#         idxmap[r][c]=i
#         tmp[i]=arr[r][c]
#         if idxmap[r+dr[(d+1)%4]][c+dc[(d+1)%4]]==0:
#             d=(d+1)%4
#     return idxmap,tmp

# idxmap,arr=makeidxmap()
# dr=[0,-1,1,0,0]
# dc=[0,0,0,-1,1]
# answer=[0,0,0,0]
# sr,sc=int((N+1)/2),int((N+1)/2)
# for m in range(M):

#     # delete bizz
#     d,s=magic[m]
#     for k in range(s,-0,-1):
#         nr,nc=sr+k*dr[d],sc+k*dc[d]
#         tmp=idxmap[nr][nc]
#         del arr[tmp]
    
#     # boom!
#     status=True
#     while status:
#         status=False
#         i=len(arr)-1
#         while i>3:
#             if arr[i]==arr[i-1]==arr[i-2]==arr[i-3]:
#                 start=i-3
#                 for j in range(i-3,1,-1):
#                     if arr[j]==arr[j-1]:
#                         start=j-1
#                     else:
#                         break
#                 answer[arr[i]]+=(i+1-start)
#                 status=True
#                 del arr[start:i+1]            
#                 i=start-1
#             else:
#                 i-=1

    
#     #check no bizz
#     if len(arr)<=1 or arr.count(0)==len(arr):
#         break
    
#     # change bizz
#     tmp=[0]*(N*N)
#     i,j,cnt=1,2,1
#     idx=1
#     len_=len(arr)
#     while True:
#         if j==len(arr):
#             if idx==N*N: 
#                 break
#             tmp[idx]=cnt
#             if idx+1==N*N: 
#                 break
#             tmp[idx+1]=arr[i]
#             break
#         if arr[i]!=arr[j]:
#             if idx==N*N: 
#                 break
#             tmp[idx]=cnt
#             if idx+1==N*N: 
#                 break
#             tmp[idx+1]=arr[i]
#             idx+=2
#             i,j,cnt=j,j+1,1
#         else:
#             cnt+=1
#             j+=1
#     arr=tmp

# print(answer[1]*1 + answer[2]*2+answer[3]*3)    