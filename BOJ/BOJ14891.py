import sys
from collections import deque

arr=[deque([]) for _ in range(4)]
for i in range(4):
    tmp=sys.stdin.readline().strip() #.split(' ')
    for j in range(8):
        arr[i].append(tmp[j])
# arr=[sys.stdin.readline().strip().split(' ') for _ in range(4)]
#print(arr)
K=int(input())

# arr=[deque(['1', '0', '1', '0', '1', '1', '1', '1']), deque(['0', '1', '1', '1', '1', '1', '0', '1']), deque(['1', '1', '0', '0', '1', '1', '1', '0']), deque(['0', '0', '0', '0', '0', '0', '1', '0'])]
# K=2
# hello=[(3,-1),(1,1)]

for k in range(K):
    num,direc=list(map(int,sys.stdin.readline().strip().split(' ')))
# for k in range(K):
#     num,direc=hello[k]

    #find rotate direction
    rot=[0,0,0,0]
    rot[num-1]=direc
    dq=deque([(num-1,direc)])
    while dq:
        x,d=dq.popleft()
        for dx in [-1,1]:
            nx=x+dx
            if 0<=nx<4 and rot[nx]==0:
                if dx==-1 and arr[x][6]!=arr[nx][2]: #left
                    rot[nx]=-1*d
                    dq.append((nx,-1*d))
                elif dx==1 and arr[x][2]!=arr[nx][6]: #right
                    rot[nx]=-1*d
                    dq.append((nx,-1*d))
    
    #rotate
    for i in range(4):
        arr[i].rotate(rot[i])

#calculate score
answer=0
for i in range(4):
    answer+=int(arr[i][0])*(2**i) #if N=0, S=1
print(answer)