import sys
from sys import stdin

K,P,N=map(int, stdin.readline().strip().split(' '))
mod=1000000007

def modulo(p,n):
    if n==1:
        return p%mod
    newn=int(n/2)
    print("p=%d, n=%d, newn=%d,",p,n,newn)
    tmp=modulo(p,newn)**2
    if n%2==0:
        return tmp % mod
    else:
        return ( tmp * (p % mod) ) % mod

result= (K%mod * modulo(P,N) )%mod
print(result)

