values=[]
with open("input1.txt","r") as f:
    for row in f:
        row=row.strip().split()
        values.append((row[0],int(row[1])))


def power(a):
    powera=0
    a=a.replace("J","")
    seta=list(set(a))
    if(len(seta)==1):
        powera=6
    elif(len(seta)==2):
        if(a.count(seta[0])==4 or a.count(seta[1])==4 or len(a)<5):
            powera=5
        else:
            powera=4
    elif(len(seta)==3):
        if(a.count(seta[0])==3 or a.count(seta[1])==3 or a.count(seta[2])==3 or len(a)<5):
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
    print(powera,a)

    a=a.replace("A","D")
    a=a.replace("K","C")
    a=a.replace("Q","B")
    a=a.replace("T","A")
    a=a.replace("J","1")
    return (powera,a)
    
values.sort(key=compare)

print(values)

som=0
for i in range(1,1+len(values)):
    som+=values[i-1][1]*i
print(som)
