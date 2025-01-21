# Python program to loop through a tuple using the 'while' loop  

fruits_tuple = ("mango", "orange", "banana", "apple", "papaya", "cherry", "strawberry", "guava", "pineapple", "watermelon")  


i=0
while i<len(fruits_tuple):
    print(i,"-",fruits_tuple[i])
    i+=1