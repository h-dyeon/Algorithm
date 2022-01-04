#220104
import sys

def calc(mlist):
    tmp=[0]*len(mlist)
    for i in range(1,len(mlist)):
        for j in range(0,i):
            if mlist[i]>mlist[j]:
                tmp[i]=max(tmp[i],tmp[j]+1)
    return tmp
N=int(sys.stdin.readline().strip())
m=list(map(int,sys.stdin.readline().strip().split(' ')))
ll=calc(m)
rr=list(reversed(calc(list(reversed(m)))))
t=[x+y for x,y in zip(ll,rr)]
print(max(t)+1)


# import sys
# #N = int(sys.stdin.readline().strip())
# #arr=list(map(int,sys.stdin.readline().strip().split(' ')))
# N=10
# arr=[1, 5, 2, 1, 4, 3, 4, 5, 2, 1]

# r_dp=[1 for i in range(N)]
# l_dp=[1 for i in range(N)]

# for i in range(N):
#     for j in range(i):
#         if arr[i]>arr[j]:
#             r_dp[i]=max(r_dp[i],r_dp[j]+1)

# for i in range(N-1, -1, -1):
#     for j in range(N-1,i,-1):
#         if arr[i]>arr[j]:
#             l_dp[i]=max(l_dp[i],l_dp[j]+1)

# answer=0
# for i in range(N):
#     if answer<r_dp[i]+l_dp[i]-1:
#         answer=r_dp[i]+l_dp[i]-1
# print(answer)