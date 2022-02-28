import sys

# N,S=map(int, sys.stdin.readline().strip().split(' '))
# arr=list(map(int, sys.stdin.readline().strip().split(' ')))


N=10
S=15
arr=[5, 1, 3, 5, 10, 7, 4, 9, 2, 8]

ll,rr=0,0
sum=0
answer=1e9

while ll<len(arr):
    if sum<S and rr<len(arr):
        sum+=arr[rr]
        rr+=1        
    else:
        if sum>=S:
            answer=min(answer,rr-ll)
        sum-=arr[ll]
        ll+=1

if answer==1e9:
    print(0)
else:
    print(answer) 
