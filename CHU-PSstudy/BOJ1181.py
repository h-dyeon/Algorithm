from sys import stdin
import sys

N = int(stdin.readline().strip())

wordlist = list(set([stdin.readline().strip() for _ in range(N)]))
wordlist.sort(key=lambda x : len(x))

# def quicksort(left,right):
#     if right<=left:
#         return
#     print("left=",left,"right=",right)
#     pivot=left
#     low=left+1
#     high=right
#     print("p=",pivot,"low=",low,"high=",high)
#     while low < high :
#         while len(wordlist[pivot]) >=  len(wordlist[low]) and low<=right:
#             low += 1
#         while len(wordlist[pivot]) <= len(wordlist[high]) and high>=pivot:
#             high -= 1
#         if low>high:
#             break
#         wordlist[low], wordlist[high] = wordlist[high], wordlist[low]
#     wordlist[pivot],wordlist[high]=wordlist[high],wordlist[pivot]
#     quicksort(left,high-1)
#     quicksort(low,right)
# quicksort(0,len(wordlist)-1)


# for i in range(0, len(wordlist)):
#     for j in range(i+1, len(wordlist)):
#         a=wordlist[i]
#         b=wordlist[j]
#         if len(a) > len(b):
#             wordlist[i],wordlist[j]=wordlist[j],wordlist[i]
#         elif len(a) == len(b):
#             tmp=[a,b]
#             tmp.sort()
#             if tmp[0] != a :
#                 wordlist[i],wordlist[j]=wordlist[j],wordlist[i]

for w in wordlist:
    print(w)