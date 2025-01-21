#Nested Tuple and List Processing

data = [(1, 2), [3, 4], (5, 6), [7, 8]]

total_sum=0

for item in data:
    if isinstance(item,(list,tuple)):
        total_sum+=sum(item)
    else:
        total_sum+=sum

print("total_sum :",total_sum)