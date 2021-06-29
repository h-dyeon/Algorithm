############################ 512ms ############################
import sys

N=int(sys.stdin.readline().strip())
matrix = [list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]

dp=[10**9]*(1<<N)
dp[0]=0
for mask in range(0,1<<N):
    #bit count
    k=0
    for i in range(N):
        if mask & (1<<i):
            k+=1

    for j in range(0,N):
        if ((1<<j) & mask) == 0: #Tasks not yet assigned to anyone
            dp[mask|(1<<j)] = min( dp[mask|(1<<j)], dp[mask]+matrix[k][j])

print(dp[-1]) # the last column


############################ 1392ms ############################
# import sys
# import math

# def bitcount(m):
#     if m==0:
#         return 0
#     return m%2 + bitcount(int(m/2))

# N=int(sys.stdin.readline().strip())
# matrix = [list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]

# dp=[math.inf]*(2**N)
# dp[0]=0
# for mask in range(0,2**N):
#     k=bitcount(mask)
#     for j in range(0,N):
#         if ((1<<j) & mask) == 0: #Tasks not yet assigned to anyone
#             dp[mask|(1<<j)] = min( dp[mask|(1<<j)], dp[mask]+matrix[k][j])

# print(dp[(2**N)-1])