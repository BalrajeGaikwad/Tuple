#Filter Even Numbers from a Tuple and Store Them in a List

tuple = (11, 12, 13, 14, 15, 16)
list=[]

for i in range(len(tuple)):
    if tuple[i]%2==0:
        list.append(tuple[i])

print(list)
