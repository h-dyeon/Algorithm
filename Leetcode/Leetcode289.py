import copy

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

newboard=copy.deepcopy(board)

dr=[-1,-1,-1,0,1,1,1,0]
dc=[-1,0,1,1,1,0,-1,-1]

for i in range(len(board)):
    for j in range(len(board[0])):
        numLiveNeighbor=0
        for k in range(8):
            ni=i+dr[k]
            nj=j+dc[k]
            if 0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj]==1:
                numLiveNeighbor+=1
        print(i,j,numLiveNeighbor)
        if board[i][j]==1 and (numLiveNeighbor<2 or numLiveNeighbor>3):
                newboard[i][j]=0
        elif board[i][j]==0 and numLiveNeighbor==3:
            newboard[i][j]=1

print(newboard)

board=copy.deepcopy(newboard)
print(board)