#Convert a Tuple to a List and Modify It

my_tuple = (10, 20, 30, 40)

list=list(my_tuple)

print(list)

list.append(7)
print("list after appending element",list)

mpdifyed_tuple=tuple(list)
print("mpdifyed_tuple : ",mpdifyed_tuple)