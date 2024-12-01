with open("input.txt","r") as f:
    rows=f.readlines()

list1=[int(x.split("   ")[0]) for x in rows]
list2=[int(x.split("   ")[1]) for x in rows]

list1.sort()
list2.sort()

som=0
for (a,b) in zip(list1,list2):
    som+=abs(a-b)

print(som)