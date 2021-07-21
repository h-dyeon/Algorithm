#참고 : https://latter2005.tistory.com/51

import sys

def gcd(a,b):
    while(b!=0):
        r=a%b ; a=b; b=r
    return a

N=int(sys.stdin.readline().strip())
arr=[sys.stdin.readline().strip() for i in range(N)]
K=int(sys.stdin.readline().strip())

if K==1:
    print("1/1")
else : 
    # 10^x
    tens=[0]*51
    tens[0]=1
    for i in range(1,51):
        tens[i]=(tens[i-1]*10)%K

    # remain of each string
    remains=[0]*N
    for i in range(N):
        r=0
        for j in range(len(arr[i])):
            r=(r*10 + int(arr[i][j])) %K
        remains[i]=r

    # find dp
    dp=[[0]*K for _ in range(1<<N)]
    dp[0][0]=1
    for i in range(1<<N):
        for j in range(K):
            for t in range(N):
                if ((i&(1<<t))==0):
                    dp[i|(1<<t)][(j*tens[len(arr[t])] + remains[t]) % K] +=dp[i][j]

    p=dp[(1<<N)-1][0]
    q=1
    for i in range(1,N+1):
        q*=i
    tmp=gcd(q,p)
    print('{0}/{1}'.format(int(p/tmp),int(q/tmp)))
