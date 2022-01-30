import sys

N,C=map(int, sys.stdin.readline().strip().split(" "))
house=[int(sys.stdin.readline().strip()) for i in range(N)]
house=sorted(house)


minn,maxx=1,house[-1]-house[0]
answer=0
while minn<=maxx:
    midd=int((minn+maxx)/2)

    count,check=1,house[0]
    for i in range(1,N):
        if house[i]-check>=midd:
            count+=1
            check=house[i]
    if count>=C:
        answer=max(answer,midd)
        minn=midd+1
    elif count<C:
        maxx=midd-1

print(answer)