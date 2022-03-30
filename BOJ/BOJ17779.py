N=int(input())
arr=[[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    tmp=list(map(int,input().split(' ')))
    for j in range(N):
        arr[i][j+1]=tmp[j]
# arr=[list(map(int,input().split(' '))) for _ in range(N)]
print(arr)
# N=6
# arr=[[1, 2, 3, 4, 1, 6], [7, 8, 9, 1, 4, 2], [2, 3, 4, 1, 1, 3], [6, 6, 6, 6, 9, 4], [9, 1, 9, 1, 9, 5], [1, 1, 1, 1, 9, 9]]
# N=7
# arr=[[1,1,1,1,1,2,2],[1,1,1,1,5,2,2],[1,1,1,5,5,5,2],[1,1,5,5,5,5,5],[3,5,5,5,5,5,4],[3,3,5,5,5,4,4],[3,3,3,5,4,4,4]]


def partialsum(x,y,d1,d2):
    hello=[[0]*(N+1) for _ in range(N+1)]
    ssum=[0]*5
    # 1
    for r in range(1,x+d1):
        f=y+1
        if r>=x: 
            f-=(r-x+1)
        for c in range(1,f):
            hello[r][c]=1
            ssum[0]+=arr[r][c]
            # print(r,c)
    # print('-----------')
    # 2
    for r in range(1,x+d2+1):
        s=y+1
        if r>x:
            s+=(r-x)
        for c in range(s,N+1):
            hello[r][c]=2
            ssum[1]+=arr[r][c]
            # print(r,c)
    # print('-----------')
    # 3
    for r in range(x+d1,N+1):
        f=y-d1+d2
        if r<x+d1+d2:
            f-=(x+d1+d2-r)
        for c in range(1,f):
            hello[r][c]=3
            ssum[2]+=arr[r][c]
            # print(r,c)
    # print('-----------')
    # 4
    for r in range(x+d2+1,N+1):
        s=y-d1+d2
        if r<=x+d1+d2:
            s+=(x+d1+d2-r+1)
        for c in range(s,N+1):
            hello[r][c]=4
            ssum[3]+=arr[r][c]
            # print(r,c)
    # 5
    # print([sum(row) for row in arr])
    ssum[4]=sum([sum(row) for row in arr])-sum(ssum)
    print(x,y,d1,d2,ssum)

    if x==3 and y==3 and d1==1 and d2==1:
        print(0)
    ssum.sort()
    return abs(ssum[0]-ssum[4])

    # answer=1e9
    # for i in range(5):
    #     for j in range(i+1,5):
    #         answer=min(answer,abs(ssum[i]-ssum[j]))
    # return answer

realanswer=1e9
for x in range(1,N):
    for y in range(2,N):
        for d1 in range(1,N):
            if y-d1<1: 
                break
            for d2 in range(1,N):
                if y+d2>N:
                    break
                if x+d1+d2<=N:
                    tmp=partialsum(x,y,d1,d2)
                    realanswer=min(realanswer,tmp)
                    print("-----",realanswer)

print(realanswer)
