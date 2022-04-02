N,K=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
print(arr)

# N,K=4,5
# arr=[10, 1, 10, 6, 3, 4, 8, 2]

robots=[0]*N

step=1
while True:
    # 1
    robots[-1]=0 #last robot
    robots=robots[-1:]+robots[:-1]
    arr=arr[-1:]+arr[:-1]
    # print("robots",robots)
    # print("arr",arr)

    # 2
    robots[-1]=0
    for i in range(N-2,-1,-1):
        if robots[i]==1 and robots[i+1]==0 and arr[i+1]>0:
            robots[i]=0
            robots[i+1]=1
            arr[i+1]-=1

    # 3
    if arr[0]!=0:
        robots[0]=1
        arr[0]-=1

    # 4
    if arr.count(0)>=K:
        break
    else:
        step+=1


print(step)
