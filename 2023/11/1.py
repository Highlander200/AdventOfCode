data=list()

def printMat():
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j],end="")
        print()
    print()

with open("input1.txt","r") as f:
    for row in f:
        row=list(row.strip())
        data.append(row)
        if("#" not in row):
            data.append(row)
    printMat()
    for j in range(len(data[0])):
        isEmpty=True
        for i in range(len(data)):
            if(data[i][j]=="#"):
                isEmpty=False
                break
        
        if(isEmpty):
            for i in range(len(data)):
                
                data[i].insert(j,".")


        print(j)
        printMat()


printMat()