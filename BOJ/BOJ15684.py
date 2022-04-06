



N,M,H=map(int,input().split(' '))
arr=[[0]*(N-1) for _ in range(H)]
for _ in range(M):
    a,b=map(int,input().split(' '))
    arr[a-1][b-1]=1
print(arr)

# N,M,H=5,5,6
# arr=[[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
answer=1e9

def check():
    for c in range(N):
        i=c
        for r in range(H):
            if i<N-1 and arr[r][i]==1:
                i+=1
                continue
            if i>0 and arr[r][i-1]==1:
                i-=1
                continue
        if c!=i:
            return False
    return True


def pick(cnt,startidx):
    global arr,answer
    if check():
        answer=min(answer,cnt)
        return
    if cnt>=answer:
        return
    if cnt==3:
        return

    for i in range(startidx,(N-1)*H):
        x=int(i/(N-1))
        y=i%(N-1)
        if arr[x][y]==1:
            continue
        if y-1>=0 and arr[x][y-1]==1:
            continue
        if y+1<N-1 and arr[x][y+1]==1:
            continue

        arr[x][y]=1
        pick(cnt+1,i+1)
        arr[x][y]=0



pick(0,0)
if answer==1e9:
    print(-1)
else:
    print(answer)





########################################3

# from collections import deque

# N,M,H=map(int,input().split(' '))
# arr=[[0]*(N-1) for _ in range(H)]
# for _ in range(M):
#     a,b=map(int,input().split(' '))
#     arr[a-1][b-1]=1
# print(arr)

# # N,M,H=5,5,6
# # arr=[[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
# def check():
#     for c in range(N-1):
#         tmp=c
#         for r in range(H):
#             if tmp<N-1 and arr[r][tmp]==1:
#                 tmp+=1
#             elif tmp>0 and arr[r][tmp-1]==1:
#                 tmp-=1
#         if c!=tmp:
#             return False   
#     return True

# def checkside(r,c):
#     if arr[r][c]==1: 
#         return True
#     if c>0 and arr[r][c-1]!=0:
#         return True
#     if c<N-2 and arr[r][c+1]!=0:
#         return True
#     return False


# def findanswer():
#     # add 0
#     if check():
#         return 0

#     # add 1
#     for i in range(0,(N-1)*H):
#         r,c=int(i/(N-1)),i%(N-1)
#         if checkside(r,c):
#             continue
#         arr[r][c]=1
#         if check():
#             return 1
#         arr[r][c]=0
        
#     # add 2
#     for i in range(0,(N-1)*H-1):
#         r,c=int(i/(N-1)),i%(N-1)
#         if checkside(r,c):
#             continue
#         arr[r][c]=1
#         for j in range(i,(N-1)*H):
#             rr,cc=int(j/(N-1)),j%(N-1)
#             if checkside(rr,cc):
#                 continue
#             arr[rr][cc]=1
#             if check():
#                 return 2
#             arr[rr][cc]=0
#         arr[r][c]=0
    
#     # add 3
#     for i in range(0,(N-1)*H-2):
#         r,c=int(i/(N-1)),i%(N-1)
#         if checkside(r,c):
#             continue
#         arr[r][c]=1
#         for j in range(i,(N-1)*H-1):
#             rr,cc=int(j/(N-1)),j%(N-1)
#             if checkside(rr,cc):
#                 continue
#             arr[rr][cc]=1
#             for k in range(j,(N-1)*H-2):
#                 rrr,ccc=int(k/(N-1)),k%(N-1)
#                 if checkside(rrr,ccc):
#                     continue
#                 arr[rrr][ccc]=1
#                 if check():
#                     return 3
#                 arr[rrr][ccc]=0
#             arr[rr][cc]=0
#         arr[r][c]=0
            
#     return -1
            

# print(findanswer())




N,M,H=map(int,input().split(' '))
arr=[[0]*(N-1) for _ in range(H)]
for _ in range(M):
    a,b=map(int,input().split(' '))
    arr[a-1][b-1]=1
print(arr)

# N,M,H=5,5,6
# arr=[[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
def check():
    for c in range(N-1):
        tmp=c
        for r in range(H):
            if tmp<N-1 and arr[r][tmp]==1:
                tmp+=1
            elif tmp>0 and arr[r][tmp-1]==1:
                tmp-=1
        if c!=tmp:
            return False   
    return True

def dfs(cnt,idxfrom):
    global answer
    if cnt>3:
        answer=min(answer,1e9)
        return
    if cnt>=answer:
        return
    if check():
        answer=min(answer,cnt)
        return

    for i in range(idxfrom+1,(N-1)*H): #-(2-cnt)):
        c=i%(N-1)
        r=int(i/(N-1))
        if arr[r][c]==1:
            continue
        if c>0 and arr[r][c-1]!=0:
            continue
        if c<N-2 and arr[r][c+1]!=0:
            continue
        # print("="*2*(cnt+5), cnt, idxfrom,",,,,,,,",i)
        arr[r][c]=1
        dfs(cnt+1,i)
        arr[r][c]=0


answer=1e9
dfs(0,-1)
print(answer if answer!=1e9 else -1)