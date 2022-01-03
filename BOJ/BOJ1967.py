import sys
from collections import deque

N=12
kkk=[[1, 2, 3], [1, 3, 2], [2, 4, 5], [3, 5, 11], [3, 6, 9], [4, 7, 1], [4, 8, 7], [5, 9, 15], [5, 10, 4], [6, 11, 6], [6, 12, 10]]

#N=int(input())
arr=[[]for i in range(N+1)]
for i in range(1,N):
    #p,c,w=map(int,sys.stdin.readline().strip().split(" "))
    p,c,w=kkk[i-1]
    arr[p].append([c,w])
    arr[c].append([p,w])

def far_node(start):
    print("in start=",start,"\tchilds=",arr[start])
    queue=deque([(start,0)])
    visited=[0]*(N+1)
    visited[start]=1
    farr=[start, 0] # node idx, node distance
    while queue:
        c,w=queue.popleft()
        print("c=",c,"w=",w,"\tchilds=",arr[c])
        for newc,neww in arr[c]:
            if visited[newc]!=1:
                if len(arr[newc])!=1:
                    queue.append((newc,neww+w))
                visited[newc]=1
                if farr[1]<neww+w:
                    farr=[newc, neww+w]
        print("c=",c,"w=",w,"\tqueues=",queue)
    return farr

n,d=far_node(1)
print("----------------------")
nn,dd=far_node(n)
print(dd)










#=============시간초과==================
# import sys

# # N=int(sys.stdin.readline().strip())
# # arr=[list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N-1)]
# N=12
# arr=[[1, 2, 3], [1, 3, 2], [2, 4, 5], [3, 5, 11], [3, 6, 9], [4, 7, 1], [4, 8, 7], [5, 9, 15], [5, 10, 4], [6, 11, 6], [6, 12, 10]]

# pos=[-1]*10001
# savem=[0]*10001

# for i in range(N-1):
#     if pos[arr[i][0]]==-1:
#         pos[arr[i][0]]=i

# def getmax(parent):
#     global maxanswer
#     print("parent=",parent,"\tin")
#     # if pos[parent]==-1:
#     #     return
#     max_twochild=[]
#     for i in range(pos[parent],N-1):
#         if arr[i][0]>parent:
#             break
#         if arr[i][0]==parent:
#             if pos[parent]!=-1:
#                 getmax(arr[i][1])
#             max_twochild.append(arr[i][2]+savem[arr[i][1]])

#     max_twochild.sort(reverse=True)
#     print("parent=",parent,"\tmax_twochild=",max_twochild)
#     if len(max_twochild)==1:
#         savem[parent]=max(savem[parent],max_twochild[0])
#     elif len(max_twochild)>1:
#         maxanswer=max(maxanswer, max_twochild[0]+max_twochild[1])
#         savem[parent]=max(savem[parent],max_twochild[0])
#     print("parent=",parent,"\tout return 0")
#     return 

# maxanswer=0
# getmax(1)
# print(maxanswer)

