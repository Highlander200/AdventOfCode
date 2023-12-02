def printV(vet):
    for i in range(len(vet)):
        print(vet[i],i)
    print("\n")


input=list()
start=list()
positions=list()
with open("20/inputtest.txt","r") as f:
    i=0
    for row in f:
        row=row.replace("\n","")
        input.append(int(row))
        start.append(int(row))
        positions.append(i)
        i+=1

lenInput=len(start)

for i in range(lenInput):
    #printV(input)
    num=start[i]
    print(input,positions)
    
    newPos=positions[i]+num
    print(i,positions[i])
    if(abs(newPos)>=lenInput):
        volte=int(newPos/lenInput)
        newPos%=lenInput

        if(num>0):
            newPos+=volte
        else:
            newPos-=volte
    else:
        newPos%=lenInput
    input.pop(positions[i])
    input.insert(newPos,num)
    
    positions[i]=newPos
    
    for j in range(min(i,newPos)+1,max(i,newPos)+1):
        positions[j]-=1

num1=input[1000%lenInput]
num2=input[2000%lenInput]
num3=input[3000%lenInput]
tot=num1+num2+num3


print(num1,num2,num3)
print(tot)