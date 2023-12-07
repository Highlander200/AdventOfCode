values=[]
with open("input.txt","r") as f:
    for row in f:
        row=row.strip().split()
        values.append((row[0],int(row[1])))


def power(a):
    powera=0
    seta=list(set(a))
    if(len(seta)==1):
        powera=6
    elif(len(seta)==2):
        if(a.count(seta[0])==4 or a.count(seta[1])==4):
            powera=5
        else:
            powera=4
    elif(len(seta)==3):
        if(a.count(seta[0])==3 or a.count(seta[1])==3 or a.count(seta[2])==3):
            powera=3
        else:
            powera=2
    elif(len(seta)==4):
        powera=1
    else:
        powera=0
    return powera

def compare(a):
    a=a[0]

    powera=power(a)

    a=a.replace("A","E")
    a=a.replace("K","D")
    a=a.replace("Q","C")
    a=a.replace("J","B")
    a=a.replace("T","A")
    return (powera,a)

    
values.sort(key=compare)

print(values)


som=0
for i in range(1,1+len(values)):
    som+=values[i-1][1]*i
print(som)
