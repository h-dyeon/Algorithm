# ##################################################22.04.22
direc=[(0,1),(1,0),(0,-1),(-1,0)]

def see_range(type,R_,C_):
    tmp=set()
    for t in type:
        r,c=R_,C_
        while True:
            nr,nc=r+direc[t][0],c+direc[t][1]
            if 0>nr or nr>=N or 0>nc or nc>=M or arr[nr][nc]==6: # wall
                break
            tmp.add((nr,nc))
            r,c=nr,nc
    return tmp

def get_cctv_see():
    cctv_see_tmp=[]
    for type in range(1,6):
        for r,c in cctv_pos[type]:
            tmp=[]
            if type==1:
                for k in range(4):
                    t=see_range([k],r,c)
                    tmp.append(t)
            elif type==2:
                a=see_range([0,2],r,c)
                b=see_range([1,3],r,c)
                tmp.append(a)
                tmp.append(b)
            elif type==3:
                for k in range(4):
                    a=see_range([k,(k+1)%4],r,c)
                    tmp.append(a)
            elif type==4:
                for k in range(4):
                    a=see_range([k,(k+1)%4,(k+2)%4],r,c)
                    tmp.append(a)
            elif type==5:
                a=see_range([0,1,2,3],r,c)
                tmp.append(a)
            cctv_see_tmp.append(tmp)
    return cctv_see_tmp

def dfs(idx,nowset):
    global answer, cctv_see
    if idx==cctv_num:
        a=blank_area-nowset
        answer=min(answer,len(a))
        return

    for newset in cctv_see[idx]:
        dfs(idx+1,newset | nowset)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N,M=map(int,input().split(' '))
    arr=[list(map(int,input().split(' '))) for _ in range(N)]
    cctv_pos=[[] for _ in range(6)]
    cctv_num=0
    blank_area=set()
    for i in range(N):
        for j in range(M):
            if 1<=arr[i][j]<=5:
                cctv_pos[arr[i][j]].append((i,j))
                cctv_num+=1
                arr[i][j]=-1
            elif arr[i][j]==0:
                blank_area.add((i,j))

    cctv_see=get_cctv_see()

    answer=1e9
    dfs(0,set())

    print(answer)


# ##################################################22.04.06

# N,M=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]

# cctv=[]
# for i in range(N):
#     for j in range(M):
#         if 1<=arr[i][j]<=5:
#             cctv.append((i,j))

# dr=[0,1,0,-1]
# dc=[1,0,-1,0]
# cctvDirec=[[],[[0],[1],[2],[3]],
#         [[0,2],[1,3]],
#         [[0,1],[1,2],[2,3],[3,0]],
#         [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
#         [[0,1,2,3]]]
# answer=sum([r.count(0) for r in arr])

# def check(matrix,d,r,c):
#     while True:
#         nr,nc=r+dr[d],c+dc[d]
#         if 0>nr or 0>nc or N<=nr or M<=nc or matrix[nr][nc]==6:
#             break
#         matrix[nr][nc]=-1
#         r,c=nr,nc
#     return


# def dfs(cnt,narr):
#     global answer
#     if cnt==len(cctv):
#         answer=min(answer,sum([r.count(0) for r in narr]))
#         return
    
#     r,c=cctv[cnt]
#     ttype=arr[r][c]
#     directions=cctvDirec[ttype]
#     for a in directions:
#         matrix=[row[:] for row in narr]
#         for b in a:
#             check(matrix,b,r,c)
#         dfs(cnt+1,matrix)

# dfs(0,arr)
# print(answer)





# ##################################################3
# # import sys


# # N,M=map(int,input().split(' '))
# # arr=[list(map(int,input().split(' '))) for _ in range(N)]
# # print(arr)

# # # N,M=4,6
# # # arr=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 6, 0], [0, 0, 0, 0, 0, 0]]
# # dr=[1,0,-1,0]
# # dc=[0,1,0,-1]
# # answer=100000000000 #min

# # #find cctv
# # cctv=[]
# # for i in range(N):
# #     for j in range(M):
# #         if 0<arr[i][j]<6:
# #             cctv.append((i,j,arr[i][j]))

# # def going(copyarr,direc,r,c):
# #     for k in range(1,1000):
# #         nr=r+k*dr[direc]
# #         nc=c+k*dc[direc]
# #         if 0<=nr<N and 0<=nc<M and copyarr[nr][nc]!=6:
# #             copyarr[nr][nc]=99
# #         else:
# #             break
# #     return copyarr


# # def check(copyarr,idx):
# #     global answer
# #     tmp=sum([copyarr[i].count(0) for i in range(N)])
# #     if tmp==0 or len(cctv)==idx:  
# #         answer=min(answer,tmp)
# #         return

# #     r,c,t=cctv[idx]
    
# #     if t==1:
# #         for d in range(4):
# #             narr=[r[:] for r in copyarr]
# #             check(going(narr,d,r,c),idx+1)
# #     elif t==2:
# #         for i in range(2):
# #             narr=[r[:] for r in copyarr]
# #             going(narr,i,r,c)
# #             going(narr,i+2,r,c)
# #             check(narr,idx+1)
# #     elif t==3:
# #         for i in range(4):
# #             narr=[r[:] for r in copyarr]
# #             going(narr,i,r,c)
# #             going(narr,(i+1)%4,r,c)
# #             check(narr,idx+1)
# #     elif t==4:
# #         for i in range(4):
# #             narr=[r[:] for r in copyarr]
# #             going(narr,i,r,c)
# #             going(narr,(i+1)%4,r,c)
# #             going(narr,(i+2)%4,r,c)
# #             check(narr,idx+1)
# #     elif t==5:
# #         narr=[r[:] for r in copyarr]
# #         for d in range(4):
# #             going(narr,d,r,c)
# #         check(narr,idx+1)

# # copyarr=[r[:] for r in arr]
# # check(copyarr,0)
# # print(answer)