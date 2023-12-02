with open("6/input.txt","r") as f:
    string=list(f.readline())
    list=[]
    for i in range(13):
        list.append(string[i])

    for i in range(13,4096):
        list.append(string[i])
        set={0}
        set.pop()
        print(list,i)
        for j in range(14):
            set.add(list[j])

        if(len(set)==14):
            print(i+1)
            break
        list.pop(0)

