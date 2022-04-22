from collections import deque
blank=-2

def rotate():
    tmp=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[N-j-1][i]=arr[i][j]
    return tmp

def earth():
    tmp=[[-1 if arr[i][j]==-1 else blank for j in range(N)] for i in range(N)]
    for c in range(N):
        i, j = N - 1, N - 1
        while i>=0:
            if arr[i][c]==blank:
                i-=1
            elif arr[i][c]==-1:
                i-=1
                j=i
            else:
                tmp[j][c]=arr[i][c]
                i-=1
                j-=1
    return tmp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N, M = map(int, input().split(' '))
    arr=[list(map(int,input().split(' '))) for _ in range(N)]
    answer=0
    direc=[(0,1),(0,-1),(1,0),(-1,0)]

    while True:
        groups=[]
        # find group
        all_visited=visited=[[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if arr[i][j] in [-1,blank,0] or all_visited[i][j]==1:
                    continue
                status=False
                nowcolor=arr[i][j]
                if j+1<N and (arr[i][j+1] in [nowcolor,0]):
                    status=True
                if i+1<N and (arr[i+1][j] in [nowcolor,0]):
                    status = True
                if j-1>=0 and (arr[i][j-1] in [nowcolor,0]):
                    status = True
                if i-1>=0 and (arr[i-1][j] in [nowcolor,0]):
                    status = True

                if status:
                    all_visited[i][j]=1
                    R_,C_=i,j
                    allSize=1
                    rainbow=0
                    visited=[[0]*N for _ in range(N)]
                    dq=deque([(i,j)])
                    visited[i][j]=1
                    while dq:
                        r,c=dq.popleft()
                        for dr,dc in direc:
                            nr,nc=r+dr,c+dc
                            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and (arr[nr][nc] in [0,nowcolor]):
                                visited[nr][nc]=1
                                dq.append((nr,nc))
                                allSize+=1
                                if arr[nr][nc]==0:
                                    rainbow += 1
                                else:
                                    all_visited[nr][nc]=1
                                    if R_>i or (R_==i and C_>j):
                                        R_,C_=i,j

                    groups.append((allSize,rainbow,R_,C_))
        if len(groups)==0:
            break

        # remove group

        groups=sorted(groups,key=lambda x: (-x[0],-x[1],-x[2],-x[3]))

        s,no,R,C=groups[0] # first group
        dq=deque([(R,C)])
        nowcolor=arr[R][C]
        arr[R][C] = blank
        while dq:
            r,c=dq.popleft()
            for dr,dc in direc:
                nr,nc=r+dr,c+dc
                if 0<=nr<N and 0<=nc<N and (arr[nr][nc] in [nowcolor,0]):
                    dq.append((nr,nc))
                    arr[nr][nc]=blank
        answer+=s**2

        # earth
        arr=earth()
        # rotate
        arr=rotate()
        # earth
        arr = earth()

    print(answer)








# from collections import deque
# N,M=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]

# # N,M=4,2
# # arr=[[1,2,0,1],[0,-1,-1,-1],[1,0,-1,1],[2,0,0,-1]]

# # N=3
# # M=9
# # arr=[[1,2,3],[0,5,6],[-1,8,9]]
# blank=-3

# def findgroup():
#     grouplist=[] #(size,rainbow,row,col)
#     visited=[[0]*N for _ in range(N)]
#     v=0

#     for i in range(N):
#         for j in range(N):
#             if visited[i][j]!=0 or (arr[i][j] in [blank,0,-1]):
#                 continue
#             status=False
#             for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
#                 i_,j_=i+dr,j+dc
#                 if 0<=i_<N and 0<=j_<N and (arr[i_][j_]==arr[i][j] or arr[i_][j_]==0):
#                     status=True
#                     break

#             # if i<N-1 and (arr[i][j]==arr[i+1][j] or arr[i+1][j]==0):
#             #     status=True
#             # if i==N-1 and (0<arr[i][j]<=M and arr[i-1][j]==0):
#             #     status=True
#             # if j<N-1 and (arr[i][j]==arr[i][j+1] or arr[i][j+1]==0):
#             #     status=True
#             # if j==N-1 and (0<arr[i][j]<=M and arr[i][j-1]==0):
#             #     status=True

#             if status:
#                 v+=1
#                 # find group
#                 cnt,rainbow,R,C=1,0,i,j
#                 dq=deque([(i,j)])
#                 visited[i][j]=v
#                 while dq:
#                     r,c=dq.popleft()
#                     for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
#                         nr,nc=r+dr,c+dc
#                         if 0<=nr<N and 0<=nc<N:
#                             if (visited[nr][nc]==0 and arr[nr][nc]==arr[i][j]) or (visited[nr][nc]!=v and arr[nr][nc]==0):
#                                 visited[nr][nc]=v
#                                 dq.append((nr,nc))
#                                 cnt+=1
#                                 if arr[nr][nc]==0:
#                                     rainbow+=1
#                                 if arr[nr][nc]!=0:
#                                     if R>nr or (R==nr and C>nc):
#                                         R,C=nr,nc
#                 grouplist.append((cnt,rainbow,R,C))

#     if len(grouplist)==0:
#         return -1,-1,-1
#     else:
#         grouplist=sorted(grouplist,key=lambda x:(-x[0],-x[1],-x[2],-x[3]))
#         return grouplist[0][2],grouplist[0][3],grouplist[0][0]    

# def deletegroup(R,C):
#     global arr
#     dq=deque([(R,C)])
#     color=arr[R][C]
#     arr[R][C]=blank
#     cnt=1
#     while dq:
#         r,c=dq.popleft()
#         for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
#             nr,nc=r+dr,c+dc
#             if 0<=nr<N and 0<=nc<N and (arr[nr][nc]==0 or arr[nr][nc]==color):
#                 arr[nr][nc]=blank
#                 dq.append((nr,nc))
#                 cnt+=1
#     return cnt

# def earth():
#     tmp=[[0]*N for _ in range(N)]
#     for c in range(N):
#         j=N-1
#         for i in range(N-1,-1,-1):
#             if arr[i][c]==-1:
#                 tmp[i][c]=-1
#                 j=i-1
#             elif arr[i][c]==0:
#                 tmp[j][c]=1e9
#                 j-=1
#             elif 0<arr[i][c]<=M:
#                 tmp[j][c]=arr[i][c]
#                 j-=1
#     for i in range(N):
#         for j in range(N):
#             if tmp[i][j]==1e9:
#                 tmp[i][j]=0
#             elif tmp[i][j]==0:
#                 tmp[i][j]=blank
#     return tmp

# def rotate():
#     tmp=[[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             tmp[N-j-1][i]=arr[i][j]
#     return tmp


# answer=0
# while True:
#     r,c,tmp=findgroup()
#     print(tmp)
#     if r==-1: # no group
#         break
#     answer+=deletegroup(r,c)**2
#     arr=earth()
#     arr=rotate()
#     arr=earth()
# print(answer)
