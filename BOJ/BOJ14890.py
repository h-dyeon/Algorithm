import sys

# N,L=list(map(int,sys.stdin.readline().strip().split()))
# arr=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
# print(arr)

N,L=6,2
arr=[[3,2,1,1,2,3], [3, 2, 2, 1, 2, 3], [3, 2, 2, 2, 3, 3], [3, 3, 3, 3, 3, 3], [3,3, 3, 3, 2, 2], [3,3, 3, 3, 2, 2]]
# N,L=6,1
# arr=[[3, 2, 1, 1, 2, 3], [3, 2, 2, 1, 2, 3], [3, 2, 2, 2, 3, 3], [3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 2, 2], [3, 3, 3, 3, 2, 2]]

# N,L=6,2
# arr=[[3, 3, 3, 3, 3, 3], [2, 3, 3, 3, 3, 3], [2, 2, 2, 3, 2, 3], [1, 1, 1, 2, 2, 2], [1, 1, 1, 3, 3, 1], [1, 1, 2, 3, 3, 2]]

# N,L=6,2
# arr=[[3,2,2,2,3,3], [2, 3, 3, 3, 3, 3], [2, 2, 2, 3, 2, 3], [1, 1, 1, 2, 2, 2], [1, 1, 1, 3, 3, 1], [1, 1, 2, 3, 3, 2]]

def rowCheck(r,cs,cf,step):
    cnt,num=1,arr[r][cs]
    for c in range(cs,cf,step):
        if cnt<0 and arr[r][c]-arr[r][c+step]!=0:
            return False
        elif arr[r][c]-arr[r][c+step]==0:
            cnt+=1
        elif abs(arr[r][c]-arr[r][c+step])>1:
            return False
        elif arr[r][c]-arr[r][c+step]==1: #down
            num=arr[r][c+step]
            cnt=-1*L+1
        elif arr[r][c]-arr[r][c+step]==-1: #up
            if L<=cnt:
                num=arr[r][c+step]
                cnt=1
            else:
                return False
    if cnt<0:
        return False
    return True

def colCheck(c,rs,rf,step):
    cnt,num=1,arr[rs][c]
    for r in range(rs,rf,step):
        if cnt<0 and arr[r][c]-arr[r+step][c]!=0:
            return False
        elif arr[r][c]-arr[r+step][c]==0:
            cnt+=1
        elif abs(arr[r][c]-arr[r+step][c])>1:
            return False
        elif arr[r][c]-arr[r+step][c]==1: #down
            num=arr[r+step][c]
            cnt=-1*L+1
        elif arr[r][c]-arr[r+step][c]==-1: #up
            if L<=cnt:
                num=arr[r+step][c]
                cnt=1
            else:
                return False
    if cnt<0:
        return False
    return True


answer=0
for i in range(N):
    print("-----------",i)
    print(rowCheck(i,0,N-1,1),rowCheck(i,N-1,0,-1))
    if rowCheck(i,0,N-1,1) or rowCheck(i,N-1,0,-1):
        answer+=1
    print(colCheck(i,0,N-1,1) , colCheck(i,N-1,0,-1))
    if colCheck(i,0,N-1,1) or colCheck(i,N-1,0,-1):
        answer+=1

print(answer)



# def rowCheck(r,cs,cf,step):
#     cnt,num=1,arr[r][cs]
#     for c in range(cs,cf,step):
#         if arr[r][c]-arr[r][c+step]==0:
#             cnt+=1
#             continue
#         elif abs(arr[r][c]-arr[r][c+step])>1:
#             return False
#         elif abs(arr[r][c]-arr[r][c+step])==1:
#             if L<=cnt and arr[r][c]<arr[r][c+step]:
#                 num=arr[r][c+step]
#                 cnt=1
#                 continue
#             else:
#                 return False
#     return True

# def colCheck(c,rs,rf,step):
#     cnt,num=1,arr[rs][c]
#     for r in range(rs,rf,step):
#         if arr[r][c]-arr[r+step][c]==0:
#             cnt+=1
#             continue
#         elif abs(arr[r][c]-arr[r+step][c])>1:
#             return False
#         elif abs(arr[r][c]-arr[r+step][c])==1:
#             if L<=cnt and arr[r][c]<arr[r+step][c]:
#                 num=arr[r+step][c]
#                 cnt=1
#                 continue
#             else:
#                 return False
#     return True