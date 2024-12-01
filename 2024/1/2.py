with open("input.txt","r") as f:
    rows=f.readlines()

list1=[int(x.split("   ")[0]) for x in rows]
list2=[int(x.split("   ")[1]) for x in rows]

som=0
for x in list1:
    som+=x*list2.count(x)
print(som)