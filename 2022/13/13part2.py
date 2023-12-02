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

signal=list()
with open("13/input.txt","r") as f:
    cont=0
    for row in f:
        if(cont==2):
            cont=0
        else:
            signal.append(json.loads(row))
            cont+=1
signal.append([[2]])
signal.append([[6]])
import functools

cmp = functools.cmp_to_key(compare)
signal=sorted(signal,key=cmp,reverse=True)
print(signal)
solution=(signal.index([[2]])+1)*(signal.index([[6]])+1)
print(solution)