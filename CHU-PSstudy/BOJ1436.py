# N=int(input())
# print(N)
N=10000

cnt=0
for i in range(665,100000000):
    if '666' in str(i):
        cnt+=1
        print(cnt,str(i))
        if cnt==N:
            print(i)
            break