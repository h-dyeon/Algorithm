def solution(dice):
    answer = 0
    total = 0
    dices=[0,0,0,0]
    for i in range(0,len(dice)):
        for j in range(6):
            total |= (1<<(dice[i][j]))
            dices[i] |= (1<<(dice[i][j]))

    if total != ((1<<10)-1):
        for i in range(1,10):
            if ((~total) & (1<<i)):
                return i

    def dfs(num,remainDice):
        status=False
        tmp=num%10
        for i in range(0,len(dice)):
            if status==True:
                break
            if (remainDice & (1<<i)) and (dices[i] & (1<<tmp)):
                if int(num/10)==0:
                    return True
                else :
                    status=dfs(int(num/10),remainDice & (~(1<<i)))
        return status

    for i in range(10,10000):
        if dfs(i,(1<<len(dice))-1) is not True:
            return i
    return 1000000

#tmp=[[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]
tmp=[[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]
print(solution(tmp))