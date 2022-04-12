##############################22.04.12
b=[]

a=[1 for _ in range(3)]
b+=a

N,M,K=map(int,input().split(' '))
arr=[list(map(int,input().split(' '))) for _ in range(N)]
trees={}
for _ in range(M):
    x,y,z=map(int,input().split(' '))
    trees.setdefault((x-1,y-1),[]).append(z)
print(trees)

# N,M,K=5,2,1
# trees={(1, 0): [3], (2, 1): [3]}
# arr=[[2, 3, 2, 3, 2], [2, 3, 2, 3, 2], [2, 3, 2, 3, 2], [2, 3, 2, 3, 2], [2, 3, 2, 3, 2]]



direc=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

ground=[[5]*N for _ in range(N)]
for _ in range(K):
    age5={}

    # spring & summer
    deletelist=set()
    for (x,y),tree in trees.items():
        treelist=sorted(tree)
        bob=0
        ntree=[]
        for t in treelist:
            if ground[x][y]>=t:
                ground[x][y]-=t
                ntree.append(t+1)
                if (t+1)%5==0:
                    age5.setdefault((x,y),0)
                    age5[(x,y)]+=1
            else:
                bob+=int(t/2)
        
        if len(ntree)==0:
            deletelist.add((x,y))
        trees[(x,y)]=ntree
        ground[x][y]+=bob

    for x,y in deletelist:
        del trees[(x,y)]

    # fall
    for x,y in age5.keys():
        cnt=age5[(x,y)]
        for dx,dy in direc:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                a=[1 for _ in range(cnt)]
                trees.setdefault((nx,ny),[])
                trees[(nx,ny)]+=a
                    

    # winter
    ground=[[ground[i][j]+arr[i][j] for j in range(N)] for i in range(N)]
    

answer=0
for (x,y),tree in trees.items():
    answer+=len(tree)
print(answer)









######################################
# from collections import deque

# N,M,K=map(int,input().split(' '))
# arr=[list(map(int,input().split(' '))) for _ in range(N)]

# trees=[[[0]*(K+11) for _ in range(N)] for _ in range(N)] # [r,c,age]
# for _ in range(M):
#     x,y,z=map(int,input().split(' '))
#     trees[x-1][y-1][z]+=1

# matrix=[[5]*N for _ in range(N)]
# for year in range(0,K):
#     killtree=deque([])
#     # spring
#     for r in range(N):
#         for c in range(N):
#             die=False
#             for age in range(K+11):
#                 if trees[r][c][age]==0:
#                     continue
#                 numtree=trees[r][c][age]
#                 if die==False:
#                     permitNum=0
#                     for i in range(numtree+1):
#                         permitNum=i
#                         if age*(i+1)>matrix[r][c]:
#                             break
#                     matrix[r][c]-=(age*permitNum) # eat
#                     if numtree>permitNum:
#                         die=True
#                         trees[r][c][age]-=(numtree-permitNum) # kill tree
#                         killtree.append((r,c,age,numtree-permitNum)) 
#                 if die==True:
#                     trees[r][c][age]=0   
#                     killtree.append((r,c,age,numtree)) 
#             for age in range(K+10,-1,-1):
#                 if trees[r][c][age]==0:
#                     continue
#                 trees[r][c][age+1]+=trees[r][c][age]
#                 trees[r][c][age]=0
#     # summer
#     for x,y,age,numtree in killtree:
#         matrix[x][y]+=int(age/2)*numtree
#     # fall
#     for r in range(N):
#         for c in range(N):
#             for age in range(5,K+11,5):
#                 for dr,dc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,+1),(1,-1),(1,0),(1,1)]:
#                     nr,nc=r+dr,c+dc
#                     if 0<=nr<N and 0<=nc<N:
#                         trees[nr][nc][1]+=trees[r][c][age]

#     # winter
#     matrix=[[matrix[i][j]+arr[i][j] for j in range(N)] for i in range(N)]

# answer=0
# for r in range(N):
#     for c in range(N):
#         for age in range(K+11):
#             answer+=trees[r][c][age]
# print(answer)

# # from collections import deque
# # N,M,K=map(int,input().split(' '))
# # arr=[list(map(int,input().split(' '))) for _ in range(N)]

# # trees={}
# # for _ in range(M):
# #     x,y,z=map(int,input().split(' '))
# #     if (x-1,y-1) not in trees:
# #         trees[(x-1,y-1)]={z:1}
# #     else:
# #         if z not in trees[(x-1,y-1)]:
# #             trees[(x-1,y-1)][z]=1
# #         else:
# #             trees[(x-1,y-1)][z]+=1

# # matrix=[[5]*N for _ in range(N)]

# # for year in range(0,K):
# #     killtree=deque([])
# #     # spring
# #     treepositionlist=[t for t in trees.keys()]
# #     for x,y in treepositionlist:
# #         agelist=sorted(trees[(x,y)].keys())
# #         die=False
# #         for age in agelist:
# #             numtree=trees[(x,y)][age]
# #             if die==False:
# #                 permitNum=0
# #                 for i in range(numtree+1):
# #                     permitNum=i
# #                     if age*(i+1)>matrix[x][y]:
# #                         break
# #                 matrix[x][y]-=(age*permitNum) # eat
# #                 if numtree>permitNum:
# #                     die=True
# #                     trees[(x,y)][age]-=(numtree-permitNum) # kill tree
# #                     killtree.append((x,y,age,numtree-permitNum)) 
# #             if die==True:
# #                 trees[(x,y)][age]=0   
# #                 killtree.append((x,y,age,numtree)) 

# #         agelist.sort(reverse=True)
# #         for age in agelist: # add age
# #             numtree=trees[(x,y)][age]
# #             if numtree!=0:
# #                 if age+1 in trees[(x,y)]:
# #                     trees[(x,y)][age+1]+=numtree
# #                 else:
# #                     trees[(x,y)][age+1]=numtree
# #             del trees[(x,y)][age]
# #         if len(trees[(x,y)].keys())==0:
# #             del trees[(x,y)]
# #     # summer
# #     for x,y,age,numtree in killtree:
# #         matrix[x][y]+=int(age/2)*numtree

# #     # fall
# #     treepositionlist=[t for t in trees.keys()]
# #     for x,y in treepositionlist:
# #         for age in trees[(x,y)]:
# #             if age%5!=0:
# #                 continue

# #             numtree=trees[(x,y)][age]
# #             for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,+1),(1,-1),(1,0),(1,1)]:
# #                 nx,ny=x+dx,y+dy
# #                 if 0<=nx<N and 0<=ny<N:
# #                     if (nx,ny) in trees.keys():
# #                         if 1 in trees[(nx,ny)]:
# #                             trees[(nx,ny)][1]+=numtree
# #                         else:
# #                             trees[(nx,ny)][1]=numtree
# #                     else:
# #                         trees[(nx,ny)]={1:numtree}
# #     # winter
# #     matrix=[[matrix[i][j]+arr[i][j] for j in range(N)] for i in range(N)]

# # answer=0
# # for x,y in trees.keys():
# #     for age in trees[(x,y)].keys():
# #         answer+=trees[(x,y)][age]
# # print(answer)
