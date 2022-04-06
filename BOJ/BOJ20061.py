# N=int(input())
# blocks=[list(map(int,input().split(' '))) for _ in range(N)]
# print(blocks)

# N=1
# blocks=[[1,1,1]]

N=8
blocks=[[1, 1, 1], [2, 3, 0], [3, 2, 2], [3, 2, 3], [3, 1, 3],[2,0,0],[3,2,0],[3,1,2]]

arr=[[[0]*4 for _ in range(6)] for _ in range(2)] #green0,blue1


# mode=0
# arr[0][0]=[1,1,1,1]
# arr[0][1]=[2,2,2,2]
# arr[0][2]=[3,3,3,3]
# arr[0][4]=[5,5,5,5]
# arr[0][5]=[6,6,6,6]
# for i in range(5,-1,-1):
#     if arr[mode][i].count(0)==0:
#         answer+=1
#         del arr[mode][i]
#         arr[mode].append([0,0,0,0])

# print(arr[0])
def moveblock(mode,x,y,t):
    global arr
    score=0
    # move block
    if t==1:
        status=True
        for i in range(5,0,-1):
            if arr[mode][i-1][y]!=0:
                arr[mode][i][y]=t
                status=False
                break
        if status:
            arr[mode][0][y]=t

    elif t==2:
        status=True
        for i in range(5,0,-1):
            if arr[mode][i-1][y]!=0 or arr[mode][i-1][y+1]!=0:
                status=False
                arr[mode][i][y]=t
                arr[mode][i][y+1]=t
                break
        if status:
            arr[mode][0][y]=t
            arr[mode][0][y+1]=t

    elif t==3:
        status=True
        for i in range(5,1,-1):
            if arr[mode][i][y]==0 and arr[mode][i-1][y]==0 and arr[mode][i-2][y]!=0:
                status=False
                arr[mode][i][y]=t
                arr[mode][i-1][y]=t
                break
        if status:
            arr[mode][1][y]=t
            arr[mode][0][y]=t

    # get score
    for i in range(5,-1,-1):
        if arr[mode][i].count(0)==0:
            score+=1
            del arr[mode][i]
            arr[mode].append([0,0,0,0])

    # light room
    while arr[mode][4].count(0)!=4:
        del arr[mode][0]
        arr[mode].append([0,0,0,0])
    return score

answer=0
for gt,gx,gy in blocks:
    #select blue&green block
    print(gt,gx,gy)
    bx,by,bt=gy,3-gx,gt
    if gt==2:
        bt=3
    elif gt==3:
        bt=2
        by-=1
    # move block
    answer+=moveblock(0,gx,gy,gt) #green 0
    answer+=moveblock(1,bx,by,bt) #blue 1

print(answer)
a=sum([row.count(0) for row in arr[0]])
b=sum([row.count(0) for row in arr[1]])
print(48-a-b)

    




    # status=True
    # while status:
    #     status=False
    #     for i in range(4):
    #         if arr[mode][i].count(0)==0:
    #             status=True
    #             answer+=1
    #             del arr[mode][i]
    #             arr[mode].append([0,0,0,0])

