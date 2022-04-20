
###############################################22.04.17
from collections import deque
N,M=map(int,input().split(' '))
arr=[input() for _ in range(N)]
red=[-1,-1]
blue=[-1,-1]
hole=[-1,-1]
large=max(N,M)
for i in range(N):
    for j in range(M):
        if arr[i][j]=='R':
            red=[i,j]
            # arr[i][j]='.'
        if arr[i][j]=='B':
            blue=[i,j]
            # arr[i][j]='.'
        if arr[i][j]=='O':
            hole=[i,j]
direc=[(1,0),(-1,0),(0,1),(0,-1)]

def solve():
    visited=[[[[-1]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[red[0]][red[1]][blue[0]][blue[1]]=0
    dq=deque([(red[0],red[1],blue[0],blue[1])])
    while dq:
        R_r,R_c,B_r,B_c=dq.popleft()
        before=visited[R_r][R_c][B_r][B_c]
        if before==10:
            return -1
        for dd in range(4):
            dr,dc =direc[dd]
            red_r,red_c=R_r,R_c
            blue_r,blue_c=B_r,B_c
            for _ in range(1,large):                
                if arr[red_r+dr][red_c+dc]=='#':
                    break
                red_r,red_c=red_r+dr, red_c+dc
                if arr[red_r][red_c]=='O':
                    break
                
            for _ in range(1,large):
                if arr[blue_r+dr][blue_c+dc]=='#':
                    break
                blue_r,blue_c=blue_r+dr, blue_c+dc
                if arr[blue_r][blue_c]=='O':
                    break
            if [blue_r,blue_c]!=hole:  
                if [red_r,red_c]==hole :
                    return before+1

                if red_r==blue_r and red_c==blue_c:
                    who=-1 # 1=red, 2=blue
                    if dd==0:
                        if R_r <B_r: who=1
                        else: who=2                        
                    elif dd==1:
                        if R_r >B_r: who=1
                        else: who=2  
                    elif dd==2:
                        if R_c <B_c: who=1
                        else: who=2  
                    elif dd==3:
                        if R_c >B_c: who=1
                        else: who=2  
                    if who==1:
                        red_r-=dr
                        red_c-=dc
                    elif who==2:
                        blue_r-=dr
                        blue_c-=dc
            
                if visited[red_r][red_c][blue_r][blue_c]==-1:
                    visited[red_r][red_c][blue_r][blue_c]=before+1
                    dq.append((red_r,red_c,blue_r,blue_c))     
    return -1

print(solve())




















###############################################333
# import sys
# from collections import deque
# import copy

# # N,M=7,7
# # Mmatrix=[['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', 'R', 'B', '#'], ['#', '.', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '.', '#'], ['#', 'O', '.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]

# N,M=map(int,sys.stdin.readline().strip().split(' '))
# matrix=[['']*M for _ in range(N)]
# Red=[-1,-1]
# Blue=[-1,-1]
# for i in range(N):
#     ss=sys.stdin.readline().strip() 
#     for j in range(M):
#         matrix[i][j]=ss[j]
#         if matrix[i][j]=='R': Red=[i,j]
#         elif matrix[i][j]=='B': Blue=[i,j]
# direc=[(0,-1,M),(0,1,M),(1,0,N),(-1,0,N)]

# def move(x,y,dx,dy):
#     cnt=0
#     nx,ny=x,y
#     while matrix[nx+dx][ny+dy]!='#' and matrix[nx][ny]!='O':
#         nx+=dx
#         ny+=dy
#         cnt+=1
#     return nx,ny,cnt

# def solve():
#     visited=[[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)] #[R_x][R_y][B_x][B_y][direction]
#     visited[Red[0]][Red[1]][Blue[0]][Blue[1]]=True
#     dq=deque([(Red[0],Red[1],Blue[0],Blue[1],0)])
#     while dq:
#         Rr,Rc,Br,Bc,count=dq.popleft()
#         if count+1>10:
#             break
#         for dr,dc in [(0,-1),(0,1),(1,0),(-1,0)]:
#             TRr,TRc,Rcnt=move(Rr,Rc,dr,dc)
#             TBr,TBc,Bcnt=move(Br,Bc,dr,dc)
#             if matrix[TBr][TBc]!='O':
#                 if matrix[TRr][TRc]=='O':
#                     print(count+1)
#                     return
#                 if TRr==TBr and TRc==TBc:
#                     if Rcnt>Bcnt:
#                         TRr-=dr
#                         TRc-=dc
#                     else:
#                         TBr-=dr
#                         TBc-=dc
#                 if not visited[TRr][TRc][TBr][TBc]:
#                     visited[TRr][TRc][TBr][TBc]=True
#                     dq.append((TRr,TRc,TBr,TBc,count+1))
#     print(-1)        


# solve()




# # import sys
# # from collections import deque
# # import copy

# # # N,M=7,7
# # # Mmatrix=[['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', 'R', 'B', '#'], ['#', '.', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '.', '#'], ['#', 'O', '.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]

# # N,M=map(int,sys.stdin.readline().strip().split(' '))
# # Mmatrix=[['']*M for _ in range(N)]
# # Red=[-1,-1]
# # Blue=[-1,-1]
# # for i in range(N):
# #     ss=sys.stdin.readline().strip() 
# #     for j in range(M):
# #         Mmatrix[i][j]=ss[j]
# #         if Mmatrix[i][j]=='R': Red=[i,j]
# #         elif Mmatrix[i][j]=='B': Blue=[i,j]


# # visited=[[[[1e9 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)] #[R_x][R_y][B_x][B_y][direction]
# # visited[Red[0]][Red[1]][Blue[0]][Blue[1]]=0

# # direc=[(0,-1,M),(0,1,M),(1,0,N),(-1,0,N)]

# # def dfs(OriginMatrix,Rr,Rc,Br,Bc,count):
# #     answer=1e9
# #     for k in range(4):
# #         dr,dc,NN=direc[k]
# #         matrix=copy.deepcopy(OriginMatrix)
# #         TRr,TRc,TBr,TBc=Rr,Rc,Br,Bc
# #         for nn in range(NN):
# #             NRr=TRr+dr
# #             NRc=TRc+dc
# #             NBr=TBr+dr
# #             NBc=TBc+dc

# #             if matrix[NRr][NRc]=='O': # red is in hole
# #                 if not((NRr-NBr)==dr or (NRc-NBc)==dc): # not in same direction and same line
# #                     answer=min(answer,count+1)
# #                 break
# #             if  matrix[NBr][NBc]=='O': # blue is in hole
# #                 break
# #             if (matrix[NRr][NRc]!='.' and matrix[NBr][NBc]!='.'): # block!
# #                 if count+1<min(answer,10) and count+1 <= visited[TRr][TRc][TBr][TBc]:
# #                     if (NRr,NRc)!=(Rr,Rc) and (NBr,NBc)!=(Br,Bc): # must move more than once
# #                         back=visited[TRr][TRc][TBr][TBc]
# #                         visited[TRr][TRc][TBr][TBc]=count+1
# #                         dfs(matrix,TRr,TRc,TBr,TBc,count+1)
# #                         visited[TRr][TRc][TBr][TBc]=back
# #                 break
            


# #             if matrix[NRr][NRc]!='#' and matrix[NBr][NBc]!='#':
# #                 matrix[TRr][TRc]='.'
# #                 matrix[TBr][TBc]='.'
# #                 matrix[NRr][NRc]='R'
# #                 matrix[NBr][NBc]='B'
# #                 TRr,TRc=NRr,NRc
# #                 TBr,TBc=NBr,NBc
# #             elif matrix[NRr][NRc]!='#':
# #                 matrix[NRr][NRc]='R'
# #                 matrix[TRr][TRc]='.'
# #                 TRr,TRc=NRr,NRc
# #             elif matrix[NBr][NBc]!='#':
# #                 matrix[NBr][NBc]='B'
# #                 matrix[TBr][TBc]='.'
# #                 TBr,TBc=NBr,NBc
# #             visited[TRr][TRc][TBr][TBc]=count+1


# # answer=dfs(Mmatrix,Red[0],Red[1],Blue[0],Blue[1],0)
           

# # if answer==1e9:
# #     print(-1)
# # else:
# #     print(answer)

# # # while dq:
# # #     Rr,Rc,Br,Bc,count=dq.popleft()
# # #     for k in range(4):
# # #         dr,dc,NN=direc[k]
# # #         TRr,TRc,TBr,TBc=Rr,Rc,Br,Bc
# # #         for nn in range(NN):
# # #             NRr=TRr+dr
# # #             NRc=TRc+dc
# # #             NBr=TBr+dr
# # #             NBc=TBc+dc

# # #             if matrix[NRr][NRc]=='O': # red is in hole
# # #                 if not((NRr-NBr)==dr or (NRc-NBc)==dc): # not in same direction and same line
# # #                     answer=min(answer,count+1)
# # #                 break
# # #             if  matrix[NBr][NBc]=='O': # blue is in hole
# # #                 break
# # #             if (matrix[NRr][NRc]!='.' and matrix[NBr][NBc]!='.'): # block!
# # #                 if count+1<min(answer,10) and count+1 < visited[TRr][TRc][TBr][TBc][k]:
# # #                     if (NRr,NRc)!=(Rr,Rc) and (NBr,NBc)!=(Br,Bc): # must move more than once
# # #                         visited[TRr][TRc][TBr][TBc][k]=count+1
# # #                         dq.append(TRr,TRc,TBr,TBc,count+1)
# # #                 break
            
# # #             if matrix[NRr][NRc]!='#':
# # #                 TRr,TRc=NRr,NRc
# # #             if matrix[NBr][NBc]!='#':
# # #                 TBr,TBc=NBr,NBc