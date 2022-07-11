a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
for number in range(a,b+1):
    if number >1: #1 is prime already
        for x in range (2,number): #read from 2 becasue number>1
            if (number%x)==0: 
                break
        else:
                print(number)
print()

