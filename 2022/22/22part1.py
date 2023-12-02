with open("22/input.txt","r") as f:
    flag=False
    for row in f:
        if(row=="\n"):
            flag=True
            continue

        if(not flag):
            startIndx=row.count(" ")
            
            row=row[startIndx:]
            print(row)