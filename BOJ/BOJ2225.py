N,K=map(int,input().split(' '))

combi=[[i+1 for i in range(K)] ,[0 for _ in range(K)]]
m=1000000000
bi=0

print(combi)
for i in range(1,N):        
    bi_=bi
    bi=1 if bi==0 else 0
    for j in range(K):
        if j==0:
            combi[bi][j]=combi[bi_][j]
        else:
            combi[bi][j]=((combi[bi][j-1]%m)+(combi[bi_][j]%m))%m    
    print(i,combi[bi])
print(combi[bi][K-1])
# print(combi[bi][K-1])
# for i in range(2,N+2):
#     bi_=bi
#     bi=1 if bi==0 else 0
#     for j in range(i+1):
#         if j==0:
#             combi[bi][j]=combi[bi_][j]
#         else:
#             combi[bi][j]=((combi[bi_][j-1]%m)+(combi[bi_][j]%m))%m    
#     print(i,combi[bi])
# print(combi[bi][K-1])