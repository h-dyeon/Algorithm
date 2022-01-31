class Solution:
    def solveEquation(self, equation: str) -> str:

        def splitByMinus(str):
            answer=[]
            check=0
            for i in range(1,len(str)):
                if str[i]=="-":
                    answer.append(str[check:i])
                    check=i
            answer.append(str[check:len(str)])
            return answer

        def splitByPlus(strlist):
            coefficient=0
            constant=0
            for i in strlist:
                tmp=i.split("+")
                for j in tmp:
                    if "x" in j:
                        if "x"==j: coefficient+=1
                        elif "-x"==j:coefficient-=1
                        else : coefficient+=int(j[0:-1])
                    else:
                        constant+=int(j)
            return coefficient,constant

        tmp=equation.split("=")
        a,b=splitByPlus(splitByMinus(tmp[0]))
        c,d=splitByPlus(splitByMinus(tmp[1]))

        coe=a-c
        con=d-b

        answer=""
        if coe==0 and con!=0:
            answer="No solution"
        elif coe==0 and con==0:
            answer="Infinite solutions"
        else:
            answer="x="+str(int(con/coe))

        return answer