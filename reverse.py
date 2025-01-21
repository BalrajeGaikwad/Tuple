#program to reverse a tuple using a loop:

my_tuple = (1, 2, 3, 4, 5)

reversed=()
for i in my_tuple:
    reversed=(i,)+reversed

print("original :",my_tuple)
print("reversed tuple",reversed)
