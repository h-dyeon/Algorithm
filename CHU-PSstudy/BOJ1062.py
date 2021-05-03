from sys import stdin

def bitcount(num):
    if num == 0:
        return 0
    return num % 2 + bitcount(int(num/2))

def getbin(txt):
    tmp=0
    for j in range(0,len(txt)):
        tmp |= (1<< (ord(txt[j])-97))
    #print("txt=",txt,"bin=",bin(tmp).rjust(26))
    return tmp

def dfs(idx, cnt,select,answer):
    if cnt==K-5:
        #print("idx=",idx,"cnt=",cnt,"select=",bin(select))
        tmp=0
        for idx in range(len(arr)):
            if (arr[idx] & ~(select|actin)) == 0 :
                tmp=tmp+1
        return max(tmp,answer)
    for i in range(idx,26):
        if (total_bin & (1<<i)) == 0 :
            continue
        if (select & (1<<i)) >0:
            continue
        select |= (1<<i)
        answer=dfs(i, cnt+1, select,answer)
        select &= ~(1<<i)
    return answer

def preprocessing(words):
    arr=[]
    total=0
    actin=getbin('actin')
    for i in range(0,N):
        txt2bin=getbin(words[i][4:len(words[i])-4])
        txt2bin &= ~actin
        arr.append(txt2bin)
        total |= txt2bin
    return arr,total

actin=getbin('actin')
N, K = list(map(int, stdin.readline().strip().split(' ')))
words = [stdin.readline().strip() for _ in range(N)]
arr,total_bin=preprocessing(words)
total_bitcount=bitcount(total_bin)

if K < 5:
    print(0)
elif total_bitcount==0 or total_bitcount + 5 <= K :
    print(N)
else :
    print(dfs(0,0,0,0))