import sys

# N=int(sys.stdin.readline().strip())
# arr=[list(map(int,sys.stdin.readline().strip().split(" "))) for _ in range(N-1)]
N=12
arr=[[1, 2, 3], [1, 3, 2], [2, 4, 5], [3, 5, 11], [3, 6, 9], [4, 7, 1], [4, 8, 7], [5, 9, 15], [5, 10, 4], [6, 11, 6], [6, 12, 10]]


def getmax(parent):
    max_twochild=[]
    for i in range(N-1):
        if arr[i][0]==parent:
            max_twochild.append(arr[i][2]+getmax(arr[i][1]))
    max_twochild.sort()
    if len(max_twochild)<2:
        return 0
    else :
        maxanswer=max(maxanswer, max_twochild[0]+max_twochild[1])
        return max_twochild[0]+max_twochild[1]


maxanswer=0
getmax(1)
print(maxanswer)
