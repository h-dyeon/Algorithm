import sys

N, K=map(int,sys.stdin.readline().strip().split(' '))
backinfo = list(list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N))

dp=[[0 for i in range(K+1)] for i in range(N+1)]

for i in range(1,N+1):
    iweight=backinfo[i-1][0]
    ivalue=backinfo[i-1][1]
    for j in range(K+1):
        if j<iweight:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-iweight]+ivalue, dp[i-1][j])

print(dp[N][K])