from sys import stdin
import sys

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())

matrix = [[0]*(N+1) for _ in range(N+1)]
for n in range(0,M):
    i,j = map(int, stdin.readline().strip().split(' '))
    matrix[i][j]=1
    matrix[j][i]=1

queue=[1]
visited=set([1])
while queue:
    now=queue.pop(0)
    linked = set([i for i, x in enumerate(matrix[now]) if x == 1])
    notvisited=linked-visited
    queue += list(notvisited)
    visited |= linked

print(len(visited)-1)
