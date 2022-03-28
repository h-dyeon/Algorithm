from collections import deque
house=deque([])
chicken=deque([])
answer=1e9
N,M=map(int,input().split(' '))
for r in range(N):
    tmp=list(map(int,input().split(' ')))
    for c in range(len(tmp)):
        if tmp[c]==1:
            house.append([r,c])
        elif tmp[c]==2:
            chicken.append([r,c])
print(chicken)
print(house)
# N,M=5,3
# chicken=deque([[1, 2], [2, 2], [4, 4]])
# house=deque([[0, 2], [1, 4], [2, 1], [3, 2]])


lchicken=len(chicken)
lhouse=len(house)
matrix=[[1e9]*lchicken for _ in range(lhouse)]
for i in range(lchicken):
    cR,cC=chicken[i]
    for j in range(lhouse):
        hR,hC=house[j]
        matrix[j][i]=abs(cR-hR)+abs(cC-hC)

visited=set()

def permutation(bits,cnt):
    global answer,visited
    if cnt==0:
        print("=====",bin(bits))
        tmp=[1e9]*lhouse # minimum distance between chicken and house
        for i in range(lchicken):
            if bits & (1<<i): # calc distance with selected chicken
                for j in range(lhouse):
                    tmp[j]=min(tmp[j],matrix[j][i])
        answer=min(answer,sum(tmp))
        return
    for i in range(lchicken):
        if bits & (1<<i):
            continue
        start=bits|(1<<i)
        if start not in visited:
            # print(bin(bits),bin(start),cnt)
            visited.add(start)
            permutation(start,cnt-1)
        
   

permutation(1<<lchicken,M)
print(answer)