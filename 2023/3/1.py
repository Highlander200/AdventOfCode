mat=[]

def isSpecial(char):
    return (not char.isdigit()) and (not char==".")

def toAdd(i,j,lenNum):
    N=len(mat)
    M=len(mat[i])

    if(j<M):
        if(isSpecial(mat[i][j])):
            return True

    for x in range(j-lenNum-1,j+1):
        if(x>=M):
            break
        
        if(i<N-1):
            if(isSpecial(mat[i+1][x])):
                return True
        if(i>1):
            if(isSpecial(mat[i-1][x])):
                return True
   
    if(j-lenNum-1>=0):
        if(isSpecial(mat[i][j-lenNum-1])):
            return True

    return False


with open("input.txt","r") as f:
    for row in f:
        mat.append(row.strip())
        
som=0
lenNum=0
for i in range(len(mat)):

    for j in range(len(mat[i])):
        if(mat[i][j].isdigit()):
            lenNum+=1
        elif(lenNum!=0):
            if(toAdd(i,j,lenNum)):
                som+=int(mat[i][j-lenNum:j])
            lenNum=0
    if(lenNum!=0):
        j=j+1
        if(toAdd(i,j,lenNum)):
            som+=int(mat[i][j-lenNum:j])
        lenNum=0
            

print(som)