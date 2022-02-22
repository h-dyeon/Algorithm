import sys
from collections import deque

primes=[1 for _ in range(10001)]
for i in range(2,10001):
    for j in range(2,10001):
        if i*j>10000:
            break
        primes[i*j]=0

N=int(input())
for i in range(N):
    start,end=map(int,sys.stdin.readline().strip().split(' '))
    visited=[-1 for _ in range(10001)]

    dq=deque([start])
    visited[start]=0
    while dq:
        tmp=dq.popleft()
        for j in range(4):
            for k in range(10):
                t=str(tmp)
                t=int(t[:j]+str(k)+t[j+1:])                
                if primes[t]==1 and visited[t]==-1 and t>=1000 and tmp!=t:
                    visited[t]=visited[tmp]+1
                    dq.append(t)

    if visited[end]!=-1:
        print(visited[end])
    else:
        print("Impossible")




