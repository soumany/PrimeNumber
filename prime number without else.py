amount=0
prime = True
for num in range(1,100):
    for i in range(2,num):
        if(num%i==0):
            prime = False
            break
    if(prime):
        amount= amount+1
        print(num)
    prime = True
print("Total amount",amount)
