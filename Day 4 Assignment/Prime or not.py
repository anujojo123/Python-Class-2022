n=int(input("Enter the value : "))
isPrime=False
i=1
for i in range(2,int(n/2)):
    if(n%i==0):
        isPrime=True
        break
if isPrime:
    print("The number is not Prime")
else:
    print("The number is Prime")
print()
        
