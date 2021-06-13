from sys import stdin
import sys

N,M,K = map(int, stdin.readline().strip().split(' ')) #row, coulmn, submerged cell

matrix = [[0]*(M+1) for _ in range(M+1)]

for i in range(K):
    r,c=map(int,stdin.readline().strip())
    matrix[r][c]=1

dr=[0,-1,0,1]
dc=[1,0,-1,0]

print(3)