s="ABCD"
numRows=3

if numRows==1:
    print(s)
else:
    a=2*(numRows-1)
    halfa=(int)(a/2)
    lenS=len(s)
    answer=""
    for b in range(0,halfa+1):
        if b==0 or b==halfa:
            for i in range(lenS):
                if a*i+b>=lenS:
                    break
                answer+=s[a*i+b]
        else :     
            for i in range(lenS):
                if a*i+b >= lenS:
                    break
                answer+=s[a*i+b]
                if a*i+a-b >= lenS:
                    break
                answer+=s[a*i+a-b]
    print(answer)