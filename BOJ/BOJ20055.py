
####################################################22.04.15
from collections import deque
N,K=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))


# N,K=4,5
# arr=[10, 1, 10, 6, 3, 4, 8, 2]
# N,K=3,2
# arr=[1,2,1,2,1,2]
# N,K=3,6
# arr=[10,10,10,10,10,10]

robot=deque([0 for _ in range(N)])
# robot=[0]*N
belt_s=0
belt_f=N-1

answer=0
step=0
while True:
    if arr.count(0)>=K:
        answer=step
        break
    step+=1

    # step 1
    belt_s=(belt_s-1)%(2*N)
    belt_f=(belt_f-1)%(2*N)
    robot.rotate(1)
    robot[N-1]=0
    # robot=robot[-1:]+robot[:-1]
    # robot[N-1]=0 #last robot

    # step 2
    for i in range(N-1,0,-1):
        if robot[i-1]==1 and robot[i]==0 and arr[(belt_s+i)%(2*N)]>0:
            robot[i-1]=0
            robot[i]=1
            arr[(belt_s+i)%(2*N)]-=1
    robot[N-1]=0  #last robot

    # step 3
    if arr[belt_s]>0:
        arr[belt_s]-=1
        robot[0]=1

print(answer)



####################################################3
# N,K=map(int,input().split(' '))
# arr=list(map(int,input().split(' ')))
# print(arr)

# # N,K=4,5
# # arr=[10, 1, 10, 6, 3, 4, 8, 2]

# robots=[0]*N

# step=1
# while True:
#     # 1
#     robots[-1]=0 #last robot
#     robots=robots[-1:]+robots[:-1]
#     arr=arr[-1:]+arr[:-1]
#     # print("robots",robots)
#     # print("arr",arr)

#     # 2
#     robots[-1]=0
#     for i in range(N-2,-1,-1):
#         if robots[i]==1 and robots[i+1]==0 and arr[i+1]>0:
#             robots[i]=0
#             robots[i+1]=1
#             arr[i+1]-=1

#     # 3
#     if arr[0]!=0:
#         robots[0]=1
#         arr[0]-=1

#     # 4
#     if arr.count(0)>=K:
#         break
#     else:
#         step+=1


# print(step)
