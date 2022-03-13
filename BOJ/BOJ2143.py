import sys

def getSums(l, arr):
    dic={}
    newarr=[0 for _ in range(l+1)]
    for i in range(0,l):
        newarr[i+1]=newarr[i]+arr[i]
    for i in range(l):
        for j in range(i+1,l+1):
            tmp=newarr[j]-newarr[i]
            if tmp in dic:
                dic[tmp]+=1
            else:
                dic[tmp]=1
    return dic

T=int(input())
N=int(input())
A=list(map(int,sys.stdin.readline().strip().split(' ')))
M=int(input())
B=list(map(int,sys.stdin.readline().strip().split(' ')))

Adic=getSums(N,A)
Bdic=getSums(M,B)

answer=0
for k in Adic.keys():
    if T-k in Bdic:
        answer+=Adic[k]*Bdic[T-k]
print(answer)