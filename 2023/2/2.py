som=0
with open("input.txt","r") as f:
    
    for row in f:
        error=False
        i=int(row.split(":")[0].split(" ")[1])
        row=row.split(":")[1].strip()
        records=row.split(";")

        nums={"red":0,"green":0,"blue":0}

        for e in records:
            e=e.strip().split(",")
            for color in e:
                color=color.strip().split(" ")
                n=int(color[0])
                colour=color[1]

                nums[colour]=max(nums[colour],n)

        mul=1
        for e in nums.values():
            mul*=e
        som+=mul
    
print(som)