import math

class Monkey:
    items=[]
    operation=[]
    test=1
    ifTrue=0
    ifFalse=0
    activeness=0
    def __init__(self,items,operation,test,ifTrue,ifFalse) -> None:
        self.items=items
        self.operation=operation
        self.test=test
        self.ifTrue=ifTrue
        self.ifFalse=ifFalse
    def round(self):
        ret=[]
        for i in range(len(self.items)):
            self.activeness+=1
            if(self.operation[0]=="+"):
                worryLevel=int(self.items[i])+int(self.operation[1])
            elif(self.operation[0]=="*"):
                worryLevel=int(self.items[i])*int(self.operation[1])
            else:
                worryLevel=int(self.items[i])*int(self.items[i])
            worryLevel%=maxRis
            if(worryLevel%int(self.test)==0):
                ret.append([self.ifTrue,worryLevel])
            else:
                ret.append([self.ifFalse,worryLevel])
        self.items=[]
        return ret
    def addItem(self,item):
        self.items.append(item)
    def getActiveness(self):
        return self.activeness
    def getItems(self):
        return self.items
    def getOperation(self):
        return self.operation

monkeys=[]
with open("11/input.txt","r") as f:
    contScimm=0
    i=0
    items=[]
    operation=[]
    test=1
    ifTrue=0
    ifFalse=0
    for row in f:
        if(row=="\n"):
            i=0
            contScimm+=1
            monkeys.append(Monkey(items,operation,test,ifTrue,ifFalse))
            continue
        row=row.replace("\n","").split()
        if(i==0):
            items=row
        elif(i==1):
            operation=row
        elif(i==2):
            test=row[0]
        elif(i==3):
            ifTrue=row[0]
        else:
            ifFalse=row[0]
        i+=1

def getAllActiveness():
    activenesses=[]
    for monkey in monkeys:
        activenesses.append(int(monkey.getActiveness()))
    return activenesses

def lcm(x, y):
    # Calculate the GCD of x and y
    gcd = math.gcd(x, y)

    # Use the GCD to calculate the LCM
    lcm = x * y / gcd

    return int(lcm)

def getDivisiors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors



items=[]
operations=[]
mcm=1
divisors=set()
for i in range(8):
    items.append(monkeys[i].getItems())
    operations.append(monkeys[i].getOperation())
for item in items:
    for e in item:
        for operation in operations:
            for x in getDivisiors(int(e)):
                divisors.add(x)
            if(operation[0]=="+"):
                new=int(e)+int(operation[1])
                for x in getDivisiors(new):
                    divisors.add(x)

print(divisors)
maxRis=1
for e in divisors:
    maxRis*=e
print(maxRis)

for i in range(10000):
    if(i%1000==0):
        print(getAllActiveness())
    for j in range(8):
        actions=monkeys[j].round()
        for action in actions:
            monkeys[int(action[0])].addItem(action[1])

activenesses=sorted(getAllActiveness())
print(activenesses,activenesses[-1]*activenesses[-2])