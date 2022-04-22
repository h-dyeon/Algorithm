################################################ 22.04.22
def adjust(matrix):
    R_=len(matrix)
    tmp=[r[:] for r in matrix]
    for i in range(R_):
        C_ = len(matrix[i])
        for j in range(C_):
            if j+1<C_ and abs(matrix[i][j]-matrix[i][j+1])>4:
                d=int(abs(matrix[i][j]-matrix[i][j+1])/5)
                if matrix[i][j]>matrix[i][j+1]:
                    tmp[i][j]-=d
                    tmp[i][j + 1]+=d
                elif matrix[i][j]<matrix[i][j+1]:
                    tmp[i][j]+=d
                    tmp[i][j + 1]-=d
            if i+1<R_ and len(matrix[i+1])>j and abs(matrix[i][j]-matrix[i+1][j])>4:
                d=int(abs(matrix[i][j]-matrix[i+1][j])/5)
                if matrix[i][j]>matrix[i+1][j]:
                    tmp[i][j]-=d
                    tmp[i+1][j]+=d
                elif matrix[i][j]<matrix[i+1][j]:
                    tmp[i][j]+=d
                    tmp[i+1][j]-=d
    return tmp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N,K=map(int,input().split(' '))
    tmp=list(map(int,input().split(' ')))
    arr=[[0] for _ in range(N)]
    for i in range(N):
        arr[i][0]=tmp[i]


    answer=0
    while True:
        min_=min([min(r) for r in arr])
        max_=max([max(r) for r in arr])
        if max_-min_<=K:
            break
        answer+=1

        arr=[[arr[i][0] if arr[i][0]!=min_ else arr[i][0]+1] for i in range(N)]

        finish_row=0
        while len(arr[finish_row])<= len(arr)-finish_row-1:
            col_=len(arr[finish_row])
            for r in range(finish_row,-1,-1):
                for c in range(col_):
                    arr[finish_row+c+1].append(arr[r][c])
            for _ in range(finish_row+1):
                del arr[0]
            finish_row=col_-1

        tmp=adjust(arr)

        arr=[0]*N
        idx=0
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                arr[idx]=tmp[i][j]
                idx+=1

        div4=int(N/4)
        idx=0
        tmp=[[0]*div4 for _ in range(4)]
        for i in range(div4):
            tmp[2][div4-i-1]=arr[idx]
            idx+=1
        for i in range(div4):
            tmp[1][i]=arr[idx]
            idx+=1
        for i in range(div4):
            tmp[0][div4-i-1]=arr[idx]
            idx+=1
        for i in range(div4):
            tmp[3][i]=arr[idx]
            idx+=1

        tmp = adjust(tmp)

        arr = [[0] for _ in range(N)]
        idx=0
        for i in range(div4):
            for j in range(4):
                arr[idx][0]=tmp[3-j][i]
                idx+=1
    print(answer)


####################################################33
# N,K=map(int,input().split(' '))
# arr=[]
# tmp=list(map(int,input().split(' ')))
# for t in tmp:
#     arr.append([t])
# # print(arr)


# # N,K=8,7
# # arr=[[5],[2],[3],[14],[9],[2],[11],[8]]
# numarr=len(arr)


# def stack():
#     startrow=0
#     finishrow=0
#     while len(arr[finishrow])<=(numarr-1-finishrow):
#         len_=len(arr[finishrow])
#         for i in range(finishrow,startrow-1,-1):
#             for j in range(len(arr[i])):
#                 #arr[finishrow+j+1][finishrow-i+1].append(arr[i][j])
#                 arr[finishrow+j+1].append(arr[i][j])
#             arr[i]=[]
#         startrow=finishrow+1
#         finishrow+=len_
#     return startrow,finishrow

# def organize(startrow,finishrow, status):
#     global arr
#     # tmp=[[0]*len(arr[startrow]) for _ in range()]
#     tmp=[row[:] for row in arr]

#     colsize=len(arr[startrow])
#     for i in range(startrow,finishrow+1): # horizon, vertical
#         for j in range(colsize):
#             if j+1<colsize and abs(arr[i][j]-arr[i][j+1])>=5:
#                 d=int(abs(arr[i][j]-arr[i][j+1])/5)
#                 if arr[i][j]>arr[i][j+1]:
#                     tmp[i][j]-=d
#                     tmp[i][j+1]+=d
#                 else:
#                     tmp[i][j]+=d
#                     tmp[i][j+1]-=d
#             if i+1<=finishrow and abs(arr[i][j]-arr[i+1][j])>=5:
#                 d=int(abs(arr[i][j]-arr[i+1][j])/5)
#                 if arr[i][j]>arr[i+1][j]:
#                     tmp[i][j]-=d
#                     tmp[i+1][j]+=d
#                 else:
#                     tmp[i][j]+=d
#                     tmp[i+1][j]-=d

#     if status==True:
#         for i in range(finishrow,numarr-1):
#             if abs(arr[i][0]-arr[i+1][0])>=5:
#                 d=int(abs(arr[i][0]-arr[i+1][0])/5)
#                 if arr[i][0]>arr[i+1][0]:
#                     tmp[i][0]-=d
#                     tmp[i+1][0]+=d
#                 else:
#                     tmp[i][0]+=d
#                     tmp[i+1][0]-=d
#     arr=tmp
#     return

# def resort(startrow,finishr_):
#     global arr
#     tmp=[[0] for _ in range(numarr)]
#     i=0
#     for r in range(startrow,finishr_):
#         for v in arr[r]:
#             tmp[i][0]=v
#             i+=1
#     arr=tmp
#     return



# times=0
# while True:
#     tmp=[max(row) for row in arr]
#     if max(tmp)-min(tmp)<=K:
#         print(times)
#         print(arr)
#         break
#     times+=1

#     #add fish
#     minfish=min(tmp)
#     for i in range(numarr):
#         if arr[i][0]==minfish:
#             arr[i][0]+=1

#     # stack fish house
#     s,f=stack()
#     # adjust fish num
#     organize(s,f,True)
#     # resort fish
#     resort(s,numarr)

#     # fold
#     a=int(numarr/4)
#     b=int(numarr/a)
#     direc=[()]
#     tmp=[[0]*b for _ in range(int(numarr/4))]
#     for i in range(0,a):
#         tmp[a-i-1][1]=arr[i][0]
#     for i in range(0,a):
#         tmp[i-a][2]=arr[a+i][0]
#     for i in range(0,a):
#         tmp[a-i-1][3]=arr[2*a+i][0]
#     for i in range(0,a):
#         tmp[i-a][0]=arr[3*a+i][0]
#     arr=tmp

#     # adjust
#     organize(0,a-1,False)
#     resort(0,a)


    
