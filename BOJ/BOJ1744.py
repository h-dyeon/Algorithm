import sys

N=int(input())
negatives=[]
positives=[]
ones=0
isZero=False
for i in range(N):
    t=int(sys.stdin.readline().strip())
    if t<0:
        negatives.append(t)
    elif t==1:
        ones+=1
    elif t>0:
        positives.append(t)
    else:
        isZero=True

positives=list(reversed(sorted(positives)))
negatives=sorted(negatives)
answer=ones

for i in range(0,len(positives)-1,2):
    answer+=positives[i]*positives[i+1]
if len(positives)%2==1:
    answer+=positives[-1]

for i in range(0,len(negatives)-1,2):
    answer+=negatives[i]*negatives[i+1]
if len(negatives)%2==1 and isZero==False:
    answer+=negatives[-1]




print(answer)



# dp=[0 for _ in range(N)]
# dp[0]=arr[0]
# for i in range(1,N):
#     tmp=arr[i]
#     for j in range(i-1,-1,-1):
#         dp[i]=max(dp[i],dp[j]+tmp)
#         tmp*=arr[j]
#     dp[i]=max(dp[i],tmp)

# print(dp[N-1])