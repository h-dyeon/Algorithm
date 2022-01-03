import sys

def gcd(a,b): # a>b
    while b!=0:
        n=a%b
        a=b
        b=n
    return a    

def func(N,Pd,Pg):
    if Pd<100 and Pg==100:
        return False
    elif Pd>0 and Pg==0:
        return False

    if (100/gcd(100,Pd))<=N:
        return True
    return False

T=int(sys.stdin.readline().strip())
for i in range(T):
    N,Pd,Pg=map(int,sys.stdin.readline().strip().split(' '))
    print("Case #%d: %s"%(i+1, "Possible" if func(N,Pd,Pg) else "Broken"))



## wrong code
# import sys

# def gcd(a,b): # a>b
#     while b!=0:
#         n=a%b
#         a=b
#         b=n
#     return a    

# def func(N,Pd,Pg):
#     # calculate Pd
#     g=gcd(100,Pd)
#     m, n=100/g,Pd/g
#     if m>N:
#         return False
#     # calculate Pg
#     if n<=Pg <= (100-m)+n :
#         return True
#     return False


# print("gcd=%d,  %d/%d",gcd(100,0),100/gcd(100,0),0/gcd(100,0))

# T=int(sys.stdin.readline().strip())
# for i in range(T):
#     N,Pd,Pg=map(int,sys.stdin.readline().strip().split(' '))
#     print("Case #%d: %s"%(i+1, "Possible" if func(N,Pd,Pg) else "Broken"))
