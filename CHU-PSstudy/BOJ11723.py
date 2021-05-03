import sys
S=0
M=int(sys.stdin.readline().strip())
for i in range(0,M):
    t=sys.stdin.readline().strip()
    if t.find(' ')>=0:
        t,x=t.split()
        x=int(x)-1

    if t=="add":
        S |= (1<<x)
    elif t=="remove":
        S &= ~(1<<x)
    elif t=="check":
        if S & (1<<x) :
            print(1)
        else:
            print(0)
    elif t=="toggle":
        S ^= (1<<x)
    elif t=="all":
        S=(1<<20)-1
    elif t=="empty":
        S=0
