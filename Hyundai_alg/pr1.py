from collections import deque
def solution(a):
    def findsol(s):
        dq=deque([s])
        while len(dq)!=0:
            tmp=dq.popleft()
            if tmp.count('a')==0 or tmp.count('b')%2!=0:
                return False
            if tmp.count('b')==0:
                return True

            #remove all side a
            tmp=tmp[tmp.find('b'):tmp.rfind('b')+1]

            #rule 1
            numA=tmp.count('a')
            if numA!=0:
                while tmp[0]!='a' or tmp[-1]!='a':
                    if tmp[0:numA].count('b') == numA and tmp[len(tmp)-numA:len(tmp)].count('b')==numA:
                        tmp=tmp[numA:len(tmp)-numA]
                dq.append(tmp)
        return False

    answer = []
    for s in a:
        answer.append(findsol(s))
    return answer



tmp=["abab", "bbaa", "bababa", "bbbabababbbaa"]
print(solution(tmp))

# # 시간초과 3개
# from collections import deque
# def solution(a):
#     def findsol(s):
#         dq=deque([s])
#         while len(dq)!=0:
#             tmp=dq.popleft()
#             if tmp.count('a')==0 or tmp.count('b')%2!=0:
#                 return False
#             if tmp.count('b')==0:
#                 return True

#             #remove all side a
#             tmp=tmp[tmp.find('b'):tmp.rfind('b')+1]

#             #rule 1
#             numA=tmp.count('a')
#             if numA!=0 and tmp[0:numA].count('b') == numA and tmp[len(tmp)-numA:len(tmp)].count('b')==numA:
#                 dq.append(tmp[numA:len(tmp)-numA])
#         return False

#     answer = []
#     for s in a:
#         answer.append(findsol(s))
#     return answer


# 시간초과 11개
# from collections import deque
# def solution(a):
#     def findsol(s):
#         if s.count('b')==0:
#             return True
#         if s.count('b')%2!=0:
#             return False
#         dq=deque([s])
#         while len(dq)!=0:
#             tmp=dq.popleft()

#             #rule 1
#             numA=tmp.count('a')
#             if numA!=0 and tmp[0:numA].count('b') == numA and tmp[len(tmp)-numA:len(tmp)].count('b')==numA:
#                 if tmp[numA:len(tmp)-numA]=='a':
#                     return True
#                 else:
#                     dq.append(tmp[numA:len(tmp)-numA])
#             #rule 2-1
#             if tmp[0]=='a':
#                 if tmp[1:] =='a':
#                     return True
#                 else:
#                     dq.append(tmp[1:])
#             #rule 2-2
#             if tmp[-1]=='a':
#                 if tmp[0:len(tmp)-1]=='a':
#                     return True
#                 else:
#                     dq.append(tmp[0:len(tmp)-1])
#         return False

#     answer = []
#     for s in a:
#         answer.append(findsol(s))
#     return answer