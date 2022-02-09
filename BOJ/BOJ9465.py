import sys


def dp():
    n=int(input())
    arr=[list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(2)]
    if n==1:
        return max(arr[0][0],arr[1][0])
    
    dp=[[0 for i in range(n+1)] for j in range(2)] 
    dp[0][1]=arr[0][1-1]
    dp[1][1]=arr[1][1-1]
    for i in range(2,n+1):
        dp[0][i]=max(dp[1][i-1],dp[1][i-2])+arr[0][i-1]
        dp[1][i]=max(dp[0][i-1],dp[0][i-2])+arr[1][i-1]

    return max(dp[0][n],dp[1][n])

T=int(input())
for t in range(T):
    print(dp()) 