from collections import deque

# def checkConnected(start,check):
#     visited[start]=check
#     dq=deque([start])
#     while dq:
#         t=dq.popleft()
#         for i in range(nodesize):
#             if visited[i]==0 and t!=i and isConnected[t][i]==1:
#                 visited[i]=check
#                 dq.append(i)
def checkConnected(start,check):
    visited[start]=check
    for i in range(nodesize):
        if visited[i]==0 and i!=start and isConnected[start][i]==1:
            checkConnected(i,check)


nodesize=len(isConnected)
visited=[0 for _ in range(nodesize)]
check=0
for i in range(nodesize):
    if visited[i]==0:
        check+=1
        checkConnected(i,check)

print(check)   
