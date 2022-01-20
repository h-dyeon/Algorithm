
# ciper=input()
ciper='1111111111' #'2511411012'
mod=1000000

if ciper[0]=='0' or len(ciper)>5000:
    print(0)
else:
    if len(ciper)==1:
        print(1)
    else :
        dp=[0 for _ in range(len(ciper)+1)]
        dp[0]=1
        sub=(int(ciper[0])*10 + int(ciper[1]))
        if 10<=sub<=26: dp[1]+=1
        if 1<=int(ciper[1])<=9: dp[1]+=1

        for i in range(2,len(ciper)):
            sub=(int(ciper[i-1])*10 + int(ciper[i]))
            if 10<=sub<=26:
                dp[i]=(dp[i]+dp[i-2])%mod
            if 1<=int(ciper[i])<=9:
                dp[i]=(dp[i]+dp[i-1])%mod
        print(dp[len(ciper)-1])

