data=list()

def getDirect(i,j):
    char=data[i][j]
    if(char=="|"):
        res="ns"
    elif(char=="-"):
        res="we"
    elif(char=="L"):
        res="ne"
    elif(char=="J"):
        res="nw"
    elif(char=="7"):
        res="sw"
    elif(char=="F"):
        res="se"
    elif(char=="."):
        res=""

    return res


with open("input.txt","r") as f:
    i=0
    for row in f:
        row=row.strip()
        data.append(row)
        s=row.find("S")

        if(s!=-1):
            start=(i,s)

        i+=1
    
        
att=start
distances=dict()
distances[att]=0


while(att!=start):
    i=att[0]
    j=att[1]

    possib=getDirect(i,j)

    if(("n" in possib) and i!=0):
        if("s" in getDirect(i-1,j)):
            distances[(i-1,j)]=distances[att]+1
    if(("s" in possib) and i+1!=len(data)):
        if("n" in getDirect(i+1,j)):
            distances[(i+1,j)]=distances[att]+1
    if(("e" in possib) and j+1!=len(data[i])):
        if("w" in getDirect(i,j+1)):
            distances[(i,j+1)]=distances[att]+1
    if(("w" in possib) and j!=0):
        if("e" in getDirect(i,j-1)):
            distances[(i,j-1)]=distances[att]+1
    