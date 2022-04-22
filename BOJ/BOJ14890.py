########## 22.04.22
def check(tmp):
    num=1
    for i in range(N-1):
        if abs(tmp[i]-tmp[i+1])>1:
            return False
        if num<0 and tmp[i] != tmp[i + 1]:
            return False
        if tmp[i] < tmp[i + 1] :
            if num < L:
                return False
            num=1
        elif tmp[i] == tmp[i + 1]:
            num+=1
        else:
            num=-1*L+1
    if num<0:
        return False
    return True

if __name__ == '__main__':
    N,L=map(int,input().split(' '))
    arr=[list(map(int,input().split(' '))) for _ in range(N)]
    answer=0
    for i in range(N):
        if check(arr[i]):
            answer+=1
        t=[0 for _ in range(N)]
        for j in range(N):
            t[j]=arr[j][i]
        if check(t):
            answer+=1
    print(answer)




########## 22.04.06
# N,L=list(map(int,input().split(' ')))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
# print(arr)

# def rowcheck(r):
#     cnt=1
#     for i in range(N-1):
#         if arr[r][i]==arr[r][i+1]:
#             cnt+=1
#         elif cnt<0:
#             return 0
#         elif abs(arr[r][i]-arr[r][i+1])>1:
#             return 0
#         elif arr[r][i]>arr[r][i+1]:
#             cnt=-1*L+1        
#         else:
#             if cnt>=L:
#                 cnt=1
#             else:
#                 return 0
#     if cnt<0:
#         return 0
#     return 1


# def colcheck(c):
#     cnt=1
#     for i in range(N-1):
#         if arr[i][c]==arr[i+1][c]:
#             cnt+=1
#         elif cnt<0:
#             return 0
#         elif abs(arr[i][c]-arr[i+1][c])>1:
#             return 0
#         elif arr[i][c]>arr[i+1][c]:
#             cnt=-1*L+1        
#         else:
#             if cnt>=L:
#                 cnt=1
#             else:
#                 return 0
#     if cnt<0:
#         return 0
#     return 1


# answer=0
# for i in range(N):
#     answer+=rowcheck(i)
#     answer+=colcheck(i)
# print(answer)





###############22.03.26########
# import sys

# # N,L=list(map(int,sys.stdin.readline().strip().split()))
# # arr=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
# # print(arr)

# N,L=6,2
# arr=[[3,2,1,1,2,3], [3, 2, 2, 1, 2, 3], [3, 2, 2, 2, 3, 3], [3, 3, 3, 3, 3, 3], [3,3, 3, 3, 2, 2], [3,3, 3, 3, 2, 2]]
# # N,L=6,1
# # arr=[[3, 2, 1, 1, 2, 3], [3, 2, 2, 1, 2, 3], [3, 2, 2, 2, 3, 3], [3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 2, 2], [3, 3, 3, 3, 2, 2]]

# # N,L=6,2
# # arr=[[3, 3, 3, 3, 3, 3], [2, 3, 3, 3, 3, 3], [2, 2, 2, 3, 2, 3], [1, 1, 1, 2, 2, 2], [1, 1, 1, 3, 3, 1], [1, 1, 2, 3, 3, 2]]

# # N,L=6,2
# # arr=[[3,2,2,2,3,3], [2, 3, 3, 3, 3, 3], [2, 2, 2, 3, 2, 3], [1, 1, 1, 2, 2, 2], [1, 1, 1, 3, 3, 1], [1, 1, 2, 3, 3, 2]]

# def rowCheck(r,cs,cf,step):
#     cnt,num=1,arr[r][cs]
#     for c in range(cs,cf,step):
#         if cnt<0 and arr[r][c]-arr[r][c+step]!=0:
#             return False
#         elif arr[r][c]-arr[r][c+step]==0:
#             cnt+=1
#         elif abs(arr[r][c]-arr[r][c+step])>1:
#             return False
#         elif arr[r][c]-arr[r][c+step]==1: #down
#             num=arr[r][c+step]
#             cnt=-1*L+1
#         elif arr[r][c]-arr[r][c+step]==-1: #up
#             if L<=cnt:
#                 num=arr[r][c+step]
#                 cnt=1
#             else:
#                 return False
#     if cnt<0:
#         return False
#     return True

# def colCheck(c,rs,rf,step):
#     cnt,num=1,arr[rs][c]
#     for r in range(rs,rf,step):
#         if cnt<0 and arr[r][c]-arr[r+step][c]!=0:
#             return False
#         elif arr[r][c]-arr[r+step][c]==0:
#             cnt+=1
#         elif abs(arr[r][c]-arr[r+step][c])>1:
#             return False
#         elif arr[r][c]-arr[r+step][c]==1: #down
#             num=arr[r+step][c]
#             cnt=-1*L+1
#         elif arr[r][c]-arr[r+step][c]==-1: #up
#             if L<=cnt:
#                 num=arr[r+step][c]
#                 cnt=1
#             else:
#                 return False
#     if cnt<0:
#         return False
#     return True


# answer=0
# for i in range(N):
#     print("-----------",i)
#     print(rowCheck(i,0,N-1,1),rowCheck(i,N-1,0,-1))
#     if rowCheck(i,0,N-1,1) or rowCheck(i,N-1,0,-1):
#         answer+=1
#     print(colCheck(i,0,N-1,1) , colCheck(i,N-1,0,-1))
#     if colCheck(i,0,N-1,1) or colCheck(i,N-1,0,-1):
#         answer+=1

# print(answer)



# # def rowCheck(r,cs,cf,step):
# #     cnt,num=1,arr[r][cs]
# #     for c in range(cs,cf,step):
# #         if arr[r][c]-arr[r][c+step]==0:
# #             cnt+=1
# #             continue
# #         elif abs(arr[r][c]-arr[r][c+step])>1:
# #             return False
# #         elif abs(arr[r][c]-arr[r][c+step])==1:
# #             if L<=cnt and arr[r][c]<arr[r][c+step]:
# #                 num=arr[r][c+step]
# #                 cnt=1
# #                 continue
# #             else:
# #                 return False
# #     return True

# # def colCheck(c,rs,rf,step):
# #     cnt,num=1,arr[rs][c]
# #     for r in range(rs,rf,step):
# #         if arr[r][c]-arr[r+step][c]==0:
# #             cnt+=1
# #             continue
# #         elif abs(arr[r][c]-arr[r+step][c])>1:
# #             return False
# #         elif abs(arr[r][c]-arr[r+step][c])==1:
# #             if L<=cnt and arr[r][c]<arr[r+step][c]:
# #                 num=arr[r+step][c]
# #                 cnt=1
# #                 continue
# #             else:
# #                 return False
# #     return True