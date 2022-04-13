
###############################22.04.13
from numpy import sort


RR,CC,KK=map(int,input().split(' '))
arr=[[0]*100 for _ in range(100)]
for i in range(3):
    tmp=list(map(int,input().split(' ')))
    for j in range(3):
        arr[i][j]=tmp[j]

answer=-1
R=3
C=3
for time_ in range(101):
    if arr[RR-1][CC-1]==KK:
        answer=time_
        break
    
    if R>=C:
        for i in range(R):
            nums={}
            for j in range(C):
                if arr[i][j]==0:continue
                nums.setdefault(arr[i][j],0)
                nums[arr[i][j]]+=1
            
            tmp=[]
            for n,v in nums.items():
                tmp.append((n,v))
            tmp=sorted(tmp,key=lambda x:(x[1],x[0]))

            C=max(C,2*len(tmp))
            for j in range(len(tmp)):
                n,v=tmp[j]
                arr[i][2*j]=n
                arr[i][2*j+1]=v
            for j in range(len(tmp)*2,C):
                arr[i][j]=0

    elif R<C:
        for j in range(C):
            nums={}
            for i in range(R):
                if arr[i][j]==0:continue
                nums.setdefault(arr[i][j],0)
                nums[arr[i][j]]+=1
            
            tmp=[]
            for n,v in nums.items():
                tmp.append((n,v))
            tmp=sorted(tmp,key=lambda x:(x[1],x[0]))

            R=max(R,2*len(tmp))
            for i in range(len(tmp)):
                n,v=tmp[i]
                arr[2*i][j]=n
                arr[2*i+1][j]=v
            for i in range(len(tmp)*2,R):
                arr[i][j]=0

print(answer)



################################################

# # RR,CC,KK=map(int,input().split(' '))
# # arr=[[0]*100 for _ in range(100)]
# # for i in range(3):
# #     tmp=list(map(int,input().split(' ')))
# #     for j in range(3):
# #         arr[i][j]=tmp[j]

# RR,CC,KK=1,2,3
# arr=[[0]*100 for _ in range(100)]
# arr[0][0],arr[0][1],arr[0][2]=1,2,3
# arr[1][0],arr[1][1],arr[1][2]=4,5,6
# arr[2][0],arr[2][1],arr[2][2]=7,8,9

# Rlen,Clen=3,3
# answer=-1
# for time in range(101):
#     if arr[RR-1][CC-1]==KK:
#         answer=time
#         break
#     if time==100:
#         break
#     if Rlen>=Clen:
#         for r in range(Rlen):
#             tmp={}
#             for c in range(Clen):
#                 v=arr[r][c]
#                 if v==0: continue
#                 if v in tmp: tmp[v]+=1
#                 else:  tmp[v]=1

#             sorttmp=sorted(tmp.items(),key=lambda x:(x[1],x[0]))
#             Clen=max(Clen,len(sorttmp)*2) #update
#             for i in range(min(len(sorttmp),50)):
#                 a,b=sorttmp[i]
#                 arr[r][2*i]=a
#                 arr[r][2*i+1]=b
#             for i in range(min(len(sorttmp)*2,100),Rlen):
#                 arr[r][i]=0
#     else:
#         for c in range(Clen):
#             tmp={}
#             for r in range(Rlen):
#                 v=arr[r][c]
#                 if v==0: continue
#                 if v in tmp: tmp[v]+=1
#                 else: tmp[v]=1
            
#             sorttmp=sorted(tmp.items(),key=lambda x:(x[1],x[0]))
#             Rlen=max(Rlen,len(sorttmp)*2) #update
#             for i in range(min(len(sorttmp),50)):
#                 a,b=sorttmp[i]
#                 arr[2*i][c]=a
#                 arr[2*i+1][c]=b
#             for i in range(min(len(sorttmp)*2,100),Rlen):
#                 arr[i][c]=0
                
# print(answer)



