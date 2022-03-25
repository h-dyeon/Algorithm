import sys

sys.stdin.readline().strip().split(' ')


N,M=list(map(int,input().split(' ')))
arr=[list(map(int,input().split(' '))) for _ in range(N)]
print(arr)

# N,M=4,5
# arr=[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

# N,M=5,5
# arr=[[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 2, 1, 2, 1]]

types=[[[1],[1],[1],[1]], # 1111
        [[1,1,1,1]], # square
        [[1,1],[1,1]],
        [[1,0],[1,0],[1,1]],# gun
        [[1,1,1],[1,0,0]],
        [[1,1],[0,1],[0,1]],
        [[0,0,1],[1,1,1]],
        [[0,1],[0,1],[1,1]],
        [[1,1,1],[0,0,1]],
        [[1,1],[1,0],[1,0]],
        [[1,0,0],[1,1,1]],
        [[1,0],[1,1],[0,1]], #snake
        [[0,1,1],[1,1,0]],
        [[0,1],[1,1],[1,0]],
        [[1,1,0],[0,1,1]],
        [[1,0],[1,1],[1,0]], #o!
        [[0,1,0],[1,1,1]],
        [[0,1],[1,1],[0,1]],
        [[1,1,1],[0,1,0]]]
sizeT=[(4,1),(1,4),
        (2,2),
        (3,2),(2,3),(3,2),(2,3),
        (3,2),(2,3),(3,2),(2,3),
        (3,2),(2,3),
        (3,2),(2,3),
        (3,2),(2,3),(3,2),(2,3)]
numtype=len(sizeT)

answer=0
for r in range(N):
    for c in range(M):
        for k in range(numtype):
            rl,cl=sizeT[k]
            if r+rl-1>=N or c+cl-1>=M:
                continue
            tmp=0
            for x in range(rl):
                for y in range(cl):
                    if types[k][x][y]==1:
                        tmp+=arr[r+x][c+y]
            answer=max(answer,tmp)
print(answer)
