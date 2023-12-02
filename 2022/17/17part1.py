with open("17/input.txt","r") as f:
    movments=list(f.read().replace("\n",""))

maxy=0
matrix=[]
movIndex=0
movLen=len(movments)
for k in range(2023):
    print(k,matrix)
    input()
    if(movIndex==movLen):
        movIndex=0
    while(len(matrix)<maxy+3):
        matrix.append(list("......."))

    shapeCount=k%5
    if(shapeCount==0):
        matrix.append(list("..@@@@."))
    elif(shapeCount==1):
        matrix.append(list("...@..."))
        matrix.append(list("..@@@.."))
        matrix.append(list("...@..."))
    elif(shapeCount==2):
        matrix.append(list("..@@@.."))
        matrix.append(list("....@.."))
        matrix.append(list("....@.."))
    elif(shapeCount==3):
        matrix.append(list("..@...."))
        matrix.append(list("..@...."))
        matrix.append(list("..@...."))
        matrix.append(list("..@...."))
    elif(shapeCount==4):
        matrix.append(list("..@@..."))
        matrix.append(list("..@@..."))

    isRest=False
    while(not isRest):
        #print(matrix)
        #input()
        if(movments[movIndex]=="<"): #left
            isPossible=True
            for row in matrix:
                for i in range(0,7):
                    if(row[i]=="@" and i==0):
                        isPossible=False
                        break
                    if(i==0):
                        continue
                    if(row[i]=="@" and row[i-1]=="#"):
                        isPossible=False
                        break
                if(not isPossible):
                    break
            if(isPossible):
                for row in range(len(matrix)):
                    for i in range(1,7):
                        if(matrix[row][i]=="@"):
                            matrix[row][i]="."
                            matrix[row][i-1]="@"
        else: #right
            isPossible=True
            for row in matrix:
                for i in range(0,7):
                    if(row[i]=="@" and i==6):
                        isPossible=False
                        break
                    if(i==6):
                        continue
                    if(row[i]=="@" and row[i+1]=="#"):
                        isPossible=False
                        break
                if(not isPossible):
                    break

            if(isPossible):
                for row in range(len(matrix)):
                    first=True
                    for i in range(0,6):
                        if(matrix[row][i]=="@"):
                            matrix[row][i+1]="@"
                            if(first):
                                matrix[row][i]="."
                                first=False

        #down
        isPossible=True
        for i in range(len(matrix)): #check possible
            row=matrix[i]
            for j in range(0,7):
                if(row[j]=="@" and i==0):
                    isPossible=False
                    break
                if(row[j]=="@" and matrix[i-1]=="#"):
                    isPossible=False
                    break
            if(not isPossible):
                break
        if(isPossible):
            for i in range(len(matrix)): #move
                for j in range(0,7):
                    if(matrix[i][j]=="@"):
                        matrix[i][j]="."
                        matrix[i-1][j]="@"
        else: #if not possible
            isRest=True
            for i in range(len(matrix)): #set "#"
                for j in range(0,7):
                    if(matrix[i][j]=="@"):
                        matrix[i][j]="#"
                        maxy=max(maxy,i)
    movIndex+=1
print(maxy)