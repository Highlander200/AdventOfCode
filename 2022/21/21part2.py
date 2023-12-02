copyKnownValues=dict()
copyExpressions=dict()
with open("21/input.txt","r") as f:
    for row in f:
        row=row.replace("\n","").split()
        row[0] = row[0][:-1]

        if(len(row)==2):
            copyKnownValues[row[0]]=int(row[1])
        else:
            copyExpressions[row[0]]=[row[1],row[2],row[3]]
rootExpress=copyExpressions["root"]

def copyAll():
    global express
    global knownValues
    knownValues=dict()
    express=dict()
    for e in copyExpressions.keys():
        express[e]=copyExpressions[e]
    for e in copyKnownValues.keys():
        knownValues[e]=copyKnownValues[e]

def calculation(op1,op,op2):
    if(op=="+"):
        return op1+op2
    if(op=="/"):
        return int(op1/op2)
    if(op=="-"):
        return op1-op2
    if(op=="*"):
        return op1*op2

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

    return calculation(op1,op,op2)

def solve2():
    while(len(express.values())>0):
        operation=list(express.values())[0]
        key=list(express.keys())[0]

        value=solve(operation)

        knownValues[key]=value
        express.pop(key)

lastX=100000000
x=100000000000
while(True):
    print(x,lastX)
    input()
    copyAll()
    knownValues["humn"]=x
    solve2()
    print(knownValues[rootExpress[0]],knownValues[rootExpress[2]])
    diff=knownValues[rootExpress[0]]-knownValues[rootExpress[2]]
    if(diff!=0):
        if(diff>0):
            x+=int(diff/10)*10
        else:
            x-=int(diff/10)*10
    else:
        break
print(x)





'''
toSearch="humn"

def inverso(op1,op,op2,fract=False):
    if(op=="+"):
        return op1-op2
    if(op=="/" and fract):
        return op1*op2
    if(op=="/" and not fract):
        return int(op2/op1)
    if(op=="-"):
        return op1+op2
    if(op=="*"):
        return int(op1/op2)

def solve2(expression,value):
    op1=expression[0]
    op=expression[1]
    op2=expression[2]
    if(op1==toSearch):
        print(inverso(value,op,op1))
    if(op2==toSearch):
        print(inverso(value,op,op2,True))
    
    if(op1 in copyExpressions.keys()):
        newExpression=copyExpressions[op1]
        print(value,op,op2,knownValues[op2])
        newValue=inverso(value,op,knownValues[op2])
        solve2(copyExpressions[op1],newValue)
    if(op2 in copyExpressions.keys()):
        newExpression=copyExpressions[op2]
        print(value,op,op1,knownValues[op1])
        newValue=inverso(value,op,knownValues[op1],True)
        solve2(copyExpressions[op2],newValue)

solve2(copyExpressions["root"],knownValues["root"])
'''