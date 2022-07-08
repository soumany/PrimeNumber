numbers = [4,2,8,9,5]
for x in range(len(numbers)):
    for y in range(x+1, len(numbers)):
        if numbers[x]>numbers[y]:
            numbers[x],numbers[y]=numbers[y],numbers[x]
print(numbers)