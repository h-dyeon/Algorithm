import sys
import math

T=int(sys.stdin.readline().strip())

while T :
    T-=1   
    K=int(sys.stdin.readline().strip())
    papers=list(map(int,sys.stdin.readline().strip().split(' ')))

    maximum = math.inf
    matrix = [[maximum] * (K+1) for _ in range(K+1)]
    subsum=[0] *(K+1)
    for i in range(1,K+1):
        subsum[i]=subsum[i-1]+papers[i-1]
        matrix[i][i]=0

    for gap in range(1,K):
        for start in range(1,K-gap+1):
            end=start+gap
            for mid in range(start,end):
                beforecost=matrix[start][mid]+matrix[mid+1][end]
                matrix[start][end]=min(matrix[start][end], beforecost)
            matrix[start][end]+=subsum[end]-subsum[start-1]
    print(matrix[1][K])

