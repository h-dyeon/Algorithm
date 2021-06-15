import sys

def solution_wrong():
    # n=int(sys.stdin.readline().strip())
    # ranges=list(map(int,sys.stdin.readline().strip().split(' ')))
    n = 8
    ranges = [4,0,0,0,4,0,0,0,4]

    if set(ranges) =={0}:
        return -1

    result=[-1 for _ in range(n)]
    result_sub=[0 for _ in range(n)]

    for i in range(0,n+1):
        start= i-ranges[i] if 0<i-ranges[i] else 0
        finish= i+ranges[i] if n>i+ranges[i] else n
        vary=finish-start

        if vary==n:
            return 1

        for j in range(start,finish):
            if result_sub[j]<vary:
                result[j]=i
                result_sub[j]=vary

    r=set(result)
    if r=={-1}:
        return -1
    else:
        return len(r)

def solution():
    # n=int(sys.stdin.readline().strip())
    # ranges=list(map(int,sys.stdin.readline().strip().split(' ')))
    # n = 8
    # ranges = [4,0,0,0,4,0,0,0,4]
    # n = 11
    # ranges = [1,0,2,1,1,3,0,0,1,0,2,5]
    n=9
    ranges=[0,5,0,3,3,3,1,4,0,4]

    if set(ranges) =={0}:
        return -1

    cal=[-1 for _ in range(n+1)]
    for i in range(0,n+1):
        left=max(i-ranges[i],0)
        right=min(i+ranges[i],n)
        cal[left]=max(cal[left],right)

    result=0
    maxR=0
    currentcover=0
    for i in range(0,n+1):
        if maxR<i:
            return -1
        if currentcover < i:
            result+=1
            currentcover=maxR
        maxR=max(maxR, cal[i])
    return result




print(solution())
#print(solution_wrong())