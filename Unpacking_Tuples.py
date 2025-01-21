# Python program to demonstrate an approach of unpacking a tuple 

fruits_tuple = ("mango", "orange", "banana", "apple", "papaya") 

print("given tuple :",fruits_tuple)

(varOne,varTwo,varThree,varFour,varFive)=fruits_tuple

print("First Variable :", varOne)  
print("Second Variable :", varTwo)  
print("Third Variable :", varThree)  
print("Fourth Variable :", varFour)  
print("Fifth Variable :", varFive)  



for i in range(len(fruits_tuple)):  
    # printing the element  
    print(i + 1, "-", fruits_tuple[i])  