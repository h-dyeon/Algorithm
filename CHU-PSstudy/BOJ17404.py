import sys

RGB=3
INF=10e9
#N=int(sys.stdin.readline().strip())
#val=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]
N=3
val=[[26, 40, 83], [49, 60, 57], [13, 89, 99]]

dp=[[INF]*3 for _ in range(2)]

answer=INF
for c in range(RGB):
    dp[0][c]=val[0][c]
    now=1
    before=0
    for i in range(1,N):
        dp[now][0]=min(dp[before][1],dp[before][2])+val[i][0]
        dp[now][1]=min(dp[before][0],dp[before][2])+val[i][1]
        dp[now][2]=min(dp[before][0],dp[before][1])+val[i][2]
        now=before
        before=0 if now== 1 else 1
    for cc in range(RGB):
        if cc!=c:
            answer=min(answer,dp[before][cc])

print(answer)

# import sys

# RGB=3
# INF=10e9
# #N=int(sys.stdin.readline().strip())
# #val=[list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(N)]
# N=3
# val=[[26, 40, 83], [49, 60, 57], [13, 89, 99]]


# now=1
# before=0 if now== 1 else 1

# print(now)
# print(before)

# now=before
# before=0 if now== 1 else 1

# print(now)
# print(before)



# dp=[[INF]*3 for _ in range(N)]

# answer=INF
# for c in range(RGB):
#     for cc in range(RGB):
#         if c==cc:
#             dp[0][cc]=val[0][c]
#         else:
#             dp[0][cc]=INF
#     for i in range(1,N):
#         dp[i][0]=min(dp[i-1][1],dp[i-1][2])+val[i][0]
#         dp[i][1]=min(dp[i-1][0],dp[i-1][2])+val[i][1]
#         dp[i][2]=min(dp[i-1][0],dp[i-1][1])+val[i][2]
#     for cc in range(RGB):
#         if cc!=c:
#             answer=min(answer,dp[-1][cc])

# print(answer)