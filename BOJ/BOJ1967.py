import sys
from collections import deque

# N=int(input())
# linked=[{}for _ in range(N)]
# for _ in range(N-1):
#     parent, child, v = map(int,sys.stdin.readline().strip().split(' '))
#     linked[parent-1][child-1]=v
#     linked[child-1][parent-1]=v
N=12
linked=[{1: 3, 2: 2}, {0: 3, 3: 5}, {0: 2, 4: 11, 5: 9}, {1: 5, 6: 1, 7: 7}, {2: 11, 8: 15, 9: 4}, {2: 9, 10: 6, 11: 10}, {3: 1}, {3: 7}, {4: 15}, {4: 4}, {5: 6}, {5: 10}]

def far_node(start):
    dq=deque([(start,0)])
    visited=[-1 for _ in range(N)]
    visited[start]=0
    while dq:
        s,v=dq.popleft()
        for f in linked[s].keys():
            if visited[f]==-1:
                visited[f]=linked[s][f]+v
                dq.append([f,visited[f]])
    return visited.index(max(visited)), max(visited)

i,value=far_node(0)
i,value=far_node(i)
print(value)







# #220112 re! =====================recursion error
# import sys

# def findFarNode(start,weight):
#     for f in linked[start].keys():
#         if visited[f]==-1:
#             visited[f]=linked[start][f]+weight
#             findFarNode(f,visited[f])

# N=int(input())
# linked=[{}for _ in range(N)]
# for _ in range(N-1):
#     parent, child, v = map(int,sys.stdin.readline().strip().split(' '))
#     linked[parent-1][child-1]=v
#     linked[child-1][parent-1]=v

# visited=[-1 for _ in range(N)]
# visited[0]=0
# findFarNode(0,0)

# s=visited.index(max(visited))
# visited=[-1 for _ in range(N)]
# visited[s]=0
# findFarNode(s,0)

# print(max(visited))


# #220111 re! =====================over memory

# import sys
# import copy
# from collections import deque

# N=int(input())
# answer=0
# linked=[set() for _ in range(N)]
# visited=[{} for _ in range(N)]
# for _ in range(N-1):
#     parent, child, v = map(int,sys.stdin.readline().strip().split(' '))
#     # print(parent, child, v)
#     linked[child-1].add(parent-1)
#     linked[parent-1].add(child-1)
#     visited[parent-1][child-1]=v
#     visited[child-1][parent-1]=v
#     answer=max(answer,v) 

# # N=12
# # linked=[{1: 3, 2: 2}, {0: 3, 3: 5}, {0: 2, 4: 11, 5: 9}, {1: 5, 6: 1, 7: 7}, {2: 11, 8: 15, 9: 4}, {2: 9, 10: 6, 11: 10}, {3: 1}, {3: 7}, {4: 15}, {4: 4}, {5: 6}, {5: 10}]
# # visited=[{1: 3, 2: 2}, {0: 3, 3: 5}, {0: 2, 4: 11, 5: 9}, {1: 5, 6: 1, 7: 7}, {2: 11, 8: 15, 9: 4}, {2: 9, 10: 6, 11: 10}, {3: 1}, {3: 7}, {4: 15}, {4: 4}, {5: 6}, {5: 10}]
# # answer=15

# dq=deque([])
# for i in range(N):
#     if len(linked[i])==1:
#         f=list(linked[i])[0]
#         if len(linked[f])!=1:
#             dq.append([i,f]) #start, finish
# while dq:
#     s,f=dq.popleft()
#     if len(linked[f])==1:
#         answer=max(answer,visited[s][f])
#         # print(s,f,answer)
#         continue
#     for ff in list(linked[f]):
#         if ff in visited[s].keys()  or s in visited[ff].keys()  or s==ff:
#             continue
#         visited[s][ff]=visited[s][f]+visited[f][ff]
#         visited[ff][s]=visited[s][ff]
#         dq.append([s,ff])
# print(answer)









#===========================================================

# import sys
# from collections import deque

# N=12
# kkk=[[1, 2, 3], [1, 3, 2], [2, 4, 5], [3, 5, 11], [3, 6, 9], [4, 7, 1], [4, 8, 7], [5, 9, 15], [5, 10, 4], [6, 11, 6], [6, 12, 10]]

# #N=int(input())
# arr=[[]for i in range(N+1)]
# for i in range(1,N):
#     #p,c,w=map(int,sys.stdin.readline().strip().split(" "))
#     p,c,w=kkk[i-1]
#     arr[p].append([c,w])
#     arr[c].append([p,w])

# def far_node(start):
#     print("in start=",start,"\tchilds=",arr[start])
#     queue=deque([(start,0)])
#     visited=[0]*(N+1)
#     visited[start]=1
#     farr=[start, 0] # node idx, node distance
#     while queue:
#         c,w=queue.popleft()
#         print("c=",c,"w=",w,"\tchilds=",arr[c])
#         for newc,neww in arr[c]:
#             if visited[newc]!=1:
#                 if len(arr[newc])!=1:
#                     queue.append((newc,neww+w))
#                 visited[newc]=1
#                 if farr[1]<neww+w:
#                     farr=[newc, neww+w]
#         print("c=",c,"w=",w,"\tqueues=",queue)
#     return farr

# n,d=far_node(1)
# print("----------------------")
# nn,dd=far_node(n)
# print(dd)










# #=============시간초과==================
# # import sys

# # # N=int(sys.stdin.readline().strip())
# # # arr=[list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N-1)]
# # N=12
# # arr=[[1, 2, 3], [1, 3, 2], [2, 4, 5], [3, 5, 11], [3, 6, 9], [4, 7, 1], [4, 8, 7], [5, 9, 15], [5, 10, 4], [6, 11, 6], [6, 12, 10]]

# # pos=[-1]*10001
# # savem=[0]*10001

# # for i in range(N-1):
# #     if pos[arr[i][0]]==-1:
# #         pos[arr[i][0]]=i

# # def getmax(parent):
# #     global maxanswer
# #     print("parent=",parent,"\tin")
# #     # if pos[parent]==-1:
# #     #     return
# #     max_twochild=[]
# #     for i in range(pos[parent],N-1):
# #         if arr[i][0]>parent:
# #             break
# #         if arr[i][0]==parent:
# #             if pos[parent]!=-1:
# #                 getmax(arr[i][1])
# #             max_twochild.append(arr[i][2]+savem[arr[i][1]])

# #     max_twochild.sort(reverse=True)
# #     print("parent=",parent,"\tmax_twochild=",max_twochild)
# #     if len(max_twochild)==1:
# #         savem[parent]=max(savem[parent],max_twochild[0])
# #     elif len(max_twochild)>1:
# #         maxanswer=max(maxanswer, max_twochild[0]+max_twochild[1])
# #         savem[parent]=max(savem[parent],max_twochild[0])
# #     print("parent=",parent,"\tout return 0")
# #     return 

# # maxanswer=0
# # getmax(1)
# # print(maxanswer)

