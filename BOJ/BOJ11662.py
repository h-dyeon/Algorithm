import sys

ax,ay,bx,by,cx,cy,dx,dy=map(int,sys.stdin.readline().strip().split(" "))

def func(t):
    deltaX=((1-t)*cx+t*dx) - ((1-t)*ax+t*bx)
    deltaY=((1-t)*cy+t*dy) - ((1-t)*ay+t*by)
    return (deltaX**2 + deltaY**2) ** 0.5

def ternary(lo,hi):
    for i in range(100):
        a=(2*lo + hi)/3
        b=(lo+2*hi)/3
        if func(a)<func(b):
            hi=b
        else:
            lo=a
    return (lo+hi)/2

t=ternary(0,1)
print(func(t))
