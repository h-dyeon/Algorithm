dominoes = "..R.."

i=0
while i<len(dominoes):
    nexti=i+1
    before=dominoes
    if dominoes[i]=='.':
        if i==0:
            for j in range(i+1,len(dominoes)):
                if dominoes[j]=='R':
                    nexti=j
                    break
                elif dominoes[j]=='L':
                    dominoes='L'*j+dominoes[j:]
                    nexti=j
                    break
                elif j==len(dominoes)-1:
                    nexti=j
        elif dominoes[i-1]=='L':
            for j in range(i+1,len(dominoes)):
                if dominoes[j]=='R':
                    nexti=j
                    break
                elif dominoes[j]=='L':
                    dominoes=dominoes[0:i]+'L'*(j-i)+dominoes[j:]
                    nexti=j
                    break
                elif j==len(dominoes)-1:
                    nexti=j
        elif dominoes[i-1]=='R':
            for j in range(i,len(dominoes)):
                if dominoes[j]=='R':
                    dominoes=dominoes[0:i]+'R'*(j-i)+dominoes[j:]
                    nexti=j
                    break
                elif dominoes[j]=='L':
                    numOfDot=(j-i)
                    mid=int((j-i)/2)
                    if numOfDot%2==0:
                        dominoes=(dominoes[0:i]+
                                    'R'*mid+'L'*mid+
                                    dominoes[j:])     
                    elif numOfDot%2==1:
                        dominoes=(dominoes[0:i]+
                                    'R'*mid+'.'+'L'*mid+
                                    dominoes[j:])
                    nexti=j
                    break
                if j==len(dominoes)-1:
                    dominoes=dominoes[0:i]+'R'*(j-i+1)
    i=nexti

print(dominoes)