import json

def compare(left,right):
    i=0
    while(i<len(left) and i<len(right)):
        if(type(left[i]) is int and type(right[i]) is int):
            if(left[i]<right[i]):
                return 1
            elif(left[i]>right[i]):
                return -1
        elif(type(left[i]) is list and type(right[i]) is list):
            ris=compare(left[i],right[i])
            if(ris!=0):
                return ris
        elif(type(left[i]) is list):
            ris=compare(left[i],[right[i]])
            if(ris!=0):
                return ris
        else:
            ris=compare([left[i]],right[i])
            if(ris!=0):
                return ris
        i+=1
    if(i<len(left) and i>=len(right)):
        return -1
    elif(i>=len(left) and i<len(right)):
        return 1
    return 0


with open("13/input.txt","r") as f:
    cont=0
    solution=0
    index=0
    lastRow=[]
    for row in f:
        if(cont==2):
            cont=0
            continue
        elif(cont==0):
            lastRow=json.loads(row)
        else:
            index+=1
            row=json.loads(row)
            print(index)
            if(compare(lastRow,row)==1):
                solution+=index
        cont+=1
print(solution)