import sys
N,M=map(int,sys.stdin.readline().split(' '))
matrix=[sys.stdin.readline().strip() for _ in range(N)]
# N=10
# M=13
# matrix=['BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB', 'WWWWWWWWWWBWB']

def countdiff(str1, mrow):
    answer=0
    for i in range(0,8):
        if str1[i]!=mrow[i] :
            answer+=1
    return answer

rows=['BWBWBWBW','WBWBWBWB']
answer=10000
for i in range(N-8+1):
    for j in range(M-8+1):
        tmp=[0,0]
        for r in range(8):
            tmp[0]+=countdiff(matrix[i+r][j:j+8],rows[r%2])
            tmp[1]+=countdiff(matrix[i+r][j:j+8],rows[(r+1)%2])
        answer=min(answer, min(tmp[0],tmp[1]))
print(answer)
