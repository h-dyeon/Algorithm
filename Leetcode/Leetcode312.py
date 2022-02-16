nums = [3,1,5,8]
dp=[[0 for _ in range(len(nums))]for _ in range(len(nums))]

for n in range(0,len(nums)):
    for i in range(0,len(nums)-n):
        j=i+n
        maxx=0
        for k in range(i,j+1):
            left=0 if k==i else dp[i][k-1]
            right=0 if k==j else dp[k+1][j]

            leftnum=nums[i-1] if i!=0 else 1
            rightnum=nums[j+1] if j!=(len(nums)-1) else 1
            maxx=max(maxx,left+right+(leftnum*nums[k]*rightnum))
        dp[i][j]=maxx

print(dp[0][len(nums)-1])