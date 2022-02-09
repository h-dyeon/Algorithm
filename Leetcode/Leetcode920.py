class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

        modd=1000000007

        dp=[[0 for _ in range(goal+1)] for _ in range(n+1)]
        dp[0][0]=1

        for i in range(1,n+1):
            for j in range(1,goal+1):
                dp[i][j]=(dp[i-1][j-1]*(n-i+1) + dp[i][j-1]*max(0,i-k))%modd
        return dp[n][goal]