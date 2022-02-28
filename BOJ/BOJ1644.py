from operator import ne
import sys

N=50 #int(input())

# nest=set([i for i in range(3,N+1,2)])
# nest.add(2)
# for i in range(3,len(nest),2):
#     for j in range(3,len(nest),2):
#         if i*j>N: break
#         if i*j in nest:
#             nest.remove(i*j)
# nest=list(nest)


primes=[0 for _ in range(N)] # save primes
nest=[1 for _ in range(N+1)]
t=0
for i in range(2,len(nest)):
    if nest[i]==0: continue

    primes[t]=i #save primes
    t+=1

    for j in range(2,len(nest)):
        if i*j>N: break
        nest[i*j]=0

print(primes)


left,right=0,0
summ=0
answer=0

while left<t:
    if summ<N and right<t:
        summ+=primes[right]
        right+=1
    else:
        if summ==N:
            answer+=1
        summ-=primes[left]
        left+=1
print(answer)