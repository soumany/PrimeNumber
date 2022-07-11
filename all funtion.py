amount=0
for num in range(1,100):
    if all(num%i!=0 for i in range(2,num)):
        amount=amount+1
        print(num)
print("total amount",amount)