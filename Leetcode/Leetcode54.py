class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        visited=[[0 for _ in range(cols)]for _ in range(rows)]

        dr=[0,1,0,-1]
        dc=[1,0,-1,0]
        mode=0
        r,c,check=0,0,0 #row, col, check
        
        answer=[]
        while True:
            answer.append(matrix[r][c])
            visited[r][c]=1
            check+=1
            if check==(rows*cols):
                break
            
            if ((mode==0 and c+1==cols) or 
                (mode==1 and r+1==rows) or 
                (mode==2 and c==0) or 
                (mode==3 and r==0)) :
                    mode=(mode+1)%4
            
            tr=r+dr[mode]
            tc=c+dc[mode]
            if (0>r or r>=rows or 0>c or c>=cols or visited[tr][tc]==1):
                mode=(mode+1)%4
            r+=dr[mode]
            c+=dc[mode]

        return answer
            