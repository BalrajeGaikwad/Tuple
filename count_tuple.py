# Python program to demonstrate the use of count() method in the case of tuples

T1 = (0, 2, 3, 6, 4, 2, 5, 6, 3, 2, 2, 6, 7, 2, 7, 8, 0, 1, 9, 1)  
T2 = ('Apple', 'Orange', 'Mango', 'Apple', 'Banana', 'Mango', 'Mango', 'Orange', 'Mango', 'Apple')  

count=T1.count(2)
print(count)

count1=T1.count(1)
print(count1)


count3=T2.count('Mango')
print(count3)