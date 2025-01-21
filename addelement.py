# Python program to demonstrate an approach of adding the element in the tuple by adding a new tuple to the existing one  

fruits_tuple = ("mango", "orange", "banana", "apple", "papaya")  
print("before adding a new element in tuple :")
print("original tuple =",fruits_tuple)

#creating new tuple
temp_tuple=("pineapple",)

fruits_tuple=fruits_tuple+temp_tuple

print("Adding new element - pineapple ")
print("updated tuple",fruits_tuple)