T=int(input())

colors={0:'w',1:'y'}
face={ 'U':0,'D':1,'F':2,'B':3,'L':4,'R':5}


def rotate_face(cube,f,direc):
    tmp=[[0]*3 for _ in range(3)]
    if direc==0: #not clock
        for i in range(3):
            for j in range(3):
                tmp[2-j][i]=cube[f][i][j]
    elif direc==1: # clock
        for i in range(3):
            for j in range(3):
                tmp[j][2-i]=cube[f][i][j]
    cube[f]=tmp
    return

def initCube():
    arr=[[] for _ in range(6)]
    # for i in range(6):
    #     arr[i]=[[1,2,3],[4,5,6],[7,8,9]]
    arr[0]=[['w']*3 for _ in range(3)] #up
    arr[1]=[['y']*3 for _ in range(3)] #down
    arr[2]=[['r']*3 for _ in range(3)] #front
    arr[3]=[['o']*3 for _ in range(3)] #back
    arr[4]=[['g']*3 for _ in range(3)] #left
    arr[5]=[['b']*3 for _ in range(3)] #right
    return arr

def mrotate(cube,f,direc):
    rotate_face(cube,f,direc)
    if f==0: #up
        if direc==0: #L->F->R->B
            tmp=[cube[4][0][0],cube[4][0][1],cube[4][0][2]]
            cube[4][0][0],cube[4][0][1],cube[4][0][2]=cube[3][0][0],cube[3][0][1],cube[3][0][2]
            cube[3][0][0],cube[3][0][1],cube[3][0][2]=cube[5][0][0],cube[5][0][1],cube[5][0][2]
            cube[5][0][0],cube[5][0][1],cube[5][0][2]=cube[2][0][0],cube[2][0][1],cube[2][0][2]
            cube[2][0][0],cube[2][0][1],cube[2][0][2]=tmp[0],tmp[1],tmp[2]
        elif direc==1:#L<-F<-R<-B
            tmp=[cube[2][0][0],cube[2][0][1],cube[2][0][2]]
            cube[2][0][0],cube[2][0][1],cube[2][0][2]=cube[5][0][0],cube[5][0][1],cube[5][0][2]
            cube[5][0][0],cube[5][0][1],cube[5][0][2]=cube[3][0][0],cube[3][0][1],cube[3][0][2]
            cube[3][0][0],cube[3][0][1],cube[3][0][2]=cube[4][0][0],cube[4][0][1],cube[4][0][2]
            cube[4][0][0],cube[4][0][1],cube[4][0][2]=tmp[0],tmp[1],tmp[2]
    elif f==1: #down
        if direc==0: #L<-F<-R<-B
            tmp=[cube[2][2][0],cube[2][2][1],cube[2][2][2]]
            cube[2][2][0],cube[2][2][1],cube[2][2][2]=cube[5][2][0],cube[5][2][1],cube[5][2][2]
            cube[5][2][0],cube[5][2][1],cube[5][2][2]=cube[3][2][0],cube[3][2][1],cube[3][2][2]
            cube[3][2][0],cube[3][2][1],cube[3][2][2]=cube[4][2][0],cube[4][2][1],cube[4][2][2]
            cube[4][2][0],cube[4][2][1],cube[4][2][2]=tmp[0],tmp[1],tmp[2]
        elif direc==1: #L->F->R->B
            tmp=[cube[4][2][0],cube[4][2][1],cube[4][2][2]]
            cube[4][2][0],cube[4][2][1],cube[4][2][2]=cube[3][2][0],cube[3][2][1],cube[3][2][2]
            cube[3][2][0],cube[3][2][1],cube[3][2][2]=cube[5][2][0],cube[5][2][1],cube[5][2][2]
            cube[5][2][0],cube[5][2][1],cube[5][2][2]=cube[2][2][0],cube[2][2][1],cube[2][2][2]
            cube[2][2][0],cube[2][2][1],cube[2][2][2]=tmp[0],tmp[1],tmp[2]
    elif f==2: #front
        # U : cube[0][2][0],cube[0][2][1],cube[0][2][2]
        # L : cube[4][2][2],cube[4][1][2],cube[4][0][2]
        # D : cube[1][0][2],cube[1][0][1],cube[1][0][0]
        # R : cube[5][0][0],cube[5][1][0],cube[5][2][0]
        if direc==0: #U->L->D->R
            tmp=[cube[5][0][0],cube[5][1][0],cube[5][2][0]]
            cube[5][0][0],cube[5][1][0],cube[5][2][0]=cube[1][0][2],cube[1][0][1],cube[1][0][0]
            cube[1][0][2],cube[1][0][1],cube[1][0][0]=cube[4][2][2],cube[4][1][2],cube[4][0][2]
            cube[4][2][2],cube[4][1][2],cube[4][0][2]=cube[0][2][0],cube[0][2][1],cube[0][2][2]
            cube[0][2][0],cube[0][2][1],cube[0][2][2]=tmp[0],tmp[1],tmp[2]
        elif direc==1: #U<-L<-D<-R
            tmp=[cube[0][2][0],cube[0][2][1],cube[0][2][2]]
            cube[0][2][0],cube[0][2][1],cube[0][2][2]=cube[4][2][2],cube[4][1][2],cube[4][0][2]
            cube[4][2][2],cube[4][1][2],cube[4][0][2]=cube[1][0][2],cube[1][0][1],cube[1][0][0]
            cube[1][0][2],cube[1][0][1],cube[1][0][0]=cube[5][0][0],cube[5][1][0],cube[5][2][0]
            cube[5][0][0],cube[5][1][0],cube[5][2][0]=tmp[0],tmp[1],tmp[2]
    elif f==3: #back
        # U : cube[0][0][2],cube[0][0][1],cube[0][0][0]
        # R : cube[5][2][2],cube[5][1][2],cube[5][0][2]
        # D : cube[1][2][0],cube[1][2][1],cube[1][2][2]
        # L : cube[4][0][0],cube[4][1][0],cube[4][2][0]
        
        if direc==0: #U->R->D->L
            tmp=[cube[4][0][0],cube[4][1][0],cube[4][2][0]]
            cube[4][0][0],cube[4][1][0],cube[4][2][0]=cube[1][2][0],cube[1][2][1],cube[1][2][2]
            cube[1][2][0],cube[1][2][1],cube[1][2][2]=cube[5][2][2],cube[5][1][2],cube[5][0][2]
            cube[5][2][2],cube[5][1][2],cube[5][0][2]=cube[0][0][2],cube[0][0][1],cube[0][0][0]
            cube[0][0][2],cube[0][0][1],cube[0][0][0]=tmp[0],tmp[1],tmp[2]

        elif direc==1:#U<-R<-D<-L
            tmp=[cube[0][0][2],cube[0][0][1],cube[0][0][0]]
            cube[0][0][2],cube[0][0][1],cube[0][0][0]=cube[5][2][2],cube[5][1][2],cube[5][0][2]
            cube[5][2][2],cube[5][1][2],cube[5][0][2]=cube[1][2][0],cube[1][2][1],cube[1][2][2]
            cube[1][2][0],cube[1][2][1],cube[1][2][2]=cube[4][0][0],cube[4][1][0],cube[4][2][0]
            cube[4][0][0],cube[4][1][0],cube[4][2][0]=tmp[0],tmp[1],tmp[2]
    elif f==4: #left
        # U : cube[0][0][0],cube[0][1][0],cube[0][2][0]
        # B : cube[3][2][2],cube[3][1][2],cube[3][0][2]
        # D : cube[1][0][0],cube[1][1][0],cube[1][2][0]
        # F : cube[2][0][0],cube[2][1][0],cube[2][2][0]

        if direc==0: #U->B->D->F 
            tmp=[cube[2][0][0],cube[2][1][0],cube[2][2][0]]
            cube[2][0][0],cube[2][1][0],cube[2][2][0]=cube[1][0][0],cube[1][1][0],cube[1][2][0]
            cube[1][0][0],cube[1][1][0],cube[1][2][0]=cube[3][2][2],cube[3][1][2],cube[3][0][2]
            cube[3][2][2],cube[3][1][2],cube[3][0][2]=cube[0][0][0],cube[0][1][0],cube[0][2][0]
            cube[0][0][0],cube[0][1][0],cube[0][2][0]=tmp[0],tmp[1],tmp[2]
        elif direc==1:# U<-B<-D<-F
            tmp=[cube[0][0][0],cube[0][1][0],cube[0][2][0]]
            cube[0][0][0],cube[0][1][0],cube[0][2][0]=cube[3][2][2],cube[3][1][2],cube[3][0][2]
            cube[3][2][2],cube[3][1][2],cube[3][0][2]=cube[1][0][0],cube[1][1][0],cube[1][2][0]
            cube[1][0][0],cube[1][1][0],cube[1][2][0]=cube[2][0][0],cube[2][1][0],cube[2][2][0]
            cube[2][0][0],cube[2][1][0],cube[2][2][0]=tmp[0],tmp[1],tmp[2]

    elif f==5: #right
        # U : cube[0][2][2],cube[0][1][2],cube[0][0][2]
        # F : cube[2][2][2],cube[2][1][2],cube[2][0][2]
        # D : cube[1][2][2],cube[1][1][2],cube[1][0][2]
        # B : cube[3][0][0],cube[3][1][0],cube[3][2][0]

        if direc==0: #U->F->D->B
            tmp=[cube[3][0][0],cube[3][1][0],cube[3][2][0]]
            cube[3][0][0],cube[3][1][0],cube[3][2][0]=cube[1][2][2],cube[1][1][2],cube[1][0][2]
            cube[1][2][2],cube[1][1][2],cube[1][0][2]=cube[2][2][2],cube[2][1][2],cube[2][0][2]
            cube[2][2][2],cube[2][1][2],cube[2][0][2]=cube[0][2][2],cube[0][1][2],cube[0][0][2]
            cube[0][2][2],cube[0][1][2],cube[0][0][2]=tmp[0],tmp[1],tmp[2]
        elif direc==1: #U<-F<-D<-B
            tmp=[cube[0][2][2],cube[0][1][2],cube[0][0][2]]
            cube[0][2][2],cube[0][1][2],cube[0][0][2]=cube[2][2][2],cube[2][1][2],cube[2][0][2]
            cube[2][2][2],cube[2][1][2],cube[2][0][2]=cube[1][2][2],cube[1][1][2],cube[1][0][2]
            cube[1][2][2],cube[1][1][2],cube[1][0][2]=cube[3][0][0],cube[3][1][0],cube[3][2][0]
            cube[3][0][0],cube[3][1][0],cube[3][2][0]=tmp[0],tmp[1],tmp[2]  
    return



def solve():
    n=int(input())
    arr=input()

    cube=initCube()
    for i in range(n):
        f=face[arr[i*3]]
        direc=0 if arr[i*3+1]=='-' else 1 # clockwise=1,+ /// alock=0,-
        mrotate(cube,f,direc)

    for i in range(3):
        print(cube[0][i][0]+cube[0][i][1]+cube[0][i][2])

for _ in range(T):    
    solve()