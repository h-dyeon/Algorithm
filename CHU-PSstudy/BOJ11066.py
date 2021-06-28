import sys

INF=99999999
T=int(sys.stdin.readline().strip())

while T :
    T-=1   
    K=int(sys.stdin.readline().strip())
    papers=list(map(int,sys.stdin.readline().strip().split(' ')))

    matrix=[[ INF for i in range(K+1)] for _ in range(K+1)]
    subsum=[0 for i in range(K+1)]
    for i in range(1,K+1):
        subsum[i]=subsum[i-1]+papers[i-1]
        matrix[i][i]=0

    for gap in range(1,K):
        for start in range(1,K-gap+1):
            end=start+gap
            for mid in range(start,end):
                nowcost=subsum[end]-subsum[start-1]
                beforecost=matrix[start][mid]+matrix[mid+1][end]
                matrix[start][end]=min(matrix[start][end], nowcost+beforecost)
    print(matrix[1][K])

