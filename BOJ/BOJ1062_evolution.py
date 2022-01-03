from sys import stdin
import sys

def getbitmask(txt):
    tmp=0
    for j in range(0,len(txt)):
        tmp |= (1<< (ord(txt[j])-97))
    return tmp

def bitcount(num):
    if num == 0:
        return 0
    return num % 2 + bitcount(int(num/2))

def dfs(idx, cnt,select,answer):
    if cnt==K:
        tmp=0
        for b in wordsBitmask:
            if (b & ~select ) ==0:
                tmp+=1
        return max(tmp,answer)
    for i in range(idx,26):
        if (totalBitmask & (1<<i)) == 0 :
            continue
        if (select & (1<<i)) > 0:
            continue
        select |= (1<<i)
        answer=dfs(i, cnt+1, select, answer)
        select &= ~(1<<i)
    return answer

N, K = list(map(int, stdin.readline().strip().split(' ')))
K -= 5

words = [stdin.readline().strip()[4:-4] for _ in range(N)]
wordsBitmask=[]
totalBitmask=0
must=getbitmask('actin')

# get bitmask of each word
for word in words:
    bitmask=0
    for char in word:
        bitmask |= (1<< (ord(char)-97))
    bitmask &= ~must
    wordsBitmask.append(bitmask)
    totalBitmask |= bitmask

# test the number of character
if K<0:
    print(0)
elif K==21:
    print(N)
elif bitcount(totalBitmask) <= K:
    print(N)
else :
    print(dfs(0,0,0,0))
