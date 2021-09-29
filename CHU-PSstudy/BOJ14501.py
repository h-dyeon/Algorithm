import sys

N=int(sys.stdin.readline().strip())
matrix=[]
for i in range(N):
    tmp=list(map(int,sys.stdin.readline().strip().split(' ')))
    if tmp[0]+i<=N:
        matrix.append([i,tmp])
        # matrix[i]=tmp

# print(matrix)

# N=15 답 3000
# matrix=[[0, [5, 1000]], [1, [5, 1000]], [2, [5, 1000]], [3, [5, 1000]], [4, [5, 1000]], [5, [5, 1000]], [6, [5, 1000]], [7, [5, 1000]], [8, [5, 1000]], [9, [5, 1000]], [10, [5, 1000]]]

# N=11
# matrix=[[0, [5, 10]], [1, [5, 10]], [2, [5, 200]], [3, [5, 10]], [4, [5, 10]], [5, [5, 10]]]

# N=7
# matrix={0: [3, 10], 1: [5, 20], 2: [1, 10], 3: [1, 20], 4: [2, 15]}

# N=4
# matrix=[[1, [1, 3]], [3, [1, 5]]]

# N=5
# matrix=[[1, [2, 3]],[2, [1, 5]], [3, [2, 5]]]

visited=1
maxanswer=0
while visited<(1<<len(matrix)):
    tmp=0
    date=-1
    for i in range(len(matrix)):
        if visited&(1<<i) and date<matrix[i][0]:
            tmp+=matrix[i][1][1]
            date=matrix[i][0]+matrix[i][1][0]-1
    maxanswer=max(maxanswer,tmp)
    visited+=1

print(maxanswer)