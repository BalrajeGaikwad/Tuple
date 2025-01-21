#Find Common Elements in a List and a Tuple

my_list = [1, 2, 3, 4]
my_tuple = (3, 4, 5, 6)


common=[]
for i in my_list:
    if i in my_tuple:
        common.append(i)



print("commmom elements are :",common)