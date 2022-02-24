nums = [1,2,3,4,5]
requests = [[1,3],[0,1]]


visited=[0 for _ in range(len(nums)+1)]
# for s,e in requests:
#     print(s,e)
#     for i in range(s,e+1):
#         visited[i]+=1

for s,e in requests:
    visited[s]+=1
    visited[e+1]+=-1
for i in range(1,len(nums)):
    visited[i]+=visited[i-1]


visited=sorted(visited,reverse=True)
nums=sorted(nums,reverse=True)

answer=0
modd=1000000007
for i in range(0,len(nums)):
    if visited[i]==0:
        break
    answer=(answer+(visited[i]*nums[i])%modd)%modd

print(answer)