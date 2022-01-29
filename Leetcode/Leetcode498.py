mat = [[1],[2],[3],[4]]

m=len(mat)
n=len(mat[0])
answer=[]
for i in range(0,m+n,2):
    #right_up
    start,finish,step=min(i,m-1),max(-1,i-n),-1
    for j in range(start,finish,step):
        answer.append(mat[j][i-j])
        if i-j>=n : break
    #left_down
    i+=1
    start,finish,step=max(0,i-n+1),min(i+1,m),1
    for j in range(start,finish,step):
        answer.append(mat[j][i-j])

