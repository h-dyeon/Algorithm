N,K=map(int,input().split(' '))
arr=[]
tmp=list(map(int,input().split(' ')))
for t in tmp:
    arr.append([t])
# print(arr)


# N,K=8,7
# arr=[[5],[2],[3],[14],[9],[2],[11],[8]]
numarr=len(arr)


def stack():
    startrow=0
    finishrow=0
    while len(arr[finishrow])<=(numarr-1-finishrow):
        len_=len(arr[finishrow])
        for i in range(finishrow,startrow-1,-1):
            for j in range(len(arr[i])):
                #arr[finishrow+j+1][finishrow-i+1].append(arr[i][j])
                arr[finishrow+j+1].append(arr[i][j])
            arr[i]=[]
        startrow=finishrow+1
        finishrow+=len_
    return startrow,finishrow

def organize(startrow,finishrow, status):
    global arr
    # tmp=[[0]*len(arr[startrow]) for _ in range()]
    tmp=[row[:] for row in arr]

    colsize=len(arr[startrow])
    for i in range(startrow,finishrow+1): # horizon, vertical
        for j in range(colsize):
            if j+1<colsize and abs(arr[i][j]-arr[i][j+1])>=5:
                d=int(abs(arr[i][j]-arr[i][j+1])/5)
                if arr[i][j]>arr[i][j+1]:
                    tmp[i][j]-=d
                    tmp[i][j+1]+=d
                else:
                    tmp[i][j]+=d
                    tmp[i][j+1]-=d
            if i+1<=finishrow and abs(arr[i][j]-arr[i+1][j])>=5:
                d=int(abs(arr[i][j]-arr[i+1][j])/5)
                if arr[i][j]>arr[i+1][j]:
                    tmp[i][j]-=d
                    tmp[i+1][j]+=d
                else:
                    tmp[i][j]+=d
                    tmp[i+1][j]-=d

    if status==True:
        for i in range(finishrow,numarr-1):
            if abs(arr[i][0]-arr[i+1][0])>=5:
                d=int(abs(arr[i][0]-arr[i+1][0])/5)
                if arr[i][0]>arr[i+1][0]:
                    tmp[i][0]-=d
                    tmp[i+1][0]+=d
                else:
                    tmp[i][0]+=d
                    tmp[i+1][0]-=d
    arr=tmp
    return

def resort(startrow,finishr_):
    global arr
    tmp=[[0] for _ in range(numarr)]
    i=0
    for r in range(startrow,finishr_):
        for v in arr[r]:
            tmp[i][0]=v
            i+=1
    arr=tmp
    return



times=0
while True:
    tmp=[max(row) for row in arr]
    if max(tmp)-min(tmp)<=K:
        print(times)
        print(arr)
        break
    times+=1

    #add fish
    minfish=min(tmp)
    for i in range(numarr):
        if arr[i][0]==minfish:
            arr[i][0]+=1

    # stack fish house
    s,f=stack()
    # adjust fish num
    organize(s,f,True)
    # resort fish
    resort(s,numarr)

    # fold
    a=int(numarr/4)
    b=int(numarr/a)
    direc=[()]
    tmp=[[0]*b for _ in range(int(numarr/4))]
    for i in range(0,a):
        tmp[a-i-1][1]=arr[i][0]
    for i in range(0,a):
        tmp[i-a][2]=arr[a+i][0]
    for i in range(0,a):
        tmp[a-i-1][3]=arr[2*a+i][0]
    for i in range(0,a):
        tmp[i-a][0]=arr[3*a+i][0]
    arr=tmp

    # adjust
    organize(0,a-1,False)
    resort(0,a)


    
