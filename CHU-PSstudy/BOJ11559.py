import sys
from collections import deque
C=12
R=6

# origin=[sys.stdin.readline().strip() for _ in range(12)]
# print(origin)

# 반례들
#origin=['......', '......', '......', '......', '......', '......', '......', '......', '......', '......', 'RRYY..', 'RRYY..'] #답 1
#origin=['......', '......', '......', '......', '......', '....Y.', '....Y.', '....Y.', '....RR', '...YRR', '..GGYY', '..GGYY'] #답 2
#origin=['RRRRRR', 'RRRRRR', 'RRRRRR', 'RRRRRR', 'RRRRRR', 'RRRRRR', 'RRRRRR', 'RRYYRR', 'RRGGRR', 'RRRRRR', 'RRYYRR', 'RRGGRR'] #답 1
#origin=['RRRRRR', 'RRRRRR', 'RRRRRR', 'RRRRRR', 'RRRRRR', 'RRBBRR', 'RRRRRR', 'RRRRRR', 'RRRRRR', 'RRBBRR', 'RRRRRR', 'RRRRRR'] #답 2
#origin=['......', '......', '......', '......', '......', '......', '......', '......', '.Y....', '.YG...', 'RRYG..', 'RRYGG.'] #답 3

#transpose
matrix=["" for _ in range(R)]
for j in range(R):
    for i in range(C):
        matrix[j] +=origin[11-i][j]


def dfs(rr,cc,mychar):
    dq=deque([[rr,cc]]) # row, col
    bomb=deque([[rr,cc]])
    while len(dq)!=0:
        tr,tc=dq.popleft()
        for i in range(4):
            newR=tr+dr[i]
            newC=tc+dc[i]
            if 0<=newR<R and 0<=newC<C and matrix[newR][newC]==mychar and [newR,newC] not in bomb:
                dq.append([newR,newC])
                bomb.append([newR,newC])
    return bomb


#calculate
dr=[-1,0,1,0]
dc=[0,1,0,-1]
chars="RGBPY"
answer=0

while True:
    tmp=0
    for i in range(R):
        for j in range(C):
            if matrix[i][j]=='.':
                break
            if matrix[i][j] in chars:
                bomb=dfs(i,j,matrix[i][j])
                if len(bomb)>=4: #delete bomb
                    tmp+=1
                    while len(bomb)>0:
                        rr,cc=bomb.popleft()
                        matrix[rr]=matrix[rr][0:cc]+" "+matrix[rr][cc+1:12]
    if tmp==0:
        break
    else: #reset blank
        answer+=1
        for z in range(R):
            matrix[z]=matrix[z].replace(' ','')
            matrix[z]+="."*(C-len(matrix[z]))   
print(answer)



# 문제를 잘못 이해해서 틀린 코드
# j=0
# while j<C:
#     i=0
#     while i<R:
#         #print(j,i)
#         if matrix[i][j] in chars:
#             bomb=dfs(i,j,matrix[i][j])
#             if len(bomb)>=4:
#                 answer+=1
#                 #delete bomb
#                 while len(bomb)>0:
#                     rr,cc=bomb.popleft()
#                     matrix[rr]=matrix[rr][0:cc]+" "+matrix[rr][cc+1:12]
#                 #reset blank
#                 for z in range(R):
#                     matrix[z]=matrix[z].replace(' ','')
#                     matrix[z]+="."*(C-len(matrix[z]))
#                 #re-find from (0,0)
#                 i=-1
#                 j=0
#         i+=1
#     j+=1

# print(answer)


