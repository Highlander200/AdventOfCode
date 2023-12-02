with open("1/input.txt","r") as f:
    s=0
    max=[]
    for i in f:
        i=i.replace("\n", "")
        if(len(i)>0):
            s+=int(i)
        else:
            max.append(s)
            s=0
print(sum(sorted(max)[-3:]))