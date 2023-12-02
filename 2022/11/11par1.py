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
            worryLevel=int(worryLevel/3)
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

mcm=[]
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

for i in range(50):
    for j in range(8):
        actions=monkeys[j].round()
        for action in actions:
            monkeys[int(action[0])].addItem(action[1])

activenesses=[]
for monkey in monkeys:
    activenesses.append(int(monkey.getActiveness()))

print(sorted(activenesses)[-2:])