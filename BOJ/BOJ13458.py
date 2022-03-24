import sys

N=int(input())
arr=list(map(int,sys.stdin.readline().strip().split(' ')))
B,C=list(map(int,sys.stdin.readline().strip().split(' ')))


answer=N
for i in range(N):
    tmp=arr[i]-B
    if tmp>0:
        if tmp%C==0:
            answer+=int(tmp/C)
        else:
            answer+=(int(tmp/C)+1)
print(answer)
        