def recur(r,c,len):
    if len==3:
        arr[r][c]="*"
        arr[r+1][c-1],arr[r+1][c+1]="*","*"
        arr[r+2][c-2]="*"
        arr[r+2][c-1]="*"
        arr[r+2][c]="*"
        arr[r+2][c+1]="*"
        arr[r+2][c+2]="*"
        return
    recur(r,c,int(len/2))
    recur(r+int(len/2),c-int(len/2),int(len/2))
    recur(r+int(len/2),c+int(len/2),int(len/2))

N=int(input())
arr=[[" " for _ in range(2*N-1)] for _ in range(N)]
recur(0,N-1,N)
for i in arr:
    print(''.join(i)) # print: abc
