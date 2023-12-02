knownValues=dict()
express=dict()
with open("21/input.txt","r") as f:
    for row in f:
        row=row.replace("\n","").split()
        row[0] = row[0][:-1]

        if(len(row)==2):
            knownValues[row[0]]=int(row[1])
        else:
            express[row[0]]=[row[1],row[2],row[3]]

knownValues["humn"]=3423279932940

def solve(expression):
    if(expression[0] not in knownValues):
        op1=solve(express[expression[0]])
    else:
        op1=knownValues[expression[0]]
    if(expression[2] not in knownValues):
        op2=solve(express[expression[2]])
    else:
        op2=knownValues[expression[2]]

    op=expression[1]
    if(op=="+"):
        return op1+op2
    if(op=="/"):
        return int(op1/op2)
    if(op=="-"):
        return op1-op2
    if(op=="*"):
        return op1*op2
while(len(express.values())>0):
    operation=list(express.values())[0]
    key=list(express.keys())[0]

    value=solve(operation)

    knownValues[key]=value
    express.pop(key)

print(knownValues["root"])
print(knownValues["rnsd"],knownValues["vlzj"])
