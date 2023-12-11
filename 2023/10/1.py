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

i=att[0]
j=att[1]
possib="nswe"
visited=[[False for j in range(len(data[i]))] for i in range(len(data))]
visited[i][j]=True

if(("n" in possib) and i!=0):
    if("s" in getDirect(i-1,j)):
        distances[(i-1,j)]=distances[att]+1
        att=(i-1,j)
if(("s" in possib) and i+1!=len(data)):
    if("n" in getDirect(i+1,j)):
        distances[(i+1,j)]=distances[att]+1
        att=(i+1,j)
if(("e" in possib) and j+1!=len(data[i])):
    if("w" in getDirect(i,j+1)):
        distances[(i,j+1)]=distances[att]+1
        att=(i,j+1)
if(("w" in possib) and j!=0):
    if("e" in getDirect(i,j-1)):
        distances[(i,j-1)]=distances[att]+1
        att=(i,j-1)

visited[att[0]][att[1]]=True

while(att!=(29,72)):
    i=att[0]
    j=att[1]

    possib=getDirect(i,j)

    if(("n" in possib) and i!=0):
        if((not visited[i-1][j]) and ("s" in getDirect(i-1,j))):
            distances[(i-1,j)]=distances[att]+1
            visited[i-1][j]=True
            att=(i-1,j)
    if(("s" in possib) and i+1!=len(data)):
        if((not visited[i+1][j]) and ("n" in getDirect(i+1,j))):
            distances[(i+1,j)]=distances[att]+1
            att=(i+1,j)
            visited[i+1][j]=True
    if(("e" in possib) and j+1!=len(data[i])):
        if((not visited[i][j+1]) and ("w" in getDirect(i,j+1))):
            distances[(i,j+1)]=distances[att]+1
            visited[i][j+1]=True
            att=(i,j+1)
    if(("w" in possib) and j!=0):
        if((not visited[i][j-1]) and ("e" in getDirect(i,j-1))):
            distances[(i,j-1)]=distances[att]+1
            visited[i][j-1]=True
            att=(i,j-1)

    """    
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if(visited[i][j]):
                print(i,j)
    """
    print(att)
    

print(max(distances.values())//2)