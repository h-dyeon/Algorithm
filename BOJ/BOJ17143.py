
######################################################22.04.18
R,C,M=map(int,input().split(' '))
# shark_pos=[[0,0] for _ in range(M)]
shark_sd={}
arr={}
for _ in range(M):
    r,c,s,d,z=map(int,input().split(' '))
    arr.setdefault((r-1,c-1),0)
    arr[(r-1,c-1)]=z
    shark_sd.setdefault(z,[0,0])
    shark_sd[z]=[s,d-1]

def calcpos(r,c,s,d):
    if d==0 or d==1: #up, down
        s=s%(2*R-2)
        
    else: # d==2,3 left,right
        s=s%(2*C-2)
    
    return nr,nc,nd


answer=0
person=-1
while person!=C:
    person+=1
    for r in range(R):
        if (r,person) in arr:
            gotshark=arr[(r,person])]
            answer+=gotshark
            del arr[(r,person])]
    # move
    tmp={}
    for r in range(R):
        for c in range(C):
            if (r,c) in arr:
                shark=arr[(r,c)]
                s,d=shark_sd[shark-1]
                nr,nc,nd=calcpos(r,c,s,d)
                
                if (nr,nc) in tmp:
                    beforeshark=tmp[(nr,nc)]
                    if beforeshark<shark:
                        tmp[(nr,nc)]=shark
                else:
                    tmp[(nr,nc)]=shark
    arr=tmp

print(answer)
                




######################################################3

# R,C,M=map(int,input().split(' '))
# sharks={}
# for _ in range(M):
#     r,c,s,d,z=map(int,input().split(' '))
#     sharks.setdefault((r-1,c-1),[]).append((s,d,z))
# dr=[-1,1,0,0]
# dc=[0,0,1,-1]

# # R,C,M=2,2,4
# # sharks={(0, 0): [(1, 1, 1)], (1, 1): [(2, 2, 2)], (0, 1): [(1, 2, 3)], (1, 0): [(2, 1, 4)]}
# # R,C,M=4,6,8
# # sharks={(3, 0): [(3, 3, 8)], (0, 2): [(5, 2, 9)], (1, 3): [(8, 4, 1)], (3, 4): [(0, 1, 4)], (2, 2): [(1, 2, 7)], (0, 4): [(8, 4, 3)], (2, 5): [(2, 1, 2)], (1, 1): [(2, 3, 5)]}


# # def getpos(r,c,d,s):
# #     if d==1 or d==2:
# #         s=s%(2*R-2)
# #     elif d==3 or d==4:
# #         s=s%(2*C-2)
# #     for _ in range(s):
# #         if 0<=r+dr[d-1]<R and 0<=c+dc[d-1]<C:
# #             r,c=r+dr[d-1],c+dc[d-1]
# #         else:
# #             if d==3: d=4
# #             elif d==4: d=3
# #             elif d==1: d=2
# #             elif d==2: d=1
# #             r,c=r+dr[d-1],c+dc[d-1]
# #     return r,c,d

# def getpos(r,c,d,s):
#     if d==1 or d==2:
#             s=s%(2*R-2)
#     elif d==3 or d==4:
#         s=s%(2*C-2)

#     if d==1:
#         if s<=r:
#             r-=s
#         elif s>(2*R-2)-(R-r-1):
#             r=(2*R-2)-s+r
#         else:
#             d=2
#             r=(s-r)%R
#     elif d==2:
#         if s<=R-r-1:
#             r+=s
#         elif s>=(2*R-2)-r+1:
#             r-=((2*R-2)-s)
#         else:
#             d=1
#             r=R-(s-(R-r-1))-1
#     elif d==3:
#         if s<=C-c-1:
#             c+=s
#         elif s>=(2*C-2)-c+1:
#             c-=((2*C-2)-s)
#         else:
#             d=4
#             c=C-(s-(C-c-1))-1
#     elif d==4:
#         if s<=c:
#             c-=s
#         elif s>(2*C-2)-(C-c-1):
#             c=(2*C-2)-s+c
#         else:
#             d=3
#             c=(s-c)%C
#     return r,c,d

# # a=3
# # fff=4
# # print(0,0,"->",getpos(0,0,fff,a))
# # print(0,1,"->",getpos(0,1,fff,a))
# # print(0,2,"->",getpos(0,2,fff,a))
# # print(0,3,"->",getpos(0,3,fff,a))


# answer=0
# for t in range(C):
#     # got shark
#     for r in range(R):
#         if (r,t) in sharks:
#             answer+=sharks[(r,t)][0][2]
#             del sharks[(r,t)]
#             break
    
#     # move shark
#     nshark={}
#     for (r,c),item in sharks.items():
#         s,d,z=item[0]
#         nr,nc,nd=getpos(r,c,d,s)
#         nshark.setdefault((nr,nc),[]).append((s,nd,z))
#     sharks=nshark

#     # del shark
#     tmp=sharks.keys()
#     for r,c in tmp:
#         if len(sharks[(r,c)])>1:
#             sharks[(r,c)]=sorted(sharks[(r,c)],key=lambda x : -x[2])
#             s,d,z=sharks[(r,c)][0]
#             sharks[(r,c)]=[(s,d,z)]

# print(answer)
