with open("6/input.txt","r") as f:
    string=list(f.readline())
    list=[string[0],string[1],string[2]]

    for i in range(3,4096):
        list.append(string[i])
        set={list[0],list[1],list[2],list[3]}
        
        if(len(set)==4):
            print(i+1)
            break
        list.pop(0)

