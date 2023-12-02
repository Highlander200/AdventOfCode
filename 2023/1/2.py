stringToInt={
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}


with open("input.txt","r") as f:
    som=0
    for row in f:
        row=row.strip()
        flag=False
        tmp=row
        for i in range(len(row)):
            for string in stringToInt.keys():
                if(tmp.startswith(string)):
                    n1=stringToInt[string]
                    flag=True
                    tmp=tmp[len(string):]
                    break
            if(flag):
                break
            if(tmp[0].isdigit()):
                n1=tmp[0]
                tmp=tmp[1:]
                break
            

            tmp=tmp[1:]

        n2=0
        flag=False
        tmp=row
        for i in range(len(row)):
            if(tmp[-1].isdigit()):
                n2=tmp[-1]
                tmp=tmp[:-1]
                break
            for string in stringToInt.keys():
                if(tmp.endswith(string)):
                    n2=stringToInt[string]
                    flag=True
                    tmp=tmp[:-len(string)]
                    break
            if(flag):
                break
            tmp=tmp[:-1]

        som+=int(n1+n2)

print(som)
