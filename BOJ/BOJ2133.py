import sys
N=int(sys.stdin.readline().strip())

if N%2==1 or N==0: print(0)
elif N==2: print(3)
else:
    arr=[0]*33
    arr[0]=1
    arr[2]=3
    arr[4]=11
    i=6
    while i<=N:
        arr[i]=arr[i-2]*3 + sum(arr[0:i-4+1])*2
        i+=2
    print(arr[N])